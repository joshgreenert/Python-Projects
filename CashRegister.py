# DSC 510
# Week 11
#
# Programming Assignment Week 11
# Author: Joshua Greenert
# Date: 5/26/2022
#
# This program will have a class called CashRegister that is used to hold items the user adds to their cart.
# After the user is finished adding items to their cart, the user will be provided with their total count
# of items in their cart and the price of their items using the locale imported class.
# 
import locale

# Create the class that will host the cashregister object.
class CashRegister:
    count = 0
    total = 0.0

    def addItem(self, price):
        self.count = self.count + 1
        self.total += price

    def getTotal(self):
        return self.total

    def getCount(self):
        return self.count


# Define the main method to utilize the cashregister object.
def main():

    # Create the cash register object and add variables for costs.
    cashRegister = CashRegister()
    shoeCost = 31.45
    coatCost = 45.67

    # Set the locale
    locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )

    # Welcome the user to the program.
    print("###############################################")
    print("     Welcome to the Cash Register Program!     ")
    print("###############################################")

    # Ask the user to add products until they request to quit.
    print("Please select the product you would like to purchase.")
    userInput = input("Select 1 for shoes, 2 for coats, q to quit:")

    while(userInput != "q"):
        if(userInput == "1"):
            print(f"One order of shoes added for {shoeCost}")
            cashRegister.addItem(shoeCost)
        elif(userInput == "2"):
            print(f"One order of a coat added for {coatCost}")
            cashRegister.addItem(coatCost)
        else:
            print("ERROR: Select 1 for shoes, 2 for coats, q to quit:")

        # Reprompt the user for their choice.
        print("Please select the product you would like to purchase.")
        userInput = input("Select 1 for shoes, 2 for coats, q to quit:")

    # Print the results of the cash register object.
    print(f"Number of items in the cart: {cashRegister.getCount()}")
    print(f"Total cost for today is: {locale.currency(cashRegister.getTotal())}")


# Use an if function to call to the main function.
if __name__ == "__main__":
    main()