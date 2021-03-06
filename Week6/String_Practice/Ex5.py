"""
Write a function that accepts a string and a character as input and returns the count of all the words in the string which start with the
given character. Assume that capitalization does not matter here. You can assume that the input string is a sentence i.e. words are
separated by spaces and consists of alphabetic characters.

"""

# Function Dec.
def count_char(string, char):
    new_string = string.upper().split()
    count = 0
    # Accessing all chars in the string
    for i in new_string:
        # Checking the first word 
        if i[0] == char.upper():
            count += 1
    return count
