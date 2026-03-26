import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# load dataset
df = pd.read_csv("data/yield_df.csv")

# selecting features (IMPORTANT: keep same names everywhere)
X = df[[
    "Area",
    "Item",
    "Year",
    "average_rain_fall_mm_per_year",
    "pesticides_tonnes",
    "avg_temp"
]]

y = df["hg/ha_yield"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "crop_yield_model.pkl")

print("Model trained and saved successfully!")