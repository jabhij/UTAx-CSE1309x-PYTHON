"""
Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the second argument is
a list of words (correct_spells). Your function should check each word in the input string against all the words in the correct_spells list
and return a string such that:

If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified and it should be directly
copied to the output string.
if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that
word should be replaced by the correct word in the correct_spelled list.
If neither of the two previous conditions is true, then the word in the original string should not be modified and should be directly copied
to the output string.

Notes:
Do not spell check one or two letter words (copy them directly to the output string).
In case of a tie use the first word from the correct_spelled list.
Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
All characters in the output string should all be in lower case letters.
Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
Remove extra spaces between the words.
Remove spaces at the start and end of the output string.

Examples:


Sentence (str)                   	correct_spells (list)                        	Function return (str)
Thes is the Firs cas             	['that','first','case','car']	                thes is the first case
programing is fan and eesy      	['programming','this','fun','easy','book' ]	  programming is fun and easy
Thes is vary essy	                ['this', 'is', 'very', 'very', 'easy']	      this is very easy
Wee lpve Pythen	                    ['we', 'Live', 'In', 'Python']	              we live python

""""


