'''
Created by: Joshua Greenert
Date: 8/9/2022
Assignment: Term Project Code
Class: DSC530-T302

This file will allow data processes to be performed to work with and modify the datasets.
For datasets, removed all columns of data that held no significance to reduce load on performance.
'''

# Import the necessary libraries.
import numpy as np
import pandas as pd
import thinkstats2
import thinkplot
import statsmodels.formula.api as smf

'''
ADDITIONAL FUNCTIONS NEEDED
'''
def Cov(xs, ys, meanx=None, meany=None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)

    cov = np.dot(xs-meanx, ys-meany) / len(xs)
    return cov

def Corr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx, varx = thinkstats2.MeanVar(xs)
    meany, vary = thinkstats2.MeanVar(ys)

    corr = Cov(xs, ys, meanx, meany) / np.sqrt(varx * vary)
    return corr

class DiffMeansPermute(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = abs(np.mean(group1) - np.mean(group2))
        return test_stat

    def MakeModel(self):
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
'''
END OF FUNCTIONS
'''

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
thinkplot.Hist(genderHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")

parentLOEHist = thinkstats2.Hist(parentLevelEducation, label="Education Levels")
thinkplot.Hist(parentLOEHist)
thinkplot.Config(xlabel="Scores", ylabel="Count")

# Compare two variables against each other using PMFs.
# Get male and female data separated.
maleDF = df[df.gender == "male"]
femaleDF = df[df.gender == "female"]

# Select the math scores from each.
maleMathScores = maleDF["math score"]
femaleMathScores = femaleDF["math score"]

# Create pmfs of each.
maleMathPMF = thinkstats2.Pmf(maleMathScores)
femaleMathPMF = thinkstats2.Pmf(femaleMathScores)

# Plot the PMFs
thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(maleMathPMF, align='right', width=1, color="blue")
thinkplot.Hist(femaleMathPMF, align='left', width=1, color="red")
thinkplot.Config(xlabel = "Scores", ylabel= "Count")

thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Pmfs([maleMathPMF, femaleMathPMF])
thinkplot.Show(xlabel = "Scores")

# Create 1 CDF with a variable.
femaleMathCDF = thinkstats2.Cdf(femaleMathScores, label = "Female Math Scores")
maleMathCDF = thinkstats2.Cdf(maleMathScores, label = "Male Math Scores")

# Plot the CDF
thinkplot.Cdf(femaleMathCDF)
thinkplot.Show(xlabel = "Scores", ylabel = "CDF")

thinkplot.Cdf(maleMathCDF)
thinkplot.Show(xlabel = "Scores", ylabel = "CDF")

# Plot 1 analytical distribution.
# Using the CDF comparison
thinkplot.PrePlot(2)
thinkplot.Cdfs([femaleMathCDF, maleMathCDF])
thinkplot.Show(xlabel = "Scores", ylabel = "CDF")

# Create 2 scatterplots comparing two variables.
# Using parent LOE and male and female math scores.
maleParentLOE = maleDF["parental level of education"]
femaleParentLOE = femaleDF["parental level of education"]

thinkplot.Scatter(maleParentLOE, maleMathScores)
thinkplot.Show(xlabel = "Male Parent LOE", ylabel = "Scores")

thinkplot.Scatter(femaleParentLOE, femaleMathScores)
thinkplot.Show(xlabel = "Female Parent LOE", ylabel = "Scores")

# Provide analysis on correlation and causation.
# Replace all of the instances within the dataset to be numeric.
# "some high school" = 0, "high school" = 1, "some college" = 2, "associate's degree" = 3, "bachelor's degree" = 4, "master's degree" = 5
malePLOENumbers = []
femalePLOENumbers = []

for x in maleParentLOE:
    if x == "some high school":
        malePLOENumbers.append(0)
    elif x == "high school":
        malePLOENumbers.append(1)
    elif x == "some college":
        malePLOENumbers.append(2)
    elif x == "associate's degree":
        malePLOENumbers.append(3)
    elif x == "bachelor's degree":
        malePLOENumbers.append(4)
    elif x == "master's degree":
        malePLOENumbers.append(5)

for y in femaleParentLOE:
    if y == "some high school":
        femalePLOENumbers.append(0)
    elif y == "high school":
        femalePLOENumbers.append(1)
    elif y == "some college":
        femalePLOENumbers.append(2)
    elif y == "associate's degree":
        femalePLOENumbers.append(3)
    elif y == "bachelor's degree":
        femalePLOENumbers.append(4)
    elif y == "master's degree":
        femalePLOENumbers.append(5)

# Find the covariance.
print("Male Covariance: ", Cov(malePLOENumbers, maleMathScores))
print("Female Covariance: ", Cov(femalePLOENumbers, femaleMathScores))
'''
male = 2.9188848332501163
female = 4.407611693325978
'''

# Find the correlation.
print("Male Correlation: ", Corr(malePLOENumbers, maleMathScores))
print("Female Correlation: ", Corr(femalePLOENumbers, femaleMathScores))
'''
male = 0.14223727237303505
female = 0.19202249203600952
'''
# Conduct a test on the hypothesis.
maleData = malePLOENumbers, maleMathScores
femaleData = femalePLOENumbers, femaleMathScores

# Perform a test of difference in means.
maleHT = DiffMeansPermute(maleData)
femaleHT = DiffMeansPermute(femaleData)

# Calculate the pvalues for each.
malePValue = maleHT.PValue()
femalePValue = femaleHT.PValue()

# Print the results.
print("Male p-value: ", malePValue)
print("Female p-value: ", femalePValue)
'''
male p-value = 0.0
female p-value = 0.0
'''

# Conduct a regression analysis on a dependent or explanatory variable.
# Running multiple regression analysis.
formula = 'Q("reading score") ~ Q("math score") + Q("writing score")'

model = smf.ols(formula, data=df)
results = model.fit()
results.summary()
print(results.summary())


