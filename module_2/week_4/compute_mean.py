import numpy as np


def compute_mean(x):
    return np.sum(x) / len(x)


if __name__ == '__main__':
    X = np.array([2, 0, 2, 2, 7, 4, -2, 5, -1, -1])
    print(compute_mean(X))