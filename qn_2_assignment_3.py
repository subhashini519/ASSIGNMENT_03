# Write a Python program to reverse a string.
# ﻿Sample String : "1234abcd"
# Expected Output : "dcba4321"

def str_rev(string):

    rev_str = string[::-1]
    print(f"The original string is {string}")
    print(f"The reversed string is {rev_str}")

string = input("Enter any string to reverse:")
str_rev(string)


