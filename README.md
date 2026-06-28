# 🎬 MovieMind AI

A modern AI-powered web application that predicts whether a movie review expresses a **Positive** or **Negative** sentiment using a Deep Learning LSTM model trained on the IMDB Movie Reviews dataset.

---

# Live Website


---

## 📌 Overview

MovieMind AI is a sentiment analysis web application built with **Flask**, **TensorFlow/Keras**, **HTML**, and **CSS**. Users can enter a movie review, and the application uses a trained LSTM neural network to determine whether the review is positive or negative.

This project demonstrates the complete deployment workflow of a Deep Learning model, from model training to a fully functional web application.

---

## ✨ Features

- 🎬 AI-powered Movie Review Classification
- 🧠 Deep Learning LSTM Model
- 💬 Predicts Positive or Negative Sentiment
- 📊 Displays Prediction Confidence
- 💻 Modern Responsive User Interface
- 🌐 Flask Backend
- ⚡ Real-Time Predictions
- 📱 Mobile Friendly
- 🚀 Ready for Deployment on Render

---

## 🛠️ Technologies Used

### Backend

- Python
- Flask
- TensorFlow
- Keras

### Frontend

- HTML5
- CSS3

### Dataset

- IMDB Movie Reviews Dataset (50,000 Reviews)

---

## 🧠 Model Information

| Property | Value |
|----------|-------|
| Model | LSTM Neural Network |
| Dataset | IMDB Movie Reviews |
| Reviews | 50,000 |
| Framework | TensorFlow/Keras |
| Task | Binary Sentiment Classification |

---

## 📂 Project Structure

```
Movie_review_classifier/
│
├── app.py
├── Movie_review_classifier_model.keras
├── requirements.txt
├── runtime.txt
├── README.md
│
├── static/
│   ├── style.css
│   └── favicon.ico
│
└── templates/
    └── index.html
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Movie_review_classifier.git
```

### Move into the Project Folder

```bash
cd Movie_review_classifier
```

### Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. User enters a movie review.
2. The review is converted into an integer sequence using the IMDB word index.
3. The sequence is padded to a fixed length.
4. The trained LSTM model predicts the sentiment.
5. Flask displays the result along with the prediction confidence.

---

## 📸 Screenshots

### Home Page

(Add Screenshot Here)

### Prediction Result

(Add Screenshot Here)

---

## 🌍 Future Improvements

- Multi-language Support
- Movie Recommendation Integration
- Review History
- User Authentication
- Explainable AI Predictions
- Docker Support

---

## 👨‍💻 Author

**Harsha Paloju**

GitHub:
https://github.com/harsha-paloju

LinkedIn:
https://www.linkedin.com/in/harsha-paloju-44388239b/

---

## ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐**.