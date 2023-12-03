from CommonTools.DataReader import read_from_file

import re

digits_to_value_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def get_number_from_code(code):
    digit_positions_dict = {}
    for string_digit in digits_to_value_dict.keys():
        if string_digit in code:
            for i in re.finditer(string_digit, code):
                position = i.start()
                digit_positions_dict[position] = digits_to_value_dict[string_digit]
    first = digit_positions_dict[min(digit_positions_dict.keys())]
    last = digit_positions_dict[max(digit_positions_dict.keys())]
    return str(first) + str(last)


def get_value(codes):
    value = 0
    for pos, code in enumerate(codes):
        single_code_value = int(get_number_from_code(code))
        print("{}. - {} - {}".format(pos + 1, code.strip(), single_code_value))
        value = value + int(single_code_value)
    return value


example_codes = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

example_codes = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
    "eightwo",
    "twone",
    "eightwo",
    "eighthree",
    "fiveight",
    "threethreetwothree"
]

print(get_value(read_from_file("data.txt")))
print(get_value(example_codes))
