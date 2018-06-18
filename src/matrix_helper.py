"""
Some utilities for matrix
"""
import numpy as np
from scipy.sparse import csr_matrix


def init_sparse_vector(data):
    """
    Intial sparse matrix from list of tuple(col_index, value)
    Example:
        data = [(0, 3), (1, 2), (5, 7), (20, 1)]
        return: <1x21 sparse matrix of type '<class 'numpy.int64'>'
                with 4 stored elements in Compressed Sparse Row format>
    Use function toarray() to convert sparse matrix to dense matrix

    Args:
        data (list): list of (column index, value)

    Returns:
        sparse matrix
    """
    row = np.array([0] * len(data))
    col = [c for c, v in data]
    values = [v for c, v in data]
    return csr_matrix((values, (row, col)), shape=(1, max(col) + 1))


def init_sparse_matrix(data):
    """
    intial sparse matrix from list of tuple(row_index, col_index, value)

    Args:
        data (TYPE): Description
    """
    row = [r for r, c, v in data]
    col = [c for r, c, v in data]
    values = [v for r, c, v in data]
    return csr_matrix((values, (row, col)), shape=(max(row) + 1, max(col) + 1))
