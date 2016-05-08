"""
Write a function named find_mismatch that accepts two strings as input arguments and returns:
0 if the two strings match exactly.
1 if the two strings have the same length and mismatch in only one character.
2 if the two strings do not have the same length or mismatch in two or more characters.

Capital letters are considered the same as lower case letters. Here are some examples:

First string	   Second String  	Function return
Python	         Java	               2
Hello There      helloothere	       1
sin              sink           	2 (note not the same length)
dog	          Dog	               0

"""

# Function Dec.
def find_mismatch(str1, str2):
    # Changing the case
    str1 = str1.upper()
    str2 = str2.upper()
    # If strings aren't of same length
    if len(str1) != len(str2):
        return 2

    count = 0
    # Accessing chars of string 1
    for i in range(len(str1)):
        # Comparing strings and counting mismatch
        if str1[i] != str2[i]:
            count += 1
            # Case1
            if count > 1:
                return 2
            # Case2
            elif (count < 2) and (len(str1) == len(str2)):
                return 1
            # Case3
            elif (count == 0) and (len(str1) == len(str2)):
                return 0
                
                
