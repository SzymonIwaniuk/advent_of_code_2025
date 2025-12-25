import pandas as pd
import math

def solve():
    # header = None prevent cut first row 
    df = pd.read_csv("test_puzzle.txt", sep='\s+', header=None)
    # transpose -> parse to numpy arrays -> parse to python list
    columns = df.T.values.tolist()
    res = 0

    for c in columns:
        df = pd.DataFrame(c[:-1])
        rows = df[0].tolist()
        max_len = max(len(r) for r in rows)
        matrix = [list(r.rjust(max_len)) for r in rows]
        print(df)
        print(matrix)
        l_rows = len(matrix)
        nums = []
        for col in range(max_len):
            digits = [matrix[row][col] for row in range(l_rows) if matrix[row][col] != ' ']
            nums.append(int("".join(digits)))

        if c[-1] == "+":
            res += sum(nums)
            print(sum(nums), nums)
        else:
            res += math.prod(nums)
            print(math.prod(nums), nums)
    return res


    # return res
if __name__ == '__main__':
    print(solve())