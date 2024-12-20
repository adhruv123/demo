#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 24
##PROBLEM STATEMENT:
#   Write a Python code to find all pairs from a array whose division is equal to given integer number.
# Python Version : 3.7
############################################################################################################


"""

  List: [[9,3], [20,5], [42, 6, 4.5], [4, 5, 0.58] [78,0], [2,3], [4,6], [0, 0], 0, 16, None]
    NOTE: Individual numbers, "None" value must be taken care of during the code. 
    Only two number's division must match with given input. 
    In case of more than two values in the list. Please take last two values from the list

    Sample Input: 0

    Sample Output: 1. [2,3]
                   2. [4,6]
"""


#################

data = [[9, 3], [20, 5], [42, 6, 4.5], [78, 0], [2, 3], 0, 16, None]
matched_value = 0

result_lists = []

for item in data:
    if isinstance(item, list):
        if len(item) >= 2 and item[1:2] != [0]:
            result = item[0] // item[1]
            if result == matched_value:
                result_lists.append(item)

        if len(item) >= 3 and item[2:3] != [0]:
            result = item[1] / item[2]
            if result == matched_value:
                result_lists.append(item)

print(result_lists)

#################
