"""
Write a function that accepts an alphabetic string and returns an integer which is the sum of all the UTF-8 codes of the character in that
string. For example if the input string is "hello" then your function should return 532
"""

# Function Dec.
def alpha(string):
    int_val = 0
    # Accessing all characters of a string
    for i in string:
        # Adding their values
        int_val += ord(i)
    return int_val
