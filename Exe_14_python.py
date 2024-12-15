#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 14
##PROBLEM STATEMENT:
#    Write a Python code to print the value of given key from the dictionary.

# Python Version : 3.7
############################################################################################################

"""

 Code must need to handle the test case where key can be present at any inner nested dictionary.
    Example:
        input_dict = {"k1": "v1",
             "k2": {"k3": "v3"},
             "k4": {"k5": {"k6": "v6"}}
             }

    Sample Input1: k6
    Sample Output1: v6

    Sample Input2: k1
    Sample Output2: v1

    Sample Input3: k4
    Sample Output3: {"k5": {"k6": "v6"}


"""

#################

# Code Here
def get_value_from_nested_dict(input_dict, target_key):
    """
    Function to retrieve the value of a given key from a nested dictionary using a stack.
    :param input_dict: Dictionary to search in (may be nested).
    :param target_key: Key whose value needs to be retrieved.
    :return: Value associated with the given key if found, else None.
    """
    # Use a stack to handle nested dictionaries
    stack = [input_dict]  # Start with the top-level dictionary

    while stack:
        current_dict = stack.pop()  # Get the last dictionary from the stack

        for key, value in current_dict.items():
            if key == target_key:
                return value
            elif type(value) == dict:
                stack.append(value)  # Add nested dictionary to the stack

    # Return None if the key is not found
    return None

if __name__ == "__main__":
    # Input dictionary
    input_dict = {
        "k1": "v1",
        "k2": {"k3": "v3"},
        "k4": {"k5": {"k6": "v6"}}
    }

    # Take key as input from the user
    target_key = input("Enter the key to search: ")

    # Search for the key and print the output
    result = get_value_from_nested_dict(input_dict, target_key)
    if result is not None:
        print(f"Value for '{target_key}': {result}")
    else:
        print(f"Key '{target_key}' not found.")

        


        
            

#################

