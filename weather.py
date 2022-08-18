# weather.py (Module)
# Sends an API request to api.openweathermap.org and displays data in user-friendly format.
# User can input the specific location to get the weather report of.

# Imports
import json # Standard Library
import requests # 3rd Party
import datetime # 3rd Party
import api_key # Local

# Global Variables
private_key = api_key.return_key()

def data_details():
    """
    Prints details about weather data to output stream
    
    Args:
        N/A

    Returns:
        void
    """
    print("\n---------------------- About Weather Data ----------------------")
    print("Country: United States")
    print("Language: English")
    print()
    print("City: Name of the city based on provided location")
    print("Description: Summary of weather conditions")
    print("Temperature: Intensity of heat in Imperial units (Fahrenheit)")
    print("Feels Like: Human perception of weather in Imperial units")
    print("Humidity: Percentage of water vapor in the air")
    print("Sunrise: Time that sun rises in specified location (Local Device Time)")
    print("Sunset: Time that sun sets in specified location (Local Device Time)")
    print("----------------------------------------------------------------\n")

def about_openweather():
    """
    Prints details about the API provider (Open Weather) to output stream
    
    Args:
        N/A

    Returns:
        void
    """
    print(
    "\nWeather Data is provided by OpenWeather.\n" + 
    "For more information about their team and accuracy/quality \n" +
    "of weather data, please visit https://openweathermap.org/.\n"
    )

def get_using_zip(input_zip):
    """
    Prints detailed weather report to output stream based on inputted ZIP code.
    Possible by making an API call and formatting the response.
    
    Args:
        input_zip (int): user inputted ZIP/Postal code

    Returns:
        void
    """
    # API Request URL using ZIP Code (Postal Code from USPS)
    WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?zip=" + \
        str(input_zip) + ",us&appid=" + private_key

    # Saved API Response
    api_response = requests.get(WEATHER_URL)

    # Case 1: Successful API Request
    if api_response.status_code == 200:

        # Saves response in Java Script Notation (JSON)
        data = api_response.json()

        # Main and Weather Dictionary from API response
        dict_weather = data["weather"]
        dict_main = data["main"]
        dict_sys = data["sys"]

        # City Information
        city = data["name"]  # ex: "San Diego"

        # Description of Weather
        description = dict_weather[0]["main"]  # ex: "Clear"

        # Measured Temperature
        temperature = dict_main["temp"]  # ex: "300K"
        temperature = (temperature - 273.15) * (9/5) + 32  # ex: "80.33"
        temperature = "{:.2f}".format(temperature)

        # Feels Like Temperature
        feels_like = dict_main["feels_like"]  # ex: "301K"
        feels_like = (feels_like - 273.15) * (9/5) + 32  # ex: "80.33"
        feels_like = "{:.2f}".format(feels_like)

        # Humidity Level in Percent
        humidity = "{:.2f}".format(dict_main["humidity"])

        # Sunrise/Sunset Time
        sunrise = dict_sys["sunrise"]
        sunset = dict_sys["sunset"]
        # Convert from UNIX Time to Local Device Time
        sunrise = str(datetime.datetime.fromtimestamp(float(sunrise)).strftime("%H:%M:%S"))
        sunset = str(datetime.datetime.fromtimestamp(float(sunset)).strftime("%H:%M:%S"))

        # Output Weather Information
        print("----------- WEATHER REPORT -----------")
        print("City: " + city)
        print("Description: " + description)
        print("Temperature: " + temperature + " (F)")
        print("Feels Like: " + feels_like + " (F)")
        print("Humidity: " + humidity + " (%)")
        print("Sunrise: " + sunrise)
        print("Sunset: " + sunset)
        print("--------------------------------------")
        print("(i) See \"(2) How to Interpret Weather Data\"")

    # Case 2: Unsuccessful API Request
    else:
        err_info = api_response.json()
        err_code = err_info["cod"]
        err_msg = err_info["message"]
        # ERROR: Invalid Response to API Call
        print("--------------- ERROR ---------------")
        print("Code: " + err_code)
        print("Message: " + err_msg)
        print("--------------------------------------")


