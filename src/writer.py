"""Summary
"""
import pandas as pd
import csv


def save_list(list_data, path, lineterminator='\n', encoding=None):
    """
    Export flat list fo file using csv

    Args:
        list_data (list): list of data
        path (str): file name
        lineterminator (str, optional): line break, default is '\n'
        encoding (str, optional): encoding of data such as 'utf-8'
    """
    with open(path, 'w') as f:
        writer = csv.writer(f, lineterminator=lineterminator)
        for item in list_data:
            if encoding is not None:
                writer.writerow([item.encode(encoding)])
            else:
                writer.writerow([item])


def save_list_of_list(data, path, lineterminator='\n', encoding=None):
    """
    Export list of list fo file using csv

    Args:
        data (list of): list of data
        path (str): file name
        lineterminator (str, optional): line break, default is '\n'
        encoding (str, optional): encoding of data such as 'utf-8'
    """
    with open(path, 'w') as f:
        writer = csv.writer(f, lineterminator=lineterminator)
        if encoding is not None:
            data = [[item.encoding(encoding) for item in items]
                    for items in data]
        writer.writerows(data)


def save_dataframe(df, path, index=True, header=True, encoding=None):
    """
    Args:
        df (DataFame): dataframe contains data
        path (str): file name
        index (Boolean): write row index or not, default TRUE
        header (Boolean or list of string): Write out the column names. If a
            list of strings is given it is assumed to be aliases for the column
            names
        encoding (String, optional): None, 'utf-8', etc.
    """
    df.to_csv(path, index=index, header=header, encoding=encoding)


def quick_save_array(data, file_name, delimiter=',', ):
    """
    Write array to a file as text or binary (default).
    NOTE: Information on endianness and precision is lost, so this method is
    not a good choice for files intended to archive data or transport data
    between machines with different endianness.

    Args:
        data (TYPE): ndarray type
        file_name (TYPE): file name
        delimiter (str, optional): Separator between array items for text
            output. If empty, a binary file is written, equivalent to
            file.write(a.tobytes())
    """
    data.tofile(file_name, sep=delimiter)


def save_array(data, file_name, fmt='%.18e', delimiter='', header='',
               footer=''):
    """Summary

    Args:
        data (TYPE): Description
        file_name (TYPE): Description
        fmt (str, optional): Description
        delimiter (str, optional): Description
        header (str, optional): Description
        footer (str, optional): Description
    """
    # np.savetxt(file_name, )
    # TODO
    pass


def save_array_to_binary(data, file_name):
    """TODO

    Args:
        data (TYPE): Description
        file_name (TYPE): Description
    """
    pass
