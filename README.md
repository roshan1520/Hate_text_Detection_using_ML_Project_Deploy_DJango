# Hate Text Detection using ML - Project Deployment with Django

This is a machine learning project to detect hate speech or offensive content in text using Natural Language Processing (NLP) techniques and classification models. The model is integrated into a Django web application for real-time detection via a user-friendly interface.

## 👤 Author

**Roshan Gupta**

## 📌 Features

- Detects hate or offensive text using a trained ML model.
- Web interface to input text and get instant predictions.
- Django-powered backend for serving predictions.
- HTML templates for a clean and responsive frontend.
- Model and vectorizer are serialized using `pickle`.

## 🧠 ML Techniques Used

- Text preprocessing (lowercasing, punctuation removal, stopword removal)
- TF-IDF Vectorization
- Logistic Regression Classifier

## 🚀 Tech Stack

- **Backend:** Python, Django
- **ML/NLP:** Scikit-learn, NLTK, Pandas, NumPy
- **Frontend:** HTML, CSS (optional for styling)
- **Deployment Ready:** Structure is ready for deployment on Heroku or any cloud platform


## ⚙️ Setup Instructions

**Clone the repo**

```bash
git clone https://github.com/yourusername/Hate_text_Detection_using_ML_Project_Deploy_DJango.git
cd Hate_text_Detection_using_ML_Project_Deploy_DJango
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver



