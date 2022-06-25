"""
# DSC 530
# Week 3
#
# Programming Assignment Week 3
# Author: Joshua Greenert
# Date: 6/25/2022
#
# This program will read the data from the 2002FedResp.dat.gz file to print the value counts for the
# pregnum.  Moreover, it will cross-validate the respondent and pregnancy files by comparing each
# pregnum for each respondent with the number of records in the pregnancy file.
"""

import sys
import numpy as np
import thinkstats2

from collections import defaultdict


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):

    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df

# Grabbed from the nsfg.py file to reduce imports.
def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def ValidatePregnum(resp):

    # read the pregnancy frame
    preg = ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = MakePregMap(preg)
    
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def MakePregMap(df):
    """Make a map from caseid to list of preg indices.

    df: DataFrame

    returns: dict that maps from caseid to list of indices into `preg`
    """
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid].append(index)
    return d

def main():
    # Pull in the dataframe to an object.
    femResp = ReadFemResp()

    # Display the length of the femResp object.
    print(f'The length of the file provided is {len(femResp)}')
    
    # Display the value counts for the pregnum variable.
    print('The value counts for the pregnum variable')
    print(femResp.pregnum.value_counts())

    # Use the existing validation function to validate the pregnum data.
    print(f'Does the data match the expected values?: {ValidatePregnum(femResp)}')  # Should return True


if __name__ == '__main__':
    main()
