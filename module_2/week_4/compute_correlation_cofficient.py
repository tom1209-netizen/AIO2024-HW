import numpy as np


def compute_correlation_cofficient(x, y):
    N = len(x)
    numerator = N * np.sum(x * y) - np.sum(x) * np.sum(y)
    denominator = np.sqrt((N * np.sum(x ** 2) - np.sum(x) ** 2) * (N * np.sum(y ** 2) - np.sum(y) ** 2))
    return np.round(numerator / denominator, 2)


if __name__ == '__main__':
    X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
    Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
    print("Correlation: ", compute_correlation_cofficient(X, Y))