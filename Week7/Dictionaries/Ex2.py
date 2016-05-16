"""
Write a function that accepts a dictionary as input and returns a sorted list of all the values in the dictionary. Assume that the values 
of this dictionary are just integers.

"""

# Function Dec.
def dictionary_sort(Dict):
    # Generating Dictionary View
    get_values = Dict.values()
    # Changing Dictionary to List View
    get_values = list(get_values)
    # Sorting
    get_values.sort()
    return get_values
