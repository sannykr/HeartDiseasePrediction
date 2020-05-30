import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle

st.title("Predict Heart Disease")
st.text("Please enter the following info to knwo the result:")

model = pickle.load(open('./LogisticRegression', 'rb'))

age = st.text_input(label="Age")

sex = st.selectbox("Gender", ["0", "1"])

cp = st.text_input(label="Chest Pain")

trestbps = st.text_input(label="Resting blood pressure")

chol = st.text_input(label="Serum Cholesterol in mg/dl")

fbs = st.selectbox("is fasting blood sugar > 120 mg/dl", ["0", "1"])

restecg = st.selectbox(
    'Resting Electrocardiogram Results:',
    ["0", "1", "2"]
)

thalach = st.text_input(label="Maximum Heart Rate Achieved")

exang = st.selectbox(
    'exercise induced angina:',
    ["0", "1"]
)

oldpeak = st.text_input(label="ST depression induced by exercise relative to rest")

slope = st.selectbox('The slope of the peak exercise ST segment:',
    ["0", "1", "2"]
)

ca = st.selectbox("number of major vessels (0-3) colored by flouroscopy", ["0", "1", "2", "3"])

thal = st.selectbox("Thal", ["1", "2", "3", "4", "5", "6", "7"])

pred = model.predict([[float(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang),
float(oldpeak), int(slope), int(ca), int(thal)]])

if st.button("Check The Patient"):
    with st.spinner("Predicting the Results..."):
        time.sleep(1)

    if pred==0:
        st.header("Patient has a heart problem")
    else:
        st.header("Patient is healthy")