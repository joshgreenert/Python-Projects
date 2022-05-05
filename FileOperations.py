# DSC 510
# Week 8
#
# Programming Assignment Week 8
# Author: Joshua Greenert
# Date: 5/3/2022
#
# This program will 
import re

#def add_word(word, dictionary):

def process_line(line, dictionary):
    words = line.split()

    for word in words:
        strippedWord = re.sub('[^A-Za-z]+', '', word )
        print(strippedWord)
        #add_word(word, dictionary)

#def pretty_print:

def main():

    # Open the file for the future operations.
    filename = "gettysburg.txt"

    # Create variables for later execution.
    fileHolder = {}
    dictionary = {}

    # Open the file and catch the exception should it occur.
    try:
        fileHolder = open(filename, 'r')
    except OSError:
        print("Error: File not found!") 
        
    for line in fileHolder:
        process_line(line, dictionary)
    

    # Print the data collected for the user.
    # pretty_print()

    # Close the file.
    fileHolder.close()

# Use an if function to call to the main function.
if __name__ == "__main__":
    main()
