"""
Provide functions to read data by using numpy package
and the return type is ndarray.

There are some functions of numpy:
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
from numpy import genfromtxt


def read_file_to_array(file_path, delimiter=',', skip_header=0):
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
