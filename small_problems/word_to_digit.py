# Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.


def word_to_digit(message):
    digit_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    word_list = message.split(" ")
    word_with_digit_list = []
    for word in word_list:
        if word in digit_map:
            word_with_digit_list.append(digit_map[word])
        else:
            word_with_digit_list.append(word)

    return " ".join(word_with_digit_list)


message = "Please call me at five five five one two three four"
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
