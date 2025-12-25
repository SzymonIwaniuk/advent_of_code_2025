def solve(): 
    with open("puzzle.txt") as f:
        lines = f.readlines()
    
    parsed = list(map(lambda x: x.replace("\n", ""), lines))
    ranges = []

    for line in parsed:
        if line == "":
            break
        ranges.append(line)

    ranges = [list(map(int, r.split("-"))) for r in ranges]
    ranges.sort()
    cur_start, cur_end = ranges[0]
    sets = []

    for start, end in ranges[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            sets.append([cur_start, cur_end])
            cur_start, cur_end = start, end

    sets.append([cur_start, cur_end])
    res = sum(end - start + 1 for start, end in sets)

    return res 


if __name__ == '__main__':
    print(solve())