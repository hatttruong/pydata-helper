"""
Provide functions to write ndarray to file

There are some functions of numpy:
    - ndarray.tofile: DONE
        +
    - save: TODO
        + Save an array to a binary file in NumPy .npy format.

    - savetxt: TODO
        + Save an array to a text file.

    - savez: TODO
        + Save several arrays into a single file in UNCOMPRESSED .npz format.

    - savez_compressed: TODO:
        + Save several arrays into a single file in compressed .npz format.

    -

"""

import numpy as np


def quick_save_array_to_file(data, file_name, delimiter=',', ):
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


def save_array_to_file(data, file_name, fmt='%.18e', delimiter='', header='',
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
