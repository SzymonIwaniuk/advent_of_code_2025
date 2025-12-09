def solve():
    with open("puzzle.txt") as f:
        lines = f.readlines()
    parsed = list(map(lambda y: list(y), map(lambda x: x[:-1], lines)))
    res = 0
    for line in parsed:
        maxi = 0
        l = len(line)
        for i in range(l - 1):
            for j in range(i + 1, l):
                maxi = max(maxi, int(line[i] + line[j]))
        res += maxi

    return res

if __name__ == '__main__':
    print(solve())