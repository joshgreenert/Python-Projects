# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Joshua Greenert
# Date: 3/29/2022
# 
# This program will display a welcome message, get the company name from the user, get
# the number of feet of cable from the user, evaluate the total cost, then display the 
# company, feet requested, and the total cost.
#
# Change #1
# Changes Made: Added function to modularize code and separate the calculation performed, formatted the currency,
#               and updated the program to reference the main method.
#
# Author: Joshua Greenert
# Date: 4/3/2022
# Change Approved by: Catie Williams
# Date Moved to Production: 4/4/2022

# Define the new function that will be called with two parameters: feet and price.  
# Return the total cost for the product.
def calculate_total_cost(cableInFeet, price):
    if cableInFeet > 0 and cableInFeet <= 100.00:
        price = 0.87 * cableInFeet
    elif cableInFeet > 100.00 and cableInFeet <= 250.00:
        price = 0.80 * cableInFeet
    elif cableInFeet > 250.00 and cableInFeet <= 500.00:
        price = 0.70 * cableInFeet
    elif cableInFeet > 500.00:
        price = 0.50 * cableInFeet
    else:
        print("You entered an invalid number!")
        exit()

    return price

# Define the main function to call and set the primary portions of the program within it.
def main():
    print("************************************************")
    print("Welcome to the Conditional Execution Calculator!")
    print("************************************************")

    # Get the user's company name.
    print("Please enter the name of your company:")
    companyName = input()

    # Get the number of feet needed from the user.
    print("Please enter the amount (in feet) of fiber optic cable you need:")
    cableInFeet = float(input())

    # Determine the total cost. If 100 or less 0.87, if 250.01 to 100.01 0.80, if 500 to 250.01 0.70, or 0.50
    # Set the variable inside of scope.
    # Added format for currency and price variable.
    price = 0.00
    totalCost = '${:2,.2F}'.format(calculate_total_cost(cableInFeet, price))

    # Print the information that was obtained for the user.
    print("************************************************")
    print("Thank you for shopping with us,", companyName)
    print("Fiber Optic Cable (in feet):", cableInFeet)
    # Added format for currency.
    print("Total Cost for today:", totalCost) 
    print()
    print("Please come again,", companyName, "!")

# Use an if function to call to the main function.
if __name__ == "__main__":
    main()




