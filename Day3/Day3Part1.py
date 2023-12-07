import re

lines = open("data.txt", "r").read().splitlines()

shifts = [
    (-1, -1), (-1, 0), (-1, 1),  # prev row
    (0, -1), (0, 1),  # current row
    (1, -1), (1, 0), (1, 1),  # next row
]

value = 0

for line_index, line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
        nodes = list(map(lambda x: (line_index, x), range(match.start(), match.end())))
        possible_neighbours = [(node[0] + shift[0], node[1] + shift[1]) for node in nodes for shift in shifts]
        possible_neighbours = list(
            filter(lambda x: x[0] >= 0 and x[0] < len(lines) and x[1] >= 0 and x[1] < len(line), possible_neighbours)
        )
        neighbours_signs = list(map(lambda x: lines[x[0]][x[1]] ,possible_neighbours))
        neighbours_symbols = list(filter(lambda x: not x.isdigit() and not x == ".", neighbours_signs))
        if len(neighbours_symbols) > 0:
            value = value + int(match.group())

print(value)
