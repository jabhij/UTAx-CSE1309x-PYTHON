"""
Write a function named count_consonants that receives a string as parameter and returns the total count of the consonants in the string.
Consonants are all the characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'. If the same consonant repeats multiple times
you should count all of them. Note that capitalization and punctuation does not matter here i.e. a lower case character should be considered 
the same as an upper case character.

"""

# Function Dec.
def count_consonants(str):
    # Converting in uppercase and removing spaces
    str_list = str.upper().replace(' ', '')
    L = ['A', 'E', 'I', 'O', 'U']
    count = 0
    # Accessing chars of string
    for i in str_list:
        # Logic
        if i not in L:
            count += 1
    return count
