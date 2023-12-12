def find_gears_ratio_sum(lines: list[str]) -> int:
    sum = 0
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == '*':
                # potential gear.
                ns = find_adjacent_numbers(i, j, lines)
                if len(ns) == 2:
                    sum += ns[0] * ns[1]
    return sum


def find_adjacent_numbers(lin: int, col: int, lines: list[str]) -> list[int]:
    adjs = []
    positions = set()
    for i in range(max(lin - 1, 0), lin + 2):
        for j in range(max(col - 1, 0), col + 2):
            try:
                ch = lines[i][j]
                if ch.isdigit():
                    n, index_start, index_end = find_number(i, j, lines)
                    if (index_start, index_end, i) not in positions: # do not add a number twice.
                        adjs.append(n)
                        positions.add((index_start, index_end, i))
            except: # out of bounds
                pass
    return adjs


def find_number(lin: int, col: int, lines: list[str]) -> tuple[int, int, int]:
    index_start = col
    j = index_start
    while True: # walk backwards to find where the number starts.
        j -= 1
        if j < 0:
            index_start = 0
            break
        if not lines[lin][j].isdigit():
            index_start = j + 1
            break
    
    index_end = -1
    j = index_start
    while True: # walk forwards to find where the number ends.
        j += 1
        if j == len(lines[lin]):
            index_end = len(lines[lin]) - 1
            break
        if not lines[lin][j].isdigit():
            index_end = j - 1
            break

    number = int(lines[lin][index_start:index_end + 1])
    return number, index_start, index_end

with open("input_3.txt") as f:
    matrix = [l.strip() for l in f.readlines()]
    print(find_gears_ratio_sum(matrix))
