# 📱 SMS Spam Detector

This is a simple machine learning project to detect spam messages using **Naive Bayes**.  
It includes a **Streamlit web app** where you can test messages.

## 🚀 How it works
1. Preprocess the SMS text (lowercase, remove stopwords, lemmatization).
2. Convert text to numbers using **TF-IDF**.
3. Predict spam/ham using a **Naive Bayes classifier**.

## 🖥️ Run the App
Clone the repo and install requirements:
```bash
pip install -r requirements.txt
streamlit run spam_app.py

