"""
Write a function named test_for_anagrams that receives two strings as parameters, both of which consist of alphabetic characters and 
returns True if the two strings are anagrams, False otherwise. Two strings are anagrams if one string can be constructed by rearranging 
the characters in the other string using all the characters in the original string exactly once. For example, the strings "Orchestra" 
and "Carthorse" are anagrams because each one can be constructed by rearranging the characters in the other one using all the characters
in one of them exactly once. Note that capitalization does not matter here i.e. a lower case character can be considered the same as an 
upper case character.

"""

# Function Dec.
def test_for_anagrams(str1, str2):
    # String Comparision
    if sorted(str1.upper()) == sorted(str2.upper()):
        return True
    return False
