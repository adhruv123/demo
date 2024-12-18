#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 18
##PROBLEM STATEMENT:
#   Python code to demonstrate the exception handling. Make sure your code print the detailed exception traceback 
#   and also write all the exception occured to a specific file.
# Python Version : 3.7
############################################################################################################




#################

import traceback

# Define the log file to write exceptions
log_file = "exceptions.log"

def write_exception_to_file(exception):
    """Write exception traceback to the log file."""
    with open(log_file, "a") as file:
        file.write("Exception occurred:\n")
        file.write(traceback.format_exc())
        # file.write("\n" + "=" * 50 + "\n")  # Separator for readability

try:
    # Example: Division by zero
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    # Print detailed exception traceback to the console
    print("An exception occurred:")
    traceback.print_exc()

    # Write the exception details to the log file
    write_exception_to_file(e)

print(f"Exception has been logged to '{log_file}'.")


#################
