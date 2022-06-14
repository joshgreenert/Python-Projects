# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Joshua Greenert
# Date: 4/17/2022
#
# This program will ask a user for temperatures and will continue asking for
# new values from the user until they enter the letter 'q' to quit the program.  Afterwards,
# the program will print the largest and smallest temeratures along with how many temeratures 
# were entered in the list.

# Define the main method to use other functions within it.
def main():

    # Create the list
    temperatureList = []
    userInput = ''

    # Introduce the program to the user.
    print('Welcome to the Temperature Program!')

    # While user has not entered 'q', keep asking for the temperature.
    while(userInput != 'q'):
        try:
            newTemperature = 0
            userInput = input('Please enter a temperature: ')

            # Check if the user opted to quit the program.
            if(userInput == 'q'):
                break
            else:
                newTemperature = float(userInput)

            # Append the new temperature to the list.
            temperatureList.append(newTemperature)

        except: 
            print('Please enter a value that is an integer or float!')

    if(len(temperatureList) == 0):
        print('No temperatures were entered.  Have a great day!')
    else:
        # Set the values for all the temperatures (highest, lowest, count)
        tempCount = len(temperatureList)
        tempMax = max(temperatureList)
        tempMin = min(temperatureList)

        # Print all the values to the user.
        print(f'\nThe total number of temperatures entered was: {tempCount}')
        print(f'The highest temperature entered was: {tempMax}')
        print(f'The lowest temperature entered was: {tempMin}')

# Use an if function to call to the main function.
if __name__ == "__main__":
    main()
