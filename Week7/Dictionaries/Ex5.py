"""
Write a function that takes a string as input argument and returns a dictionary of letter counts i.e. the keys of this dictionary should 
be individual letters and the values should be the total count of those letters. You should ignore white spaces and they should not be 
counted as a character. Also note that a small letter character is equal to a capital letter character.

"""

# Function Dec.
def letter_count(string):
    dict = {}
    # Removing whitespaces and converting in uppercase
    string = string.replace(' ', '')
    string.upper()
    # Iterating through the string
    for char in string:
        dict[char] = string.count(char)
    return dict 
