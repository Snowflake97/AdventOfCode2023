from CommonTools.DataReader import read_from_file

def get_digits(code):
    output = ""
    for s in code:
        if s.isdigit():
            output = output + s
    output = output[0] + output[-1]
    return int(output)


def get_value(codes):
    value = 0 
    for code in codes:
        value = value + get_digits(code)
    return value

print(get_value(read_from_file("data.txt")))
