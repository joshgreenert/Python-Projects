# DSC 510
# Week 10
#
# Programming Assignment Week 10
# Author: Joshua Greenert
# Date: 5/14/2022
#
# This program will use a get request to the Chuck Norris Jokes API endpoint to provide the
# user with as many Chuck Norris jokes they would like.
import requests

# Define the function that requests the joke for the user.
def getChuckNorrisJoke():
    endpoint = "https://api.chucknorris.io/jokes/random"
    response = requests.get(endpoint)

    # Get the response from the request.
    jsonResponse = response.json()

    # Get the value from the response.
    joke = jsonResponse['value']

    # Print the joke for the user.
    print(joke)


# Define the main function.
def main():
   
    # Welcome the user to the application.
    print("##################################################")
    print("# Welcome to the Chuck Norris Jokes Application! #")
    print("##################################################")

    # Ask the user if they would like to hear a joke.
    userInput = input("Would you like to hear a joke?\n'y' or 'Y' for yes\nEnter anything else to quit.")

    # Begin the while loop to ask the user for a Chuck Norris joke.
    while userInput.lower() == 'y':
       getChuckNorrisJoke()

       userInput = input("Would you like to hear another joke?\n'y' or 'Y' for yes\nEnter anything else to quit.")

    # Thank the user for using the program.
    print("Thanks for stopping by.\nHave a great day!")


# Use an if function to call to the main function.
if __name__ == "__main__":
    main()