"""
Write a function that accepts a list as input and returns a new list which includes every other element in the original list. Keep the first element, i.e. input_list[0]. For example if:

input_list = ["we", "love", "python", "so","much"]
then your function should return a list such as:
['we', 'python', 'much']
"""

# Function Dec.
def get_alternate(L):
    # An Empty list
    new_list = []
    # Accessing range
    for i in range(0, len(L), 2):
        new_list.append(L[i])
    return new_list