def get_using_city(input_city, input_state):
    """
    Prints detailed weather report to output stream based on 
    inputted city and state combination.
    Possible by making an API call and formatting the response.
    
    Args:
        input_city (str): user inputted city
        input_state (str): user inputted state that city is in

    Returns:
        void
    """
    # API Request URL using City and State
    WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        str(input_city) + "," + str(input_state) +"&appid=" + private_key

    # Saved API Response
    api_response = requests.get(WEATHER_URL)

    # Case 1: Successful API Request
    if api_response.status_code == 200:

        # Saves response in Java Script Notation (JSON)
        data = api_response.json()

        # Main and Weather Dictionary from API response
        dict_weather = data["weather"]
        dict_main = data["main"]
        dict_sys = data["sys"]

        # City Information
        city = data["name"]  # ex: "San Diego"

        # Description of Weather
        description = dict_weather[0]["main"]  # ex: "Clear"

        # Measured Temperature
        temperature = dict_main["temp"]  # ex: "300K"
        temperature = (temperature - 273.15) * (9/5) + 32  # ex: "80.33"
        temperature = "{:.2f}".format(temperature)

        # Feels Like Temperature
        feels_like = dict_main["feels_like"]  # ex: "301K"
        feels_like = (feels_like - 273.15) * (9/5) + 32  # ex: "80.33"
        feels_like = "{:.2f}".format(feels_like)

        # Humidity Level in Percent
        humidity = "{:.2f}".format(dict_main["humidity"])

        # Sunrise/Sunset Time
        sunrise = dict_sys["sunrise"]
        sunset = dict_sys["sunset"]
        # Convert from UNIX Time to Local Device Time
        sunrise = str(datetime.datetime.fromtimestamp(float(sunrise)).strftime("%H:%M:%S"))
        sunset = str(datetime.datetime.fromtimestamp(float(sunset)).strftime("%H:%M:%S"))

        # Output Weather Information
        print("----------- WEATHER REPORT -----------")
        print("City: " + city)
        print("Description: " + description)
        print("Temperature: " + temperature + " (F)")
        print("Feels Like: " + feels_like + " (F)")
        print("Humidity: " + humidity + " (%)")
        print("Sunrise: " + sunrise)
        print("Sunset: " + sunset)
        print("--------------------------------------")
        print("(i) See \"(2) How to Interpret Weather Data\"")

    # Case 2: Unsuccessful API Request
    else:
        err_info = api_response.json()
        err_code = err_info["cod"]
        err_msg = err_info["message"]
        # ERROR: Invalid Response to API Call
        print("--------------- ERROR ---------------")
        print("Code: " + err_code)
        print("Message: " + err_msg)
        print("--------------------------------------")


# Below are examples of raw output from a successful API response and unsuccessful API failure.

"""
EXAMPLE OF API CALL FAILURE:

Error Mesage for if API calls exceed limit.
{ "cod": 429,
"message": "Your account is temporary blocked due to exceeding of requests limitation of your subscription type. 
Please choose the proper subscription http://openweathermap.org/price"
}

"""

"""
EXAMPLE OF API RESPONSE:

{
     "coord": {"lon": -122.08,"lat": 37.39},
     "weather": [
       {
         "id": 800,
         "main": "Clear",
         "description": "clear sky",
         "icon": "01d"
       }
     ],
     "base": "stations",
     "main": {
       "temp": 282.55,
       "feels_like": 281.86,
       "temp_min": 280.37,
       "temp_max": 284.26,
       "pressure": 1023,
       "humidity": 100
     },
     "visibility": 16093,
     "wind": {
       "speed": 1.5,
       "deg": 350
     },
     "clouds": {
       "all": 1
     },
     "dt": 1560350645,
     "sys": {
       "type": 1,
       "id": 5122,
       "message": 0.0139,
       "country": "US",
       "sunrise": 1560343627,
       "sunset": 1560396563
     },
     "timezone": -25200,
     "id": 420006353,
     "name": "Mountain View",
     "cod": 200
     }

"""
