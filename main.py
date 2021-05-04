import requests
import datetime as dt
import json

API_ID = "e97a2e0a"
API_KEY = "7f443bec4ee7bea8fb6c86c0f220ca51"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": input("What is your gender? "),
    "weight_kg": input("Enter your weight in kg: "),
    "height_cm": input("Enter your height in cm: "),
    "age": input("Enter your age: ")
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response = response.json()

now = str(dt.datetime.now())
divided_now = now.split(" ")
date = divided_now[0]
time = divided_now[1].split(".")[0]


duration = input("How long did your workout last? ")
for exercise in response["exercises"]:
    rows = {
        "workout":{
            "date": date,
            "time": time,
            "exercise": exercise_text,
            "duration": duration,
            "calories": exercise["nf_calories"]
        }
    }

    sheety_header = {
        "Content-Type": "application/json"
    }

    sheety_res = requests.post(url="https://api.sheety.co/cb662cbd335c18760ecd9cb30b9d13b1/workoutTracing/workouts", json=rows, headers=sheety_header)
    print(sheety_res.json())
    print(sheety_res.status_code)  

    with open("workouts.json", "a") as workout:
        json.dump(rows, workout)