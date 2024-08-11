import numpy as np


def compute_median(x):
    size = len(x)
    x = np.sort(x)

    if size % 2 == 0:
        return (x[size//2 - 1] + x[size//2]) / 2
    else:
        return x[size//2]


if __name__ == '__main__':
    X = [1, 5, 4, 4, 9, 13]
    print("Median: ", compute_median(X))
