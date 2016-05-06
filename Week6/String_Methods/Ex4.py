"""
Write a function which accepts an input string consisting of alphabetic characters and spaces and returns the string with all the spaces 
removed. Do NOT use any string methods for this problem.
"""

# Function Dec.
def remove_ws(string):
    new_string = ' '
    # Accessing all the characters in string
    for i in range(1, len(string)):
        # Selecting only* character
        # Rejecting whitespaces
        if string[i] != ' ':
            # Adding characters to a new string
            new_string += string[i]
    return new_string
