"""
Write a function which returns the total number of vowels in an input string which consists of alphabetic characters. Note that 
capitalization does not matter here i.e. a lower case character should be considered the same as an upper case character. For this 
problem, the vowels are considered to be A, E, I, O, U.
"""

# Function Dec.
def vowel_count(string):
  new_string = string.upper()
  count = 0
  vowels = ['A', 'E', 'I', 'O', 'U']
  # Accessing all chars in the string
  for char in new_string:
      # Checking if the chars are in the list
      if char in vowels:
      count += 1
  return count
