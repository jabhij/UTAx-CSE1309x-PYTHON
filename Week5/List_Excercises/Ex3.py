"""
Write a function that accepts a list of integers and returns a new list which is the sorted version (ascending order) of the original list
(Original list should not be modified). You may NOT use the built in sort() or sorted() functions. Notice that the original list should not
be modified
"""

# Function Dec.
def sorting (L1):
    L = L1
    for i in range(len(L)):
        # Next Value from the list
        # For comp.
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L
