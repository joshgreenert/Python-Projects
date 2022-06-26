'''
DSC 530
Week 3

Programming Assignment Week 3
Author: Joshua Greenert
Date: 6/25/2022

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier
than others.  Compute Cohen's d to quantify the difference between the groups.  How does
it compare to the difference in pregnancy length?
'''
import first
import math

def main():

    # Using Cohen's D (mean difference / standard deviation) to quantify the difference between groups.
    # femResp.pregordr If the pregordr is 1, then it's the first born; otherwise, it's after the first.
    # Live is not used but is required to unpack the data.
    live, firstBorns, others = first.MakeFrames()

    # Find the means for each group.
    firstBornMean = firstBorns.totalwgt_lb.mean()
    otherMean = others.totalwgt_lb.mean()

    print(f'The first born child mean is {firstBornMean}')
    print(f'The other born child mean is {otherMean}')

    # Mean difference
    meanDifference = firstBornMean - otherMean
    print(f'The difference between the two means is {meanDifference}')
    
    # Determine the length for each group.
    firstLength = len(firstBorns)
    otherLength = len(others)

    # Determine the variance for the groups.
    firstVariance = firstBorns.totalwgt_lb.var()
    otherVariance = others.totalwgt_lb.var()

    # Find the pooled variance to determine cohen's d
    pooledVariance = (firstLength * firstVariance + otherLength * otherVariance) / (firstLength + otherLength)
    cohensD =  meanDifference / math.sqrt(pooledVariance)
    
    print(f'Cohen\'s d is {cohensD}')
    print('Since Cohen\'s d was negative, the mean for the other children is larger than the mean for first borns.')
    print('Additionally, since the value is 0.08, we can determine that the effect difference is small when comparing'+
        ' the two values.')

if __name__ == '__main__':
    main()
