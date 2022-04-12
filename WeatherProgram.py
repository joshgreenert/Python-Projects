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

# Convert the temperature to fahrenheit
# F = 9/5(K - 273) + 32
def convert_to_fahrenheit(temp):
    return '{:2,.2F}'.format(9.0 / 5.0 * (temp - 273.0) + 32.0)

# Start the main program here.
def main():

    # Create the array variables.
    weatherDataArray = []

    # Welcome the user.
    print("Welcome to the weather application!")
    zipCode = input("Please enter the zip code you would like:")

    # Get the user's waather data using the endpoint + appid + their zip code.
    appId = "73545cb70bb2e48c60e5a4d09cf7fd5a"
    endPoint = "http://api.openweathermap.org/data/2.5/forecast?appid=" + appId + "&zip=" + zipCode
    response = requests.get(endPoint)

    # Get the response in json format to then get the specific fields.
    jsonResponse = response.json() 

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
        weatherTemperature = convert_to_fahrenheit(weatherTemperature)

        # Set the items to an array
        weatherDataArray.append([convertedDate, weatherDescription, weatherTemperature])

    print_weather_data(weatherDataArray)

    



if __name__ == "__main__":
    main()



 