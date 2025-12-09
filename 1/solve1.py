
def solve():
    with open("puzzle.txt") as f:
        lines = f.readlines()
    parsed = list(map(lambda c1: -int(c1[1:]) if c1[0] == "L" else int(c1[1:]), map(lambda c2: c2.replace("\n", ""), lines)))
    res = 0 ; start = 50
    for n in parsed:
        start += (n % 100)
        start = start % 100 if start > 99 else start
        res += 1 if start == 0 else 0
    return res

if __name__ == '__main__':
    print(solve())
        
