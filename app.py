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

        review = request.form["review"].strip().lower()

        # Convert review to sequence
        review_sequence = [1]  # Start token

        for word in review.split():
            review_sequence.append(word_to_id.get(word, 2) + 3)

        # Pad sequence
        review_sequence = sequence.pad_sequences(
            [review_sequence],
            maxlen=200
        )

        # Predict
        prediction = model.predict(review_sequence, verbose=0)[0][0]

        if prediction >= 0.5:
            result = "😊 Positive Review"
            color = "positive"
            confidence = round(prediction * 100, 2)
            message = (
                "The model predicts that this review expresses a "
                "positive sentiment."
            )
        else:
            result = "😞 Negative Review"
            color = "negative"
            confidence = round((1 - prediction) * 100, 2)
            message = (
                "The model predicts that this review expresses a "
                "negative sentiment."
            )

        return render_template(
            "index.html",
            review=review,
            result=result,
            confidence=confidence,
            color=color,
            message=message
        )

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
