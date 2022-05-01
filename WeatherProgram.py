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
# Endpoint for API call http://api.openweathermap.org/data/2.5/weather?
import requests
import time

# Define the print function for the multi-dimensional array.
def print_weather_data(weatherDataArray):
    for i in weatherDataArray:
        date = ''
        description = ''
        temperature = 0

        count = 0

        # Get the variables set to print collectively.
        for j in i:
            if(count == 0):
                date = j
                count += 1
            elif(count == 1):
                description = j
                count += 1
            elif(count == 2):
                temperature = j
    
        print("The forcast for", date)
        print(description, temperature)

# Define the zip code call to the API.
def get_zipCode_json():
    zipCode = input("Please enter the zip code you would like:")

    while (zipCode.isnumeric() != True or len(zipCode) != 5):
        print("Error: Invalid selection")
        zipCode = input("Please enter the zip code you would like:")

    tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    while (tempUnit.lower != "f" or tempUnit.lower != "c" or tempUnit.lower != "k" ):
        print("Error: Invalid selection")
        tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    # Get the user's waather data using the endpoint + appid + their zip code.
    appId = "73545cb70bb2e48c60e5a4d09cf7fd5a"
    endPoint = "http://api.openweathermap.org/data/2.5/forecast?appid=" + appId + "&zip=" + zipCode + "&units=" + tempUnit
    response = requests.get(endPoint)

    # Get the response in json format to then get the specific fields.
    jsonResponse = response.json() 
    return jsonResponse

# Define the city call to the API.
def get_city_json():
    cityName = input("Please enter the city name:")
    stateName = input("Please enter the state abbreviation:")

    tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")

    while (tempUnit.lower != "f" or tempUnit.lower != "c" or tempUnit.lower != "k" ):
        print("Error: Invalid selection")
        tempUnit = input("Would you like to view temperatures in Fahrenheit, Celsius, or Kelvin.\nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")
    
    # Get the user's waather data using the endpoint + appid + their zip code.
    appId = "73545cb70bb2e48c60e5a4d09cf7fd5a"
    endPoint = "http://api.openweathermap.org/data/2.5/weather?q=" + cityName + "," + stateName + "&appid=" + appId + "&units=" + tempUnit
    response = requests.get(endPoint)

    # Get the response in json format to then get the specific fields.
    jsonResponse = response.json() 
    return jsonResponse

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

    while zipOrCityPrompt != "1" or zipOrCityPrompt != "2":
        print("Error: Invalid selection")
        zipOrCityPrompt = input("Would you like to lookup weather data by US City or zip code?\nEnter 1 for US City 2 for zip:")

    # Get the json response from the request.
    if(zipOrCityPrompt == 1):
        jsonResponse = get_city_json()
    else:
        jsonResponse = get_zipCode_json()

    # Get the count of days
    totalDays = jsonResponse['cnt']

    # Use a for loop to access each element.
    for i in range(totalDays):

        # Set and get the date to display to the user.
        UnixEpochtimeStamp = jsonResponse['list'][i]['dt']
        convertedDate = time.strftime('%m-%d-%Y %H:%M:%S', time.localtime(UnixEpochtimeStamp))

        # Get the weather description for each day.
        weatherDescription = jsonResponse['list'][i]['weather'][0]['description']

        # Get the temperature from the data
        weatherTemperature = jsonResponse['list'][i]['main']['temp']

        # Convert the temperature to farenheit
        weatherTemperature = weatherTemperature

        # Set the items to an array
        weatherDataArray.append([convertedDate, weatherDescription, weatherTemperature])

    print_weather_data(weatherDataArray)

    



if __name__ == "__main__":
    main()



 