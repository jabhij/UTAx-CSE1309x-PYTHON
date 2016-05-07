"""
Write a function which accepts an input string and returns a reverse of the input string while the case for every single character is 
reversed. The input string for this function would be a sentence (words separated by spaces) consisting of alphabetic characters. 
For example if:
input_string = "Hello Python World"
then the function should return a string such as:
"DLROw NOHTYp OLLEh"

"""

# Function Dec.
def change_str(string):
    updated_str = ''
    start = -1
    # Iterating through string
    while start > -(len(string)+1):
        # Reversing and Swapping the case
        updated_str += string[start].swapcase()
        start -= 1
    return updated_str
