"""
Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.

"""

# Function Dec.
def dictionary_sort(Dict):
    # Generating Dictionary View
    get_keys = Dict.keys()
    # Changing Dictionary to List View
    get_keys = list(get_keys)
    # Sorting
    get_keys.sort()
    return get_keys
