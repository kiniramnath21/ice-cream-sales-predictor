import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("../model/ice_cream_model_pipeline.pkl", "rb"))

st.set_page_config(page_title="Ice Cream Sales Predictor", page_icon="🍦")

st.title("🍦 Ice Cream Sales Revenue Predictor")
st.markdown("Enter the details below to estimate today's ice cream revenue.")

# Inputs
temp = st.slider("Temperature (°C)", 5, 45, 30)
humidity = st.slider("Humidity (%)", 10, 100, 60)
day = st.selectbox("Day of the Week", ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
holiday = st.radio("Is it a Holiday?", ['Yes', 'No'])
prev_sales = st.number_input("Previous Day's Sales (₹)", min_value=0.0, step=10.0)

# Mapping inputs
day_map = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
holiday_val = 1 if holiday == 'Yes' else 0

features = np.array([[temp, humidity, day_map[day], holiday_val, prev_sales]])

# Prediction
if st.button("Predict Revenue"):
    prediction = model.predict(features)[0]
    st.success(f"📈 Predicted Sales Revenue: ₹{prediction:.2f}")
