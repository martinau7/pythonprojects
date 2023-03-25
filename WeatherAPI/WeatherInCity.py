import datetime as dt
import requests

# URL of the api we are using
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# Enter your API key here
API_KEY = ""
CITY = "Plovdiv"


# Function that converts kelvin to celsius and fahrenheit
def k_to_c_f(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


# Constructing a URL for making an API request to retrieve weather data for the given city.
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

# Sending an HTTP GET request to the URL, and then convert the response from JSON format to a Python object.
response = requests.get(url).json()

# Extracting specific weather data from the API response, performing conversions where necessary, and storing the
# values in variables for output.
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = k_to_c_f(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = k_to_c_f(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_celsius:.2f} C or {temp_fahrenheit:.2f} F.")
print(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f} C or {feels_like_fahrenheit:.2f} F.")
print(f"Humidity in {CITY}: {humidity} %.")
print(f"Wind speed in {CITY}: {wind_speed} m/s.")
print(f"General weather in {CITY} : {description} .")
print(f"Sun rises in {CITY} at {sunrise_time} local time. ")
print(f"Sun set in {CITY} at {sunset_time} local time. ")
