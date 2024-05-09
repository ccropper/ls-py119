# Write a function that takes a string argument consisting of a first name, a space, and a last name, and returns a new string consisting of the last name, a comma, a space, and the first name.


def swap_name(name):
    name_list = name.split(" ")
    return ", ".join(reversed(name_list))


print(swap_name("Joe Roberts"))  # "Roberts, Joe"


# What if the person has one or more middle names? Refactor the current solution so that it can accommodate this; the middle names should be listed after the first name:


def swap_name(name):
    name_list = name.split(" ")
    swapped_name = ""
    swapped_name += name_list[-1]
    swapped_name += ", "
    swapped_name += " ".join(name_list[:-1])
    return swapped_name


print(swap_name("Karl Oskar Henriksson Ragvals"))  # "Ragvals, Karl Oskar Henriksson"
