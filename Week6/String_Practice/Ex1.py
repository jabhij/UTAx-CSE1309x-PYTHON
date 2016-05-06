"""
Write a function that takes a string consisting of alphabetic characters as input argument and returns True if the string is a palindrome.
A palindrome is a string which is the same backward or forward. Note that capitalization does not matter here i.e. a lower case character 
can be considered the same as an upper case character.
"""

# Function Dec.
def palindrome_str(string):
    # Reading string from both forward and
    # backward and checking if it's equal
    if str(string).lower() == str(string)[::-1].lower():
        return True
    else:
        return False
