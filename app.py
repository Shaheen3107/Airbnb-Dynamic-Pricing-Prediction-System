import streamlit as st
import joblib
import pandas as pd
import numpy as np
print("NumPy version:", np.__version__)

# Sklearn models
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor

model = joblib.load("model_new.pkl")
columns = joblib.load("columns.pkl")

st.title("🏡 Airbnb Price Prediction")

room_type = st.selectbox("Room Type", ["Hotel room", "Private room", "Shared room"])

neighbourhood = st.selectbox("Neighbourhood", [
    "Hackney","Hammersmith and Fulham","Islington",
    "Kensington and Chelsea","Lambeth","Southwark",
    "Tower Hamlets","Wandsworth","Westminster","other"
])
latitude = st.number_input("Latitude", value=51.5074)
longitude = st.number_input("Longitude", value=-0.1278)
demand_score = st.number_input("Demand Score (0 = Low, 1 = High)",
    value=1.0,
    min_value=0.0,
    max_value=1.0,
    step=0.1)
min_night_category = st.selectbox("Minimum Night Category",
    [0, 1, 2],
    format_func=lambda x: ["Short (1–3 nights)", "Medium (4–10 nights)", "Long (10+ nights)"][x]
)


input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

input_data['latitude'] = latitude
input_data['longitude'] = longitude
input_data['demand_score'] = demand_score

for col in input_data.columns:
    if "room_type" in col:
        input_data[col] = 0

# Reset all room_type columns to 0
for col in input_data.columns:
    if col.startswith("room_type_"):
        input_data[col] = 0

# Set selected room_type to 1
selected_col = f"room_type_{room_type}"
if selected_col in input_data.columns:
    input_data[selected_col] = 1


if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price: £ {round(prediction,2)}")