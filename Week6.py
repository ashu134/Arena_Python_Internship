#Program: Display Current Date and Time

'''
from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now)
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

'''

#Weather App – Fetch Data from API

'''
import requests

city = input("Enter city name: ")
api_key = "YOUR_API_KEY"
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)
data = response.json()

print("City:", data["location"]["name"])
print("Temperature:", data["current"]["temp_c"], "°C")
print("Condition:", data["current"]["condition"]["text"])

'''

#Currency Converter Using Real Exchange Rates

'''
import requests

amount = float(input("Enter amount in USD: "))

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()

rate = data["rates"]["INR"]
converted = amount * rate

print("Rate:", rate)
print("Amount in INR:", converted)

'''

#Program: Generate Random Data

'''
import random

print("Random Number 1-100:", random.randint(1, 100))
print("Random Choice:", random.choice(["Apple", "Banana", "Mango"]))
print("Random Float:", random.random())


'''

#Practice Installing and Using Packages

'''
import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Sahil"],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)

'''

#Working with JSON Data from APIs

'''

import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)
data = response.json()

print("Login:", data["login"])
print("ID:", data["id"])
print("Public Repos:", data["public_repos"])


'''


#Build a Weather Application that fetches current weather for any city using a free weather API and displays formatted results

'''
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your real WeatherAPI key
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        print("\n----- Current Weather Report -----")
        print("City:", data["location"]["name"])
        print("Country:", data["location"]["country"])
        print("Local Time:", data["location"]["localtime"])
        print("Temperature:", data["current"]["temp_c"], "°C")
        print("Condition:", data["current"]["condition"]["text"])
        print("Humidity:", data["current"]["humidity"], "%")
        print("Wind Speed:", data["current"]["wind_kph"], "km/h")
        print("----------------------------------\n")
    else:
        print("Error fetching weather data. Please check the city name!")


# ------- Main Program -------
city_input = input("Enter city name: ")
get_weather(city_input)

'''