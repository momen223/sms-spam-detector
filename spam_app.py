import streamlit as st
import pickle
import os

# Get absolute path of current folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and vectorizer safely
model_path = os.path.join(BASE_DIR, "spam_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# Streamlit App
st.title("📩 SMS Spam Detector")
st.write("Enter a message and the app will predict whether it's **Spam** or **Not Spam**.")

# Input box
user_input = st.text_area("Type your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message before predicting.")
    else:
        # Transform message using the vectorizer
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]

        if prediction == 1:  # Assuming 1 = Spam, 0 = Not Spam
            st.error("🚨 This message is **SPAM**!")
        else:
            st.success("✅ This message is **Not Spam**.")

