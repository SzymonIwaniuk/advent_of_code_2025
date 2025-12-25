import pandas as pd
import math

def solve():
    # header = None prevent cut first row 
    df = pd.read_csv("puzzle.txt", sep='\s+', header=None)
    # transpose -> parse to numpy arrays -> parse to python list
    columns = df.T.values.tolist()
    res = 0
    for c in columns:
        nums = [int(num) for num in c[:-1]]
        if c[-1] == "+":
            res += sum(nums)
        else:
            res += math.prod(nums)

    return res

if __name__ == '__main__':
    print(solve())