"""
Write a function that will receive a 2D list of integers. The function should return the count of how many rows of the list have even sums
and the count of how many rows have odd sums. 
For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].

"""

# Function Dec.
def get_rows_count(L):
    new_list = []
    # Iterating through Lists
    for i in L:
        new_list.append(sum(i))
        even_count = 0
        odd_count = 0
        # Checking Even-Odd
        for j in new_list:
            if j % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return [even_count, odd_count]
