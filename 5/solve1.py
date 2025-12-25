def solve(): 
    with open("puzzle.txt") as f:
        lines = f.readlines()
    
    parsed = list(map(lambda x: x.replace("\n", ""), lines))
    ids, ranges = [], []
    flag = True

    for line in parsed:
        if line == "":
            flag = False
            continue

        if flag:
            ranges.append(line)
        else:
            ids.append(line)

    ranges = [list(map(int, r.split("-"))) for r in ranges]
    ids = [int(id) for id in ids]
    res = 0

    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                res += 1    
                break
    
    return res
    

if __name__ == '__main__':
    print(solve())