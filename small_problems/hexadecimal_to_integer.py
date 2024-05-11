def hexadecimal_to_integer(string):
    hex_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    lowered_string = string.lower()

    result = 0

    for digit in string:
        result = 16 * result + hex_map[digit.upper()]

    return result


print(hexadecimal_to_integer("4D9f") == 19871)  # True
