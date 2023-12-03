def read_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines
