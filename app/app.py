from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("../model/ice_cream_model_pipeline.pkl", "rb"))

@app.route("/")
def home():
    return "🍦 Welcome to the Ice Cream Sales Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    features = np.array([[
        data["Temperature"],
        data["Humidity"],
        data["DayOfWeek"],
        data["Holiday"],
        data["PrevSales"]
    ]])
    
    prediction = model.predict(features)[0]
    return jsonify({"Predicted Revenue": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
