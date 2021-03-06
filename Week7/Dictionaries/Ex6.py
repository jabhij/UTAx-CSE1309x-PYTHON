"""
Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e. the keys of this dictionary should 
be individual vowels and the values should be the total count of those vowels. You should ignore white spaces and they should not be 
counted as a character. Also note that a small letter vowel is equal to a capital letter vowel.

"""
 
def count_vowel(string):
    dict = {}
    string = string.replace(' ', '')
    string.upper()
    vowels = ['A', 'E', 'I', 'O' 'U']
    for char in string:
        if char in vowels:
            dict[char] = string.count(char)
    return dict
