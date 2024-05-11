# In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

# You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.


def integer_to_string(int):
    int_map = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }

    # 4321

    digits_list = []
    number = int

    while True:

        # 4321 % 10 = 1
        # 4321 // 10 = 432
        # 432 % 10 = 2
        # 432 // 10 = 43
        # 43 % 10 = 3
        # 43 // 10 = 4
        # 4 % 10 = 4
        # 4 // 10 = 0

        digit = number % 10
        digits_list = [int_map[digit]] + digits_list

        number = number // 10

        if number == 0:
            break

    return "".join(digits_list)


print(integer_to_string(4321) == "4321")  # True
print(integer_to_string(0) == "0")  # True
print(integer_to_string(5000) == "5000")  # True
print(integer_to_string(1234567890) == "1234567890")  # True
