def solve():
    with open("test_puzzle.txt") as f:
        lines = f.read()
    parsed = list(map(lambda y: (int(y[0]), int(y[1])), map(lambda x: x.split("-"), lines.split(","))))
    res = 0 
    for a, b in parsed:
        for n in range(a, b+1):
            num = str(n)
            l = len(num)
            if l % 2 == 0:
                if num[:(l//2)] == num[(l//2):]:
                    res += n
    return res

if __name__ == '__main__':
    print(solve())