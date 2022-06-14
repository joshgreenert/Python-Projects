# DSC 530
# Week 1
#
# Programming Assignment Week 1
# Author: Joshua Greenert
# Date: 6/14/2022
# 
# This program will perform several various functions that will be labeled by comments
# to describe what they will be doing.

# Define the main function.
def main():
    
    # Display the hello world text.
    print("Hello World!  I wonder why that is always the default coding text to start with")

    # Add two numbers together.
    num1 = 1
    num2 = 2
    print(f"{num1} + {num2} = {num1 + num2}")

    # Subtract a number from another number.
    print(f"{num2} - {num1} = {num2 - num1}")

    # Multiply two numbers.
    print(f"{num1} * {num2} = {num1 * num2}")

    # Divide between two numbers.
    print(f"{num2} / {num1} = {num2 / num1}")

    # Concatenate two strings together.
    word1 = "this string"
    word2 = " is beautiful"
    print(f"The two strings placed together is '{word1 + word2}'")

    # Create a list of 4 items.
    sampleList = ["bird", "dog", "cat", "rat"]
    print(f"The list with four items is {sampleList}")

    # Append an item to the list.
    sampleList.append("monkey")
    print(f"The list with a fifth item is {sampleList}")

    # Create a tuple with 4 items.
    sampleTuple = (2, 4, 6, 8)
    print(f"The tuple created with four items is {sampleTuple}")


# Use an if function to call to the main function.
if __name__ == "__main__":
    main()