import streamlit as st
from predict import predict_yield

st.title("🌾 Crop Yield Prediction System")

st.write("Enter details to predict crop yield")

# user inputs
area = st.number_input("Area Code")
item = st.number_input("Crop Code")
year = st.number_input("Year", 1990, 2030)
rainfall = st.number_input("Average Rainfall (mm)")
pesticides = st.number_input("Pesticides Used")
temp = st.number_input("Average Temperature")

# prediction button
if st.button("Predict Yield"):
    result = predict_yield(area, item, year, rainfall, pesticides, temp)
    st.success(f"Predicted Yield: {result:.2f}")