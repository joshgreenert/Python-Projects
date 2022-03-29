# DSC 510
# Week 3
# Programming Assignment Week 3
# Author: Joshua Greenert
# Date: 3/29/2022
# 
# This program will display a welcome message, get the company name from the user, get
# the number of feet of cable from the user, evaluate the total cost, then display the 
# company, feet requested, and the total cost.
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
totalCost = 0.00

if cableInFeet > 0 and cableInFeet <= 100.00:
    totalCost = 0.87 * cableInFeet
elif cableInFeet > 100.00 and cableInFeet <= 250.00:
    totalCost = 0.80 * cableInFeet
elif cableInFeet > 250.00 and cableInFeet <= 500.00:
    totalCost = 0.70 * cableInFeet
elif cableInFeet > 500.00:
    totalCost = 0.50 * cableInFeet
else:
    print("You entered an invalid number!")
    exit()

# Print the information that was obtained for the user.
print("************************************************")
print("Thank you for shopping with us,", companyName)
print("Fiber Optic Cable (in feet):", cableInFeet)
print("Total Cost for today:", round(totalCost, 2))
print()
print("Please come again,", companyName, "!")






