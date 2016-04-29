"""
Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k. The multiples should be
calculated starting from 1 to 5 (including both 1 and 5). For example the first five multiples of 3 are 3, 6, 9, 12, and 15
"""

# Function Dec.
def get_multiples(K):
    # A blank list
    L = []
    # Accessing the range
    for i in range(1, 6):
        # Logic and adding multiples
        # in the list L
        multiple = (K * i)
        L.append(multiple)
    return L
