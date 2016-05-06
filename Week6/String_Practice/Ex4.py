"""
Write a function that accepts a string and a character as input and returns the number of times the character is repeated in the string.
Note that capitalization does not matter here i.e. a lower case character should be treated the same as an upper case character.

"""

# Function Dec.
def count_char(string, char):
    new_string = string.upper()
    count = 0
    # Accessing all chars in the string
    for i in new_string:
        # Checking if char is in string
        if (i == char.upper()):
            count += 1
    return count
