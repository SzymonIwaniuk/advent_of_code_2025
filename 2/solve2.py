def solve():
    with open("puzzle.txt") as f:
        lines = f.read()
    parsed = list(map(lambda y: (int(y[0]), int(y[1])), map(lambda x: x.split("-"), lines.split(","))))
    res = 0
    for a, b in parsed:
        for n in range(a, b+1):
            num = str(n)
            l = len(num)
            for i in range(1,l//2 + 1):
                if num[:i] * (l//i) == num:
                    res += n
                    break

    return res

if __name__ == '__main__':
    print(solve())