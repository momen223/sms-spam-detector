import streamlit as st
import pickle
import os

# Absolute paths
BASE_DIR = r"C:\codes and data\sms spam"

model = pickle.load(open(os.path.join(BASE_DIR, "spam_model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

st.title("📩 SMS Spam Detector")
st.write("Type a message and find out if it's Spam or Not Spam!")

message = st.text_area("Enter your SMS message:")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        message_vec = vectorizer.transform([message])
        prediction = model.predict(message_vec)[0]
        proba = model.predict_proba(message_vec)[0]

        if prediction == 1:
            st.error(f"🚨 Spam! (Confidence: {proba[1]*100:.2f}%)")
        else:
            st.success(f"✅ Not Spam (Confidence: {proba[0]*100:.2f}%)")
