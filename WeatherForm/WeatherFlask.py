from flask import Flask, render_template

import datetime as dt
import requests

app = Flask(__name__)

# URL of the API we are using
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# Enter your API key here
API_KEY = ""
CITY = "Plovdiv"


# Function that converts kelvin to Celsius and fahrenheit
def k_to_c_f(kelvin):
    celsius = (kelvin - 273.15).__round__()
    fahrenheit = (celsius * (9 / 5) + 32).__round__()
    return celsius, fahrenheit


@app.route('/')
def weather():
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

    return render_template('weather.html', CITY=CITY, temp_celsius=temp_celsius,
                           temp_fahrenheit=temp_fahrenheit, feels_like_celsius=feels_like_celsius,
                           feels_like_fahrenheit=feels_like_fahrenheit, humidity=humidity,
                           description=description, sunrise_time=sunrise_time, sunset_time=sunset_time,
                           wind_speed=wind_speed)


if __name__ == '__main__':
    app.run(debug=True)
