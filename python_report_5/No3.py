import numpy as np


def nearest_value(X, target):
    return X[np.abs(X - target).argmin()]


if __name__ == "__main__":
    X = np.array([1, 2, 3, 4, 5, 6, 7])
    target = 4.3
    print(f"가장 인접한 값: {nearest_value(X, target)}")
    target = float(input())
    print(f"가장 인접한 값: {nearest_value(X, target)}")
