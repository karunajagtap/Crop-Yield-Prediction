import joblib
import pandas as pd

model = joblib.load("crop_yield_model.pkl")


data = {
    "Area": [10],
    "Item": [2],
    "Year": [2013],
    "average_rain_fall_mm_per_year": [1200],
    "pesticides_tonnes": [100],
    "avg_temp": [25]
}

df = pd.DataFrame(data)

prediction = model.predict(df)

print("Predicted Crop Yield:", prediction[0])