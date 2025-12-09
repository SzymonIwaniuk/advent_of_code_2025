def solve():
    with open("puzzle.txt") as f:
        lines = f.readlines()
    parsed = list(map(lambda c1: -int(c1[1:]) if c1[0] == "L" else int(c1[1:]), map(lambda c2: c2.replace("\n", ""), lines)))
    res = 0 ; start = 50
    for n in parsed:
        k = abs(n)
        first = (100 - (start % 100)) % 100 if n > 0 else start % 100
        first = 100 if first == 0 else first
        res += 1 + (k - first) // 100 if k >= first else 0
        start = (start + n) % 100

    return res

if __name__ == '__main__':
    print(solve())