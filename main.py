#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created June 2022
# This program formats text using a list


def string_formatter(whole_string):
    # takes the users string and formats it

    formatted_string = []
    largest_word = 0
    header_footer = ""

    # find the largest word to set the width of the format
    for large_word_check in whole_string:
        if len(large_word_check) > largest_word:
            largest_word = len(large_word_check)
    for counter in range(4 + largest_word):
        header_footer += "*"

    # create the final formatted string, word by word
    formatted_string.append(header_footer)
    for single_word in whole_string:
        while len(single_word) < largest_word:
            single_word += " "
        formatted_word = "* {} *".format(single_word)
        formatted_string.append(formatted_word)
    formatted_string.append(header_footer)

    return formatted_string


def main():
    # Gets strings from the user, calls a function to format them,
    # and then outputs them back to the user

    whole_string = []

    print("This program takes your input and formats it to look cool.")
    print("Enter -1 to format the strings you entered.\n")

    # input
    while True:
        temp_string = input("Enter a line to be formatted: ")
        if temp_string != "-1":
            whole_string.append(temp_string)
        else:
            print("")
            break

    # call function
    formatted_string = string_formatter(whole_string)

    # output
    for word in formatted_string:
        print(word)
    print("\nDone.")


if __name__ == "__main__":
    main()

