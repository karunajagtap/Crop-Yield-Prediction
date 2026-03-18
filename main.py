import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("yield_df.csv")

df = df.drop("Unnamed: 0", axis=1)

le_area = LabelEncoder()
le_item = LabelEncoder()

df["Area"] = le_area.fit_transform(df["Area"])
df["Item"] = le_item.fit_transform(df["Item"])

X = df.drop("hg/ha_yield", axis=1)
y = df["hg/ha_yield"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print("Model Accuracy:", score)
import joblib

joblib.dump(model, "crop_yield_model.pkl")

print("Model saved successfully!")