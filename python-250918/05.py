import sys
import numpy as np
import pandas as pd

def df_diag_ones(df):
    df.values[range(df.shape[0]), range(df.shape[1])] = 0
    df.values[range(df.shape[0]), range(df.shape[1] - 1, -1, -1)] = 0
    return df

if __name__ == '__main__':
    df = []
    for line in sys.stdin.readlines():
        df.append(list(map(int, line.split())))
    df = pd.DataFrame(df)
    print(df_diag_ones(df).values)
