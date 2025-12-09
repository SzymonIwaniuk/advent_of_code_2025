# garek brute force
def check(x, y, n, m, grid):
    cnt = 0
    for i in range(max(y - 1, 0), min(y + 2, n)):
        for j in range(max(x - 1, 0), min(x + 2, m)):
            if (i, j) != (y, x) and grid[i][j] == "@":
                cnt += 1
            # print(cnt, grid[i][j], i, j)
            if cnt > 3:
                return False
    return True


def solve():
    with open("puzzle.txt") as f:
        lines = f.readlines()
    parsed = list(map(lambda x: x.replace("\n", ""), lines))
    n, m = len(parsed), len(parsed[0])
    res = 0
    
    for y in range(n):
        for x in range(m):
            if parsed[y][x] == "@" and check(x, y, n, m, parsed):
                res += 1
    return res

if __name__ == '__main__':
    print(solve())