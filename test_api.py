import requests

url = "http://127.0.0.1:5000/predict"

payload = {
    "Temperature": 30,
    "Humidity": 60,
    "DayOfWeek": 6,
    "Holiday": 0,
    "PrevSales": 600
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Prediction:", response.json())
