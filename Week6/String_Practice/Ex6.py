"""
Write a function which returns the number of words in the input string which have more than 4 characters. Assume that the input string 
consists of alphabetic characters separated by spaces and capitalization does not matter i.e. an upper case character should be treated 
the same as a lower case character.

"""

# Function Dec.
def count_words(string):
    count = 0
    # Converting string in upper case
    # and splitting every word in string
    new_string = string.upper().split()
    # Accessing all the words
    for i in new_string:
        # Checking the length
        if len(i) > 4:
            count += 1
    return count
