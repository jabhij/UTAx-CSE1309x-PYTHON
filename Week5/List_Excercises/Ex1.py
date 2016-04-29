"""
Write a function that accepts a list (which has a length of 4 or more) and a string and returns the list such that the second through the 
fourth element (index 1 through 3 both inclusive) in the input list are replaced by the input string. For example:

input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
input_string = "Brahman" 
Then, your function should return a list such as:
['Isha', 'Brahman', 'Brahman', 'Brahman', 'Sri']
"""

# Updating a List
# Function Dec.
def update_list(L, string):
    # Accessing range & Logic
    for i in range(1, 4):
        L[i] = string
    return L
