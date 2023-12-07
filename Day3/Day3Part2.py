import re

lines = open("data.txt", "r").read().splitlines()

shifts = [
    (-1, -1), (-1, 0), (-1, 1),  # prev row
    (0, -1), (0, 1),  # current row
    (1, -1), (1, 0), (1, 1),  # next row
]

value = 0


def remove_nodes_if_its_same_number(neighbours_digits):
    neighbours_dict = {}
    for pos, (node, _) in enumerate(neighbours_digits):
        row, col = node
        if row in neighbours_dict:
            neighbours_dict[row].append(col)
        else:
            neighbours_dict[row] = [col]

    for key, values in neighbours_dict.items():
        updated_list = []
        for value in values:
            if value - 1 in updated_list:
                updated_list.remove(value - 1)
            updated_list.append(value)
        neighbours_dict[key] = updated_list

    nodes = [(x, y) for x in neighbours_dict.keys() for y in neighbours_dict[x]]

    return nodes

def find_numbers_from_nodes_positions(nodes):
    nums = []
    for node in nodes:
        row, col = node
        line = lines[row]
        for match in re.finditer(r'\d+', line):
            if match.start() <= col <= match.end():
                nums.append(int(line[match.start():match.end()]))

    return nums


for line_index, line in enumerate(lines):
    for match in re.finditer(r'\*', line):
        nodes = list(map(lambda x: (line_index, x), range(match.start(), match.end())))
        possible_neighbours = [(node[0] + shift[0], node[1] + shift[1]) for node in nodes for shift in shifts]
        possible_neighbours = list(
            filter(lambda x: x[0] >= 0 and x[0] < len(lines) and x[1] >= 0 and x[1] < len(line), possible_neighbours)
        )
        neighbours_signs = list(map(lambda x: ((x[0], x[1]), lines[x[0]][x[1]]), possible_neighbours))
        neighbours_digits = list(filter(lambda x: x[1].isdigit(), neighbours_signs))
        updated_nodes = remove_nodes_if_its_same_number(neighbours_digits)
        numbers = find_numbers_from_nodes_positions(updated_nodes)

        if len(numbers) == 2:
            value = value + numbers[0] * numbers[1]

print(value)

