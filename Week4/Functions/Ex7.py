# Function Definition
def get_max(new_list):
    maximum = new_list[0]
    # For Loop and Logic
    for val in new_list:
        if val > maximum:
            maximum = val
    return maximum
