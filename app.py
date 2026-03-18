import streamlit as st
import joblib
import pandas as pd

model = joblib.load("crop_yield_model.pkl")

st.title("Crop Yield Prediction")

st.write("Enter the farming conditions to predict crop yield")

area = st.number_input("Area Code")
item = st.number_input("Crop Code")
year = st.number_input("Year", 1990, 2030)
rainfall = st.number_input("Average Rainfall")
pesticides = st.number_input("Pesticides Used")
temp = st.number_input("Average Temperature")

if st.button("Predict Yield"):

    data = {
        "Area":[area],
        "Item":[item],
        "Year":[year],
        "average_rain_fall_mm_per_year":[rainfall],
        "pesticides_tonnes":[pesticides],
        "avg_temp":[temp]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)

    st.success(f"Predicted Crop Yield: {prediction[0]:.2f}")