"""
(30 points possible)
Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the first string can become the same as the second string by inserting or deleting a single character. Notice that inserting and 
deleting a character is not the same as replacing a character.
2 otherwise

Capital letters are considered the same as lower case letters. Here are some examples:

First string	  Second String	  Function return
Python	         Java             2
book           	boot	          2
sin	        sink            1 (Inserting a single character at the end)
dog	        Dog	            0
poke      	spoke           1 (Inserting a single character at the start)
poker     	poke	         1 (Deleting a single character from the end)
programing	programming	  1 (Inserting a single character)

"""

