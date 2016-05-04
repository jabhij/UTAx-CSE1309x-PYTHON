"""
Write a function called pattern_sum that receives two single digit positive integers, (k and m) as parameters and calculates and returns
the total sum as: 
k + kk + kkk + .... (the last number in the sequence should have m digits) 
For example, if the two integers are:

(4, 5)
Your function should return the total sum of: 
4 + 44 + 444 + 4444 + 44444 
Notice the last number in this sequence has 5 digits. The return value should be:
49380
"""

# Function Dec.
def pattern_sum(k, m):
    total = 0
    # Getting a range for Pattern
    for i in range(1, m + 1):
        # Logic
        i = (i * str(k))
        total += int(i)
    return total
