# Install required packages before running:
# pip install streamlit scikit-learn pandas numpy joblib

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# ------------------- LOAD MODEL -------------------
@st.cache_resource
def load_model():
    model = joblib.load("heart_model.pkl")      # Ensure model.pkl is in same folder
    scaler = joblib.load("scaler.pkl")         # If you used a scaler during training
    return model, scaler

model, scaler = load_model()

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>
.title-style {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    color: #b91c1c;
    margin-bottom: 5px;
}
.subtitle-style {
    font-size: 18px;
    text-align: center;
    color: #374151;
    margin-bottom: 20px;
}
.result-box {
    background: #f3f4f6;
    padding: 20px;
    border-radius: 8px;
    font-size: 20px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------- TITLE -------------------
st.markdown('<div class="title-style">❤️ Heart Disease Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-style">Predict risk based on medical health metrics</div>', unsafe_allow_html=True)

# ------------------- INPUT FORM -------------------
st.subheader("Enter Patient Details")

age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ("Male", "Female"))
cp = st.selectbox("Chest Pain Type (0-3)", (0, 1, 2, 3))
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", (0, 1))
restecg = st.selectbox("Resting ECG (0-2)", (0, 1, 2))
thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", (0, 1))
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", (0, 1, 2))
ca = st.selectbox("Number of Major Vessels (0-4)", (0, 1, 2, 3, 4))
thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", (1, 2, 3))

# Convert categorical to numeric (if required)
sex = 1 if sex == "Male" else 0

# ------------------- PREDICT BUTTON -------------------
if st.button("Predict Heart Disease Risk"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])

    # Scale input if scaler used
    try:
        input_data = scaler.transform(input_data)
    except:
        pass  # Skip if no scaler used

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.markdown("<div class='result-box' style='color:red;'>High Risk of Heart Disease ⚠️</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-box' style='color:green;'>Low Risk of Heart Disease ✅</div>", unsafe_allow_html=True)

# ------------------- FOOTER -------------------
st.markdown("""
---
<div style='text-align:center; font-size:14px; color:#6b7280'>
Developed using <b>Streamlit</b> | Model: Logistic Regression / Random Forest  
</div>
""", unsafe_allow_html=True)
