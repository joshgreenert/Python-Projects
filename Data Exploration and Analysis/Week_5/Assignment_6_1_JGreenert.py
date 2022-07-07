'''
DSC 530
Week 5

Programming Assignment Week 5
Author: Joshua Greenert
Date: 7/6/2022

Compute the median, mean, skewness, and peason's skewness of the resulting sample.  What fraction
of households report a taxable income below the mean?  How do the results depend on the assumed
upper bound?
'''
import density
import thinkplot
import hinc
import thinkstats2
import numpy as np

# Pull in the hinc2.py function
def InterpolateSample(df, log_upper=6.0):

    # compute the log10 of the upper bound for each range
    df['log_upper'] = np.log10(df.income)

    # get the lower bounds by shifting the upper bound and filling in
    # the first element
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0

    # plug in a value for the unknown upper bound of the highest range
    df.log_upper[41] = log_upper

    # use the freq column to generate the right number of values in
    # each range
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, int(row.freq)) # Had to add int coercion
        arrays.append(vals)

    # collect the arrays into a single sample
    log_sample = np.concatenate(arrays)
    return log_sample

# Define the main method.
def main():
    # Create a data.frame object.
    dataframe = hinc.ReadData()
    log_sample = InterpolateSample(dataframe, log_upper=6.0)

    # Create the cdf from the log sample.
    cdf = thinkstats2.Cdf(log_sample)

    # Graph the cdf.
    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel="Income", ylabel="Data")

    # Create the sample; sample is up to 1,000,000
    sample = pow(10, log_sample)

    # According to density.py, Summarize returns two results.
    mean, median = density.Summarize(sample)

    # Get the CDF of the log log sample
    logCDF = thinkstats2.Cdf(sample)
    print(f'Percentages of houses that reported taxable income below mean: {logCDF[mean]}')

    # Create the PDF
    pdf = thinkstats2.EstimatedPdf(sample)

    # Plot the sample of the PDF.
    thinkplot.Pdf(pdf)
    thinkplot.Show(xlabel="Income", ylabel="Data")

# call the main function.
if __name__ == '__main__':
    main()