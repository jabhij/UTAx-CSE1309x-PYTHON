"""
Write a function called find_integer_with_most_divisors that accepts a list of integers and returns the integer from the list that has the
most divisors. In case of a tie, return the first item that has the most divisors. For example: 

if the list is:

 [8, 12, 18, 6]
In this list, 8 has four divisors which are: [1,2,4,8] ; 12 has six divisors which are: [1,2,3,4,6,12]; 18 has six divisors which 
are: [1,2,3,6,9,18] ; and 6 has four divisors which are: [1,2,3,6]. Notice that both 12 and 18 are tied for maximum number of divisors 
(both have 6 divisors). Your function should return the first item with maximum numer of divisors; so it should return:
 12
 """
 
 # Function Dec.
def get_divisors(L):
    # Empty List / Divisors
    new_list = []
    div_length = 0
    max_divisors = None
    # Accessing Elements
    for i in L:
        # Getting all Divisors 
        for j in range(1, i):
            if i % j == 0:
                new_list.append(i)
        length = len(new_list)
        # Getting Lengths of Divisors
        if length > div_length:
            div_length = length
            max_divisors = i
    return max_divisors
