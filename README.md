Name: Mingson Leung
Course: COGS 18
Date: February 2022

Program:
    Simple user interface that provides options to the user.
    Program will output a real-time weather report based on the location the user inputs.
    Program will take either City/State or ZIP Code.
    Weather information provided by API call to OpenWeather.

Files:
    Public:
        main.py
        weather.py
        requirements.txt
        README.md
        extra_credit.txt
    Private:
        api_key.py
        test.py

Limitations:
    There is a set limit of API calls per day.
    Weather data only supports United States (intentional)

Difficulties:
    Consistent formatting for user experience
    Allowing for either City/State or ZIP Code input
    Figuring out how to make an API call and utilize the API response
    Debugging API response errors

Future Plans:
    Performance statistics
    Longitude/Latitude location support
    Images based on weather description (ASCII Art)
    An option to view basic or detailed report
    Refactoring code and increasing efficiency

API Source: https://openweathermap.org/
Limit: 1000 API Calls / day