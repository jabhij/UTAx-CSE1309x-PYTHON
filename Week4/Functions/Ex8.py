# Function Definition
def get_min(new_list):
    minimum = new_list[0]
    # For Loop and Logic
    for val in new_list:
        if val < minimum:
            minimum = val
    return minimum
