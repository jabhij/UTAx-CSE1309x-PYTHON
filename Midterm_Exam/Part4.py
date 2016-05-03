"""
Write a function named list_of_primes that accepts a positive integer n and returns a sorted list (ascending order) of all the prime numbers
between 2 and n (including 2 but not including n)
"""

# Function Dec.
def list_of_primes(n):
    num = 2
    l = []
    # Accessing values in range
    while num < n:
        prime = True
        start = 2
        # Cheking Divisibility
        while start < num:
            if num % start == 0:
                prime = False
            start += 1
        # Conditon Check
        if prime:
            l.append(num)
        num += 1
    return l
