# 🍦 Ice Cream Sales Prediction using Machine Learning

<p align="center">
  <a href="https://kiniramnath21-ice-cream-sales-predictor.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Demo">
  </a>
</p>

This project predicts ice cream sales revenue based on weather and temporal features using a machine learning model. It includes a Flask API for backend prediction and a Streamlit app for a user-friendly web interface.

---

## 📌 Features
- Input: Temperature, Humidity, Day of Week, Holiday, Previous Day's Sales
- Output: Predicted Ice Cream Revenue (in ₹)
- Trained using Linear Regression (R² ~ 98%)
- Streamlit UI and Flask API included
- Easy to run, easy to deploy

---

## 🔧 Tech Stack
- Python 3.13
- Pandas, NumPy, Scikit-learn
- Flask (API backend)
- Streamlit (Web UI)
- VS Code

---

## 📁 Project Structure
```

ice\_cream\_sales\_prediction/
├── data/                  # Contains SalesData.csv
├── model/                 # Model training script and saved model
├── app/                   # Flask API for predictions
├── streamlit\_app/         # Streamlit frontend
├── test\_api.py            # Script to test API manually
├── README.md              # Project overview (this file)

````

---

## 🚀 How to Run the Project

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/ice-cream-sales-predictor.git
cd ice-cream-sales-predictor
python -m venv venv
venv\Scripts\activate
pip install -r app/requirements.txt
````

### 2. Train the Model

```bash
cd model
python model_training.py
```

### 3. Run Flask API

```bash
cd ../app
python app.py
```

### 4. Run Streamlit App

```bash
cd ../streamlit_app
streamlit run icecream_app.py
```

---

## Sample Prediction (via API):

```json
{
  "Temperature": 30,
  "Humidity": 60,
  "DayOfWeek": 6,
  "Holiday": 0,
  "PrevSales": 600
}
```

Expected Output:

```json
{
  "Predicted Revenue": 640.75
}
```

---

## 🌐 Deployment

* ✅ **Streamlit Cloud**: Free hosting for your UI [https://streamlit.io/cloud](https://streamlit.io/cloud)
* ✅ **Flask API** (optional): Deploy via Render.com, Replit, or Railway

---

## 🧾 Credits

**Developed by:** K Ramanath  
**Email:** [kiniramnath21@gmail.com](mailto:kiniramnath21@gmail.com)  
**GitHub:** [kiniramnath21](https://github.com/kiniramnath21)

---

## 🏁 Conclusion

This project showcases how simple regression models can be used for real-world business applications. With modular deployment using Flask and Streamlit, it can easily be extended into larger forecasting systems for retail analytics.

```

