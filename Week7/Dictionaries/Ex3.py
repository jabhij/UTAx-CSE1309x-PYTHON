"""
Write a function that accepts a dictionary as input which contains the names and grades of students (The keys are student names and the 
values are lists of grades for 3 exams (1 Dimensional list)) and returns the list of names for those students whose grade on all three 
exams is greater than or equal to 78.

"""

# Function Dec.
def get_grades(dict):
    new_list = []
    get_keys = dict.keys()
    for key in get_keys:
        lists = dict[key]
        grade1, grade2, grade3 = lists[0], lists[1], lists[3]
        if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
            new_list.append(key)
    return new_list
