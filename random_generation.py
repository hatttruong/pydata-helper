"""
A collection of how to random data

"""
import numpy as np


def generate_linear_data(size, intercept=0, slopes=[1]):
    """Generate data with format: Y = b + W*X

    Args:
        size (TYPE): number of records
        intercept (int, optional): value of b
        slopes (list, optional): value of W (1 x *)

    Returns:
        TYPE: tuple of X and Y

    """
    x_train = []
    y_train = []

    nb_slope = len(slopes)

    for i in xrange(size):
        x = np.zeros(nb_slope)

        for j in xrange(len(x)):
            x[j] = np.random.rand()

        y = intercept + x * slopes
        x_train.append(x)
        y_train.append(y)

    return np.array(x_train), np.transpose([y_train])
