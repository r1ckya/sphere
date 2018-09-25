import numpy as np

def zeros_insert(k, n):
    idxs = np.array([[i] * n for i in range(len(k) - 1, 0, -1)]).flatten()
    return np.insert(k, idxs, np.zeros(n * (len(k) - 1))).astype(np.float64)

if __name__ == '__main__':
    print(zeros_insert(list(map(float, input().split())), int(input())))
    