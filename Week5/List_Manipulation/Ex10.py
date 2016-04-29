"""
Write a function that accepts a positive integer k and returns the ascending sorted list of cube root values of all the numbers from 1 to k
(including 1 and not including k). [if k is 1, your program should return an empty list]
"""

# Function Decl.
def cube_root(k):
    # An empty list
    L = []
    # Accessing range 
    for i in range(1, k):
        # Logic 
        val = i**(1/3)
        L.append(val)
    return L
