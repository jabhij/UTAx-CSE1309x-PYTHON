"""
Write a function that accepts a string of words separated by spaces consisting of alphabetic characters and returns a string such that 
each word in the input string is reversed while the order of the words in the input string is preserved. The length of the input string
must be equal to the length of the output string i.e. there should be no extra trailing or leading spaces in your output string.
For example if:

input_string   = “this is a sample test”
then the function should return a string such as:
"siht si a elpmas tset"

"""

# Function Dec.
def change_str(L):
    # Splitting the string
    split_list = L.split()
    updated_str = ''
    # Accessing every element and
    # Reversing it
    for i in range(0, len(split_list)):
        split_list[i] = split_list[i][::-1]
    # Accessing every element and 
    # adding it to a new string with whitespaces
    for j in range(0, len(split_list)):
        updated_str += split_list[j]+' '
    return updated_str
    
