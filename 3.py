def adjacent_to_symbol(lin: int, col: int, lines: list[str]) -> bool:
    for i in range(max(lin - 1, 0), lin + 2):
        for j in range(max(col - 1, 0), col + 2):
            try:
                adj = lines[i][j]
                if not adj.isdigit() and adj != ".":
                    print(f"Position {i, j} is a symbol adjacent to {lin, col}")
                    return True
            except: # out of bounds
                pass
    return False

def number_adjacent_to_symbol(x_start: int, x_end: int, line: int, lines: list[str]) -> bool:
    for i in range(x_start, x_end + 1):
        if adjacent_to_symbol(line, i, lines):
            return True
    return False

with open("input_3.txt") as f:
    matrix = [l.strip() for l in f.readlines()]
    sum = 0
    for i, line in enumerate(matrix):
        digits = []
        for j, c in enumerate(line):
            if c.isdigit():
                digits.append(c)

            if not c.isdigit() or j == len(line) - 1:
                if len(digits):
                    # number parsed.
                    number = int(''.join(digits))
                    
                    number_start_index = j - len(digits)
                    number_end_index = j - 1
                    digits = []
                    if number_adjacent_to_symbol(number_start_index, number_end_index, i, matrix):
                        sum += number
                else:
                    digits = []

print(sum)



