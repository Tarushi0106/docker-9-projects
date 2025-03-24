import streamlit as st
import pandas as pd
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "titanic_model.pkl")
# Load the trained model
model = joblib.load(model_path)

# Set Streamlit Page Config
st.set_page_config(page_title="🚢 Titanic Survival Prediction", layout="wide")

# Custom CSS for a Modern UI
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #2c3e50, #4ca1af);
        color: white;
    }
    .title {
        font-size: 45px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #3498db; /* Blue color for text */
        font-weight: bold;
        margin-bottom: 40px;
    }
    .form-container {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 35px;
        box-shadow: 0 5px 20px rgba(255, 255, 255, 0.2);
        max-width: 600px;
        margin: auto;
        text-align: center;
    }
    .stButton > button {
        background-color: #ff6b6b !important;
        color: white !important;
        font-size: 18px;
        border-radius: 8px;
        padding: 12px 24px;
    }
    .stButton > button:hover {
        background-color: #ff4757 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title & Subtitle
st.markdown('<div class="title">🚢 Titanic Survival Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Can you survive the Titanic disaster? Enter details below and find out!</div>', unsafe_allow_html=True)

# Input Fields (Styled as a Container)
st.markdown('<div class="form-container">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("🛳 Passenger Class", [1, 2, 3])
    sex = st.selectbox("👤 Sex", ['Male', 'Female'])
    age = st.slider("📅 Age", 0, 80, 25)

with col2:
    sibsp = st.number_input("👨‍👩‍👧‍👦 Siblings/Spouses Aboard", 0, 10, 0)
    parch = st.number_input("👶 Parents/Children Aboard", 0, 10, 0)
    fare = st.slider("💰 Fare Paid", 0, 500, 20)

st.markdown('</div>', unsafe_allow_html=True)

# Prediction Button
if st.button("🔮 Predict Survival"):
    with st.spinner("🧠 Analyzing..."):
        try:
            # Convert categorical values
            sex_binary = 1 if sex == 'Female' else 0
            input_data = pd.DataFrame([[pclass, sex_binary, age, sibsp, parch, fare]],
                                      columns=['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare'])

            # Make Prediction
            prediction = model.predict(input_data)
            result = "🎉 Survived! You made it! 🟢" if prediction[0] == 1 else "💔 Did not survive. 😢 🔴"

            # Display Result
            if prediction[0] == 1:
                st.success(result)
            else:
                st.error(result)

        except Exception as e:
            st.error(f"⚠️ Prediction Error: {e}")

