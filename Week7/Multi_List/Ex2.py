"""
Write a function that accepts a 2 Dimensional list of integers and returns the average. 
Remember that average = (sum_of_all_items) / (total_number_of_items).

"""

# Function Dec.
def avg_list(L):
    total_sum = 0
    # Accessing every row
    for row in range(len(L)):
        # Accessing every column
        for col in range(len(L[0])):
            # Sum and avg
            total_sum += L[row][col]
            avg = total_sum/(len(L)+len(L[0]))
    return int(avg)
