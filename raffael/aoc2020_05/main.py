import math


def calc_point(line: str, row_begin: int, row_range: int) -> int:
    if len(line) == 0:
        return row_begin
    if line[0] == 'F' or line[0] == 'L':
        return calc_point(line[1:], row_begin, int((row_begin + row_range) / 2))
    if line[0] == 'B' or line[0] == 'R':
        return calc_point(line[1:], int(math.ceil((row_begin + row_range) / 2)), row_range)


def calc_coord(line: str) -> (int, int):
    row = calc_point(''.join([c for c in line if c in ['F', 'B']]), 0, 127)
    col = calc_point(''.join([c for c in line if c in ['R', 'L']]), 0, 7)
    return col, row


def calc_id(coordinate: (int, int)) -> int:
    return (coordinate[1] * 8) + coordinate[0]


with open('aoc2020_05_input.txt', 'r') as f:
    lines = f.read().split('\n')

print(calc_coord('BFFFBBFRRR'), ";", calc_id(calc_coord('BFFFBBFRRR')), "eq (7, 70) ; 567")
print(calc_coord('FFFBBBFRRR'), ";", calc_id(calc_coord('FFFBBBFRRR')), "eq (7, 14) ; 119")
print(calc_coord('BBFFBBFRLL'), ";", calc_id(calc_coord('BBFFBBFRLL')), "eq (4, 102) ; 820")

ids = [calc_id(calc_coord(line)) for line in lines]
print('Part 1: ', max(ids))

possible_ids = [calc_id((x, y)) for x in range(8) for y in range(128)]
print('Part 2: ', [sid for sid in possible_ids if sid not in ids and sid + 1 in ids and sid - 1 in ids][0])

