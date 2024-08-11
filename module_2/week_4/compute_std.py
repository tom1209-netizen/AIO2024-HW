import numpy as np
from compute_mean import compute_mean


def compute_std(x):
    mean = compute_mean(x)
    variance = np.sum((x - mean) ** 2) / len(x)

    return np.sqrt(variance)


if __name__ == '__main__':
    X = [171, 176, 155, 167, 169, 182]
    print(compute_std(X))



