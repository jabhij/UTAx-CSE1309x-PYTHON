"""
Write a function named find_longest_word that receives a string as parameter and returns the longest word in the string. Assume that the 
input to this function is a string of words consisting of alphabetic characters that are separated by space(s). In case of a tie between 
some words return the last one that occurs

"""

# Function Dec.
def find_longest_word(str):
    # Splitting string into list
    str = str.split()
    # Getting first element 
    # Assigning it as max length word
    max_length = str[0]
    longest_word = len(str[0])
    # Accessing all the words in List
    for word in str:
        # Logic
        if len(word) >= longest_word:
            max_length = word
    return max_length
