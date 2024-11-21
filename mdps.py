# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:14:44 2024

@author: prati
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))

# Set custom app title and layout
st.set_page_config(page_title="Disease Prediction System", page_icon="🩺", layout="wide")

# Custom CSS for background and styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
    padding: 20px;
}
[data-testid="stSidebar"] {
    background-color: #fafafa;
    padding: 20px;
    border-right: 2px solid #eaeaea;
}
h1, h2, h3 {
    color: #333333;
    text-align: center;
}
.stButton > button {
    color: white;
    background-color: #ff4b4b;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
}
.stButton > button:hover {
    background-color: #e04141;
}
.stNumberInput > div > input, .stSelectbox > div {
    border-radius: 5px;
    border: 1px solid #cccccc;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction"],
        icons=["activity", "heart"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#fafafa"},
            "icon": {"color": "#ff4b4b", "font-size": "25px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#ffe6e6",
            },
            "nav-link-selected": {"background-color": "#ff4b4b", "color": "white"},
        },
    )

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.markdown("<h1>Diabetes Prediction 🩺</h1>", unsafe_allow_html=True)
    st.subheader("Please fill in the details below:")
    st.info("This tool predicts if a person is diabetic based on medical parameters.")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)

    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0, step=1.0)

    with col3:
        BloodPressure = st.number_input("Blood Pressure value", min_value=0.0, step=1.0)

    with col1:
        SkinThickness = st.number_input("Skin Thickness value", min_value=0.0, step=1.0)

    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0.0, step=1.0)

    with col3:
        BMI = st.number_input("BMI value", min_value=0.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value", min_value=0.0, step=0.01)

    with col2:
        Age = st.number_input("Age of the Person", min_value=0, step=1)

    # Code for prediction
    if st.button("Get Diabetes Test Result"):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                st.markdown(
                    "<div style='color: white; background-color: #ff4b4b; text-align: center; padding: 10px;'>The person is diabetic.</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<div style='color: white; background-color: #4CAF50; text-align: center; padding: 10px;'>The person is not diabetic.</div>",
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.markdown("<h1>Heart Disease Prediction ❤️</h1>", unsafe_allow_html=True)
    st.subheader("Fill in the medical details below:")
    st.info("This tool predicts if a person has heart disease.")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, step=1)

    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])

    with col3:
        cp = st.selectbox("Chest Pain types", ["Type 1", "Type 2", "Type 3", "Type 4"])

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0, step=1.0)

    with col2:
        chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=0.0, step=1.0)

    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])

    with col1:
        restecg = st.selectbox("Resting ECG results", ["Normal", "ST-T abnormality", "Left ventricular hypertrophy"])

    with col2:
        thalach = st.number_input("Maximum Heart Rate achieved", min_value=0.0, step=1.0)

    with col3:
        exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])

    with col1:
        oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0, step=0.1)

    with col2:
        slope = st.selectbox("Slope of peak exercise ST segment", ["Upsloping", "Flat", "Downsloping"])

    with col3:
        ca = st.number_input("Number of major vessels (0-4)", min_value=0, max_value=4, step=1)

    with col1:
        thal = st.selectbox("Thalassemia", ["Normal", "Fixed defect", "Reversible defect"])

    # Prediction
    if st.button("Get Heart Disease Test Result"):
        try:
            user_input = [
                age,
                1 if sex == "Male" else 0,
                cp,
                trestbps,
                chol,
                1 if fbs == "Yes" else 0,
                restecg,
                thalach,
                1 if exang == "Yes" else 0,
                oldpeak,
                slope,
                ca,
                thal,
            ]
            heart_prediction = heart_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.markdown(
                    "<div style='color: white; background-color: #ff4b4b; text-align: center; padding: 10px;'>The person has heart disease.</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<div style='color: white; background-color: #4CAF50; text-align: center; padding: 10px;'>The person does not have heart disease.</div>",
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.error(f"Error in prediction: {e}")
