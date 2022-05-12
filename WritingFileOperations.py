
# DSC 510
# Week 8
#
# Programming Assignment Week 8
# Author: Joshua Greenert
# Date: 5/3/2022
#
# This program will open a file and read the text line by line to remove special characters while
# adding each word to a dictionary.  The dictionary should contain the word and the count of how
# often the word occurs.  At the end of the program, the dictionary should be printed to the 
# screen in a legible format for the user.
import re

# Define the add word function so that each word that is added is counted appropriately.
def add_word(word, dictionary):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

# Process the line to split the words and remove the special characters.
def process_line(line, dictionary):
    words = line.split()

    # Use regex to strip word.
    for word in words:
        strippedWord = re.sub(r"[^a-zA-Z0-9]+", '', word)
        strippedWord = strippedWord.lower()
        
        if(strippedWord != '' ):
            add_word(strippedWord, dictionary)
    

# Define the pretty print function so that the dictionary is printed in a legible format.
def process_file(dictionary, userFilename):
    
    # Ask the user for their filename.
    try:
        userFileHolder = open(userFilename, 'a')
    except IOError:
        print("Something happened.")

    length = len(dictionary)

    # Sort the dictionary by value instead of key.
    sortedDictionary = sorted(dictionary.items(), key = lambda kv: kv[1], reverse = True)

    # Print the length and the words in order from largest to smallest.
    userFileHolder.write(f"Length of the dictionary: {length}\n")
    userFileHolder.write("Word             Count\n")
    userFileHolder.write("----------------------\n")

    # Use a for loop to print the data.
    for i in sortedDictionary:
        userFileHolder.write("{0:12}{1:8d}\n".format(i[0], i[1]))
    

def main():

    # Open the file for the future operations.
    filename = "gettysburg.txt"

    # Create variables for later execution.
    fileHolder = {}
    dictionary = {}
    userFilename = ''

    # Ask the user for their filename.
    try:
        userFilename = input('Please enter the name of your file you would like to generate:') + ".txt"
        userFileHolder = open(userFilename, 'w')
    except IOError:
        print("Something happened.")

    # Open the file and catch the exception should it occur.
    try:
        fileHolder = open(filename, 'r')
    except IOError:
        print("Error: File not found!") 

    # Create a new object to hold the lines, then for loop them.
    lines = fileHolder.readlines()
    
    for line in lines:
        process_line(line, dictionary)
    
    # Print the data collected for the user.
    process_file(dictionary, userFilename)

    # Close the file.
    userFileHolder.close()
    fileHolder.close()

# Use an if function to call to the main function.
if __name__ == "__main__":
    main()
