"""
Write a function that accepts a positive integer k and returns the list of all the divisors of k. Your list should include both 1 and k.
"""

# Function Dec.
def get_divisors(k):
    # An Empty list
    L = []
    # Accessing range
    for i in range(1, k):
        # Logic
        if k % i == 0:
            L.append(i)
    return L
