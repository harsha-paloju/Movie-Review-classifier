from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb

app = Flask(__name__)

# Load the trained model
model = load_model("Movie_review_classifier_model.keras")

# Load IMDB word index
word_to_id = imdb.get_word_index()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        try:

            review = request.form["review"].strip().lower()
            print("Review:", review)

            review_sequence = [1]

            NUM_WORDS = 5000

            for word in review.split():
                idx = word_to_id.get(word, 2) + 3

                if idx < NUM_WORDS:
                    review_sequence.append(idx)
                else:
                    review_sequence.append(2)

            print(review_sequence)

            review_sequence = sequence.pad_sequences(
                [review_sequence],
                maxlen=200
            )

            prediction = model.predict(review_sequence, verbose=0)[0][0]

            print("Prediction:", prediction)

            if prediction >= 0.5:
                result = "😊 Positive Review"
                color = "positive"
                confidence = round(prediction * 100, 2)
                message = "The model predicts that this review expresses a positive sentiment."
            else:
                result = "😞 Negative Review"
                color = "negative"
                confidence = round((1 - prediction) * 100, 2)
                message = "The model predicts that this review expresses a negative sentiment."

            return render_template(
                "index.html",
                review=review,
                result=result,
                confidence=confidence,
                color=color,
                message=message
            )

        except Exception as e:
            import traceback
            traceback.print_exc()

            return f"<h1>Error</h1><pre>{e}</pre>"

    return render_template("index.html")



import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
