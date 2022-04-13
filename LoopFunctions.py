# DSC 510
# Week 5
# Programming Assignment Week 5
# Author: Joshua Greenert
# Date: 4/12/2022
# 
# This program will define two functions, performCalculation and calculateAverage.
# performCalculation will prompt the user for two numbers, then perform the expected
# operation based on the parameter passed.  calculateAverage will ask the user how many
# numbers they would like to input, then loop to request the number from the user.  Then
# the function will calculate the total and average and print it for the user.
#
# Define the new function that will perform a calculation based on the user's input.
def performCalculation(operator):
    print('This function will perform the desired operation with two numbers.')

    # Get the numbers from the user.
    number1 = input('What is the first number?')

    # Use try/catch to convert the input to int
    try:
        number1 = int(number1)
    except:
        print('You entered a string!')

    while(isinstance(number1, int) != True and isinstance(number1, float) != True):
        print('Please enter a number!')
        number1 = input('What is the first number?')

        # Use try/catch to convert the input to int
        try:
            number1 = int(number1)
        except:
            print('You entered a string!')


    number2 = input('What is the second number?')

    # Use try/catch to convert the input to int
    try:
        number2 = int(number2)
    except:
        print('You entered a string!')

    while(isinstance(number2, int) != True and isinstance(number2, float) != True):
        print('Please enter a number!')
        number2 = input('What is the second number?')

        # Use try/catch to convert the input to int
        try:
            number2 = int(number2)
        except:
            print('You entered a string!')

    # Get the result to show at the end of execution.
    result = 0
    if(operator == "+"):
        result = number1 + number2
    elif(operator == "-"):
        result = number1 - number2
    elif(operator == "*"):
        result = number1 * number2
    elif(operator == "/"):
        try:
            result = number1 / number2
        except:
            print('Cannot divide by zero!')
            exit()
    else:
        print('How did you get here?')
        exit()
    
    # Perform the calculation for the operation.
    print('The operation (',number1, operator, number2, ') =', result)

# Define the calculateAverage function with no parameters
def calculateAverage():
    totalNumbers = input('Please enter the total numbers you wish to input')

    # Use try/catch to convert the input to int
    try:
        totalNumbers = int(totalNumbers)
    except:
        print('You entered a string!')

    while(isinstance(totalNumbers, int) != True):
        print('Error: Please enter an integer')
        totalNumbers = input('Please enter the total numbers you wish to input')

        try:
            totalNumbers = int(totalNumbers)
        except:
            print('You entered a string!')

    # User a for loop to capture all the user's numbers
    total = 0
    average = 0
    for i in range(totalNumbers):
        userNumber = input('Enter a number:')

        # Use try/catch to convert the input to int
        try:
            userNumber = int(userNumber)
        except:
            print('You entered a string!')

        while(isinstance(userNumber, int) != True and isinstance(userNumber, float) != True):
            print('Error: Enter an integer or float')
            userNumber = input('Enter a number:')

            # Use try/catch to convert the input to int
            try:
                userNumber = int(userNumber)
            except:
                print('You entered a string!')

        # Add the numbers to the total.
        total = total + userNumber

    # Calculate the average
    average = total / totalNumbers

    # Print the average for the user.
    print('The calculated average for your numbers is', average)

# Define the main function to call and set the primary portions of the program within it.
def main():
    print("************************************************")
    print("Welcome to Loop Functions!")
    print("************************************************")

    # Define a variable for the user input; q to exit.
    userInput = ''

    while(userInput != 'q'):
        print('Welcome to the loop; press "q" to quit')
        userInput = input('Press the enter key to continue...')

        # If the user wants to quit early, let them.
        if(userInput == 'q'):
            print('Thanks for trying the application!')
            exit()

        # Determine the function that the user wants to perform.
        print('Please select a function to perform:')
        userDecision = input('1 for math operations, 2 for average calculation')
        
        # Use try/catch to convert the input to int
        try:
            userDecision = int(userDecision)
        except:
            print('You entered a string!')

        while(userDecision != 1 and userDecision != 2):
            print('Error! Incorrect value entered.')
            userDecision = input('1 for math operations, 2 for average calculation')

            # Use try/catch to convert the input to int
            try:
                userDecision = int(userDecision)
            except:
                print('You entered a string!')

            # If the user entered 'q' then exit the program.
            if(userDecision == 'q'):
                print('Thanks for trying the application!')
                exit()

        # Perform an if statement to determine which function to run.
        if(userDecision == 1):
            # check the input that the user provides to ensure bad data does enter the function.
            userOperator = input('Please enter an operator (+ , -, *, or / ) ')
            while(userOperator != '+' and userOperator != '-' and userOperator != '*' and userOperator != '/'):
                print('Error! Incorrect value entered.')
                userOperator = input('Please enter an operator (+ , -, *, or / ) ')
            
            performCalculation(userOperator)

        elif(userDecision == 2):
            calculateAverage()

    

# Use an if function to call to the main function.
if __name__ == "__main__":
    main()




