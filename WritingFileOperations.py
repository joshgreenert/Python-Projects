
# DSC 510
# Week 9
#
# Programming Assignment Week 9
# Author: Joshua Greenert
# Date: 5/11/2022
#
# Change #1
# Change(s) Made: Modified program to print output to user-entered filename
# Date of Change: 5/11/2022
# Author: Joshua Greenert
# Change Approved by: Catie Williams
# Date Moved to Production: 5/10/2022
#
# This program will open a file and read the text line by line to remove special characters while
# adding each word to a dictionary.  The dictionary should contain the word and the count of how
# often the word occurs.  The user will be asked to provide a filename that, if not found, will
# be created where the data will be printed to.
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
    

# Define the process file function so that the dictionary is printed in a legible format.
# Pass in the user's filename and append it to add the dictionary into it.
def process_file(dictionary, userFilename):
    
    # Ask the user for their filename.
    try:
        userFileHolder = open(userFilename, 'a')
    except IOError:
        print(f"Error: The filename \"{userFilename}\" was unable to be opened.")

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
        print(f"Error: The filename \"{userFilename}\" was unable to be opened.")

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
