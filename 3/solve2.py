def solve():
    with open("puzzle.txt") as f:
        lines = f.readlines()
    parsed = list(map(lambda y: list(y), map(lambda x: x[:-1], lines)))
    res = 0
    for line in parsed:
        l = len(line)
        stack = []
        drop = l - 12
        for i in range(l):
            while drop and stack and stack[-1] < line[i]:
                stack.pop()
                drop -= 1
            stack.append(line[i])
        res += int(''.join(stack[:12]))
        
    return res

if __name__ == '__main__':
    print(solve())