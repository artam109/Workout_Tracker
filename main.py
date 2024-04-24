import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")

basic = HTTPBasicAuth("artam", "fsvom43npjpo51ona")

GENDER = "MALE"
WEIGHT_KG = "70"
HEIGHT = "170.0"
AGE = "24"

exercise_input = input("Tell which exercise you did today?: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}


parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
exercise_data = data["exercises"]

######################## Google Sheety ##########################
x = datetime.now()
today_date = x.strftime("%x")
time_now = x.strftime("%X")

for i in range(0,len(exercise_data)):
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise_data[i]["name"].title(),
            "duration": exercise_data[i]["duration_min"],
            "calories": exercise_data[i]["nf_calories"],
        }
    }
    s_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=basic)
    s_response.raise_for_status()
    print(s_response.text)

