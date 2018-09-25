import pandas as pd
import numpy as np 

def peak_finder(s):
    return np.where(np.logical_and(s[2:].values < s[1:-1].values,  s[1:-1].values > s[:-2].values))[0] + 1

if __name__ == '__main__':
    s = pd.Series(list(map(int, input().split())))
    print(peak_finder(s))