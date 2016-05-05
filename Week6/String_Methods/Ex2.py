"""
Write a function that accepts an input string consisting of alphabetic characters and removes all the trailing whitespace of the string 
and returns it without using any .strip() method. For example if:

input_string = "  Hello       "
then your function should return an output string such as:
output_string = "  Hello"

"""

# Function Dec.
def remove_ws(string):
    # Setting an Index
    get_index = None
    # Accessing all characters in string
    # Looking for whitespaces
    for i in range(-1, -len(string)):
        if string[i] != ' ':
            # Index for slicing
            get_index = i
            break
    # Applying list slicing
    new_string = string[::get_index]
    return len(new_string)
