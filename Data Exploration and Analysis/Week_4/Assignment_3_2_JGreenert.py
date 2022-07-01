'''
DSC 530
Week 4

Programming Assignment Week 4
Author: Joshua Greenert
Date: 6/29/2022

x = Ep^(i)x^(i)
S^2 = Ep^(i)(x^(i) - x)^ 2
Write functions called PmfMean and PmfVar that take a Pmf object and compute
the mean and variance.  To test these methods, check that they are consistent
with the methods Mean and Var provided by Pmf.
'''
import nsfg
import first
import thinkstats2
import thinkplot

# Returns the mean of the pmf.
def PmfMean(pmf):
    mean = 0.0 # set to float just in case.

    for i, j in pmf.Items():
        mean += i * j
    return mean

# Returns the pmf variance.
def PmfVar(pmf):

    variance = 0.0 # set to float just in case.

    # Set the mean for the pmf to use in the equation below.
    pmfMean = pmf.Mean()

    for i, j in pmf.Items():
        variance += j * (i - pmfMean) ** 2
    return variance

# Define the main function.
def main():
    # Pull in the data.
    live, firsts, others = first.MakeFrames()

    pregnancyLength = live.prglngth

    # Create the pmf object.
    pmf = thinkstats2.Pmf(pregnancyLength)

    # Set the standard methods to compare against.
    standardMean = pmf.Mean()
    standardVar = pmf.Var()

    # Set the variables using the new methods.
    mean = PmfMean(pmf)
    var = PmfVar(pmf)

    print(f'The standard mean is {standardMean} and the new mean is {mean}')
    print(f'The standard var is {standardVar} and the new var is {var}')

# call the main function.
if __name__ == '__main__':
    main()