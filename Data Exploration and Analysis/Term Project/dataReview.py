'''
Created by: Joshua Greenert
Date: 8/9/2022
Assignment: Term Project Code
Class: DSC530-T302

This file will allow data processes to be performed to work with and modify the datasets.
For datasets, removed all columns of data that held no significance to reduce load on performance.
'''

# Import the necessary libraries.
import os
from os.path import basename, exists
import numpy as np
import pandas as pd
import thinkstats2
import thinkplot

# Set the name of the file.
schoolFileCSV = 'c:/Users/Josh/Documents/GitHub/Python-Projects/Data Exploration and Analysis/Term Project/StudentsPerformance.csv'

# Create the dataframe to work with the data.
df = pd.read_csv(schoolFileCSV)

# Show the data and describe it to the user.
print(df.head())
print(df.describe())

# Select five variables to use within the dataset.
'''
The five variables chosen for this task are "math score", "reading score", "writing score", "gender", and "parental level of education"
'''

# Create the histograms for each variable.

mathScores = df["math score"]
readingScores = df["reading score"]
writingScores = df['writing score']
genderGroup = df["gender"]
parentLevelEducation = df["parental level of education"]

mathHist = thinkstats2.Hist(mathScores, label="Math Scores")
thinkplot.Hist(mathHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")

readingHist = thinkstats2.Hist(readingScores, label="Reading Scores")
thinkplot.Hist(readingHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")

writingHist = thinkstats2.Hist(writingScores, label="Writing Scores")
thinkplot.Hist(writingHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")

genderHist = thinkstats2.Hist(genderGroup, label="Genders")
thinkplot.Hist(readingHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")

parentLOEHist = thinkstats2.Hist(parentLevelEducation, label="Education Levels")
thinkplot.Hist(readingHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")
