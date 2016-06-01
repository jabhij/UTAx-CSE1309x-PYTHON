"""
Write a function that takes an integer as input argument and returns the integer using words. For example if the input is 4721 then the 
function should return the string "four seven two one". Note that there should be only one space between the words and they should be all 
lowercased in the string that you return.
"""

# Function Dec.
def num_to_word(get_int):
    # Integer to String
    get_string = str(get_int)
    # String to List
    get_list = list(get_string)
    dict = {'0': 'zero', '1': 'one', '2': 'two',
            '3': 'three', '4' : 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight',
            '9': 'nine'
           }
    output_str = ' '
    # Iterating through list
    for integer in get_list:
        # Output String
        output_str += dict[integer] + ' '
    return output_str
