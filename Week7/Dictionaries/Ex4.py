"""
Write a function which accepts a dictionary and an integer as input and returns an ascending sorted list of all the keys whose values 
contain the input value. Note that the keys of this dictionary are strings while the values of this dictionary are 1 Dimensional lists 
of integers. For example if the input dictionary is:

sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
          
and the input integer is 2 then your function should return:
[ "kitten", "rabbit",]

If the input integer is not found then your function should return an empty list.

"""

# Function Dec.
def value_containing_key(dict, num):
    new_list = []
    # Iterating through the keys
    for key in dict:
        # Checking: if the num is in the dict
        if num in dict[key]:
            new_list.append(key)
            new_list.sort()
    return new_list
