# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.


def string_to_integer(string):
    int_map = {
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
    }

    digits_list = []

    for digit in string:
        digits_list.append(int_map[digit])

    result = 0

    # digits_list = [4, 3, 2, 1]
    # digits_list = [5, 7, 0]

    for digit in digits_list:

        result = 10 * result + digit
        # result = 0 * 10 + 4 = 4
        # result = 4 * 10 + 3 = 43
        # result = 43 * 10 + 2 = 432
        # result = 432 * 10 + 1 = 4321

        # result = 0 * 10 + 5 = 5
        # result = 5 * 10 + 7 = 57
        # result = 57 * 10 + 0 = 570

    return result


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)  # True
