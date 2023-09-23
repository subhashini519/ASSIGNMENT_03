# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# ﻿Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def str_count(string):
    def string_upper(s):
        upper_count = 0
        for char in s:
            if char.isupper():
                upper_count += 1
        return upper_count

    def string_lower(s):
        lower_count = 0
        for char in s:
            if char.islower():
                lower_count += 1
        return lower_count

    upper_count = string_upper(string)
    lower_count = string_lower(string)

    print(f"The No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

string = input("Enter any string: ")
str_count(string)
