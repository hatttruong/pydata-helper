"""
Provide functions to read data
# return LIST:
    - to_list

# return DATAFRAME:
    - to_dataframe

# return ARRAY:
    - genfromtxt:
        + Load data with missing values handled as specified.

    - loadtxt: TODO
        + This function aims to be a fast reader for simply formatted files
        + Each row in the text file must have the same number of values

    - load: TODO
        + Load arrays or pickled objects from .npy, .npz or pickled files

    - fromregex: TODO
        + Construct an array from a text file, using regular expression parsing

    - fromstring: TODO
        + NOT load from FILE
        + A new 1-D array initialized from raw binary or text data in a string
"""

import pandas as pd
from numpy import genfromtxt


def to_list(file_path, encoding=None):
    """
    Read text file line by line

    Args:
        file_path (TYPE): path to file
        encoding (None, optional): encoding of file such as 'utf-8'

    Returns:
        LIST: list of lines
    """
    lines = []
    with open(file_path) as f:
        lines = f.readlines()
    if encoding is None:
        lines = [l.strip() for l in lines]
    else:
        lines = [l.strip().decode(encoding) for l in lines]
    return lines


def to_list_of_list(file_path, encoding=None):
    # TODO
    pass


def to_dataframe(file_path, delimiter=None, usecols=None, names=None,
                 encoding=None):
    """
    Read file by using pandas

    Args:
        file_path (str): path to input file
        delimiter (str): if None, ',' will be used. Some delimiters such as
                        tab (\t)
        usecols (None, optional): array of column index which will be used
        names (None, optional): array of column name which will be used
        encoding (None, optional): utf-8 for vietnamese


    Returns:
        pandas.DataFrame: dataframe
    """
    df = pd.read_csv(file_path,
                     delimiter=delimiter,
                     usecols=usecols,
                     header=None,
                     names=names,
                     encoding=encoding)

    return df


def to_array(file_path, delimiter=',', skip_header=0):
    """Summary

    Args:
        file_path (TYPE): Description
        delimiter (str, optional): Description
        skip_header (int, optional): Description

    Returns:
        TYPE: Description
    """
    csv_data = genfromtxt(file_path, delimiter=delimiter,
                          skip_header=skip_header)
    return csv_data
