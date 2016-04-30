"""
Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both list
s sorted in descending order. Your new list should include duplicate elements if they exist. Do NOT use the built in sort() or sorted() 
methods.
"""


# Function Dec.
def get_list(A, B):
    L = (A + B)
    # Accessing range & Logic
    for i in range(len(L)):
        # Next Value from the list
        for j in range(i + 1, len(L)):
            # Swapping
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
    return L
