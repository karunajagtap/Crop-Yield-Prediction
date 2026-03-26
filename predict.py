import pandas as pd
import joblib

# load trained model
model = joblib.load("crop_yield_model.pkl")

def predict_yield(area, item, year, rainfall, pesticides, temp):
    
    # create input data exactly like training
    data = pd.DataFrame({
        "Area": [area],
        "Item": [item],
        "Year": [year],
        "average_rain_fall_mm_per_year": [rainfall],
        "pesticides_tonnes": [pesticides],
        "avg_temp": [temp]
    })

    result = model.predict(data)
    return result[0]