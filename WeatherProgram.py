# DSC 510
# Week 4
# Programming Course Project
# Author: Joshua Greenert
# Date: 4/3/2022
# 
# This program will interact with a webservice in order to obtain data about the weather.  The user will be 
# prompted for their city or zip code? and request weather forcast data from OpenWeatherMap to provide the
# user with legible data.
#
import requests
import time

# Define the print function for the multi-dimensional array.
def print_weather_data(weatherDataArray):
    print(f"The forcast for {weatherDataArray[0][1]} on {weatherDataArray[0][0]} is {weatherDataArray[0][2]}")
    print(f"There will be a high of {weatherDataArray[0][3]} and a low of {weatherDataArray[0][4]}.")
    print(f"Pressure: {weatherDataArray[0][5]}")
    print(f"Humidity: {weatherDataArray[0][6]}")
    print(f"Cloud Cover: {weatherDataArray[0][7]}")

# Define the zip code call to the API.
def get_zipCode_json():
    zipCode = input("Please enter the zip code you would like:")

    while (zipCode.isnumeric() != True and len(zipCode) != 5):
        print("Error: Invalid selection")
        zipCode = input("Please enter the zip code you would like:")

    tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    while (tempUnit.lower() != "f" and tempUnit.lower() != "c" and tempUnit.lower() != "k" ):
        print("Error: Invalid selection")
        tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    # Determine the type of units to use and set that to the tempUnit variable.
    if(tempUnit == "f"):
        tempUnit = "imperial"
    elif(tempUnit == "c"):
        tempUnit = "metric"
    else:
        tempUnit = "standard"

    # Get the user's geocode json array.
    appId = "73545cb70bb2e48c60e5a4d09cf7fd5a"

    geoEndPoint = "http://api.openweathermap.org/geo/1.0/zip?zip=" + zipCode + "&appid=" + appId
    response = requests.get(geoEndPoint)

    # Get the response from the geocode request.
    geoJsonResponse = response.json() 

    # Get lat and lon from the json response.
    lon = geoJsonResponse['lon']
    lat = geoJsonResponse['lat']

    currentWeatherEndPoint = "https://api.openweathermap.org/data/2.5/weather?appid=" + str(appId) + "&units=" + str(tempUnit) + "&lat=" + str(lat) + "&lon=" + str(lon)

    # Get the response from the geocode request.
    response = requests.get(currentWeatherEndPoint) 

    # Get the response from the geocode request.
    currentWeatherJsonResponse = response.json()

    return currentWeatherJsonResponse

# Define the city call to the API.
def get_city_json():
    cityName = input("Please enter the city name:")
    stateName = input("Please enter the state abbreviation:")

    tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    while (tempUnit.lower() != "f" and tempUnit.lower() != "c" and tempUnit.lower() != "k" ):
        print("Error: Invalid selection")
        tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    # Determine the type of units to use and set that to the tempUnit variable.
    if(tempUnit == "f"):
        tempUnit = "imperial"
    elif(tempUnit == "c"):
        tempUnit = "metric"
    else:
        tempUnit = "standard"
    
    # Get the user's waather geocode json array.
    appId = "73545cb70bb2e48c60e5a4d09cf7fd5a"

    geoEndPoint = "http://api.openweathermap.org/geo/1.0/direct?q={" + cityName + "," + stateName + "}&appid=" + appId
    response = requests.get(geoEndPoint)

    # Get the response from the geocode request.
    geoJsonResponse = response.json() 

    # Get lat and lon from the json response.
    lon = geoJsonResponse[0]['lon']
    lat = geoJsonResponse[0]['lat']

    currentWeatherEndPoint = "https://api.openweathermap.org/data/2.5/weather?appid=" + str(appId) + "&units=" + str(tempUnit) + "&lat=" + str(lat) + "&lon=" + str(lon)

    # Get the response from the geocode request.
    response = requests.get(currentWeatherEndPoint) 

    # Get the response from the geocode request.
    currentWeatherJsonResponse = response.json()

    return currentWeatherJsonResponse

# Define the method that returns a zip code API object array.
def get_weather_data(jsonResponse):
    # Get the count of days
    weatherDataArray = []

    # Get the date and convert it for the user.
    UnixEpochtimeStamp = jsonResponse['dt']
    convertedDate = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(UnixEpochtimeStamp))

    # Get the other variables set to pass in the array object.
    cityName = jsonResponse['name']
    currentTemp = jsonResponse['main']['temp']
    highTemp = jsonResponse['main']['temp_max']
    lowTemp = jsonResponse['main']['temp_min']
    pressure = jsonResponse['main']['pressure']
    humidity = jsonResponse['main']['humidity']
    cloudCover = jsonResponse['weather'][0]['description']

    # Add the items to the weather data array.
    weatherDataArray.append([convertedDate, cityName, currentTemp, highTemp, lowTemp, pressure, humidity, cloudCover])

    return weatherDataArray

# Define the method that returns a city API object array.
def get_weather_data_city(jsonResponse):
    # Get the count of days
    weatherDataArray = []

# Start the main program here.
def main():

    # Create the static variables.
    weatherDataArray = []
    jsonResponse = ""

    # Welcome the user and get the user's weather lookup request.
    print("###################################")
    print("Welcome to the weather application!")
    print("###################################")

    zipOrCityPrompt = input("Would you like to lookup weather data by US City or zip code?\nEnter 1 for US City 2 for zip:")

    while zipOrCityPrompt != "1" and zipOrCityPrompt != "2":
        print("Error: Invalid selection")
        zipOrCityPrompt = input("Would you like to lookup weather data by US City or zip code?\nEnter 1 for US City 2 for zip:")

    # Get the json response from the request.
    jsonResponse = get_city_json() if zipOrCityPrompt == "1" else get_zipCode_json()

    # Get the weather data from the json into an array.
    weatherDataArray = get_weather_data(jsonResponse)

    print_weather_data(weatherDataArray)



if __name__ == "__main__":
    main()



 