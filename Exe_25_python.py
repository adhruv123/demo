#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 25
##PROBLEM STATEMENT:
#   Provide two different solution for below problem:
#    Make sure code work on both the windows and linux systems.
# Python Version : 3.7
############################################################################################################


"""

 Python code to list all the files in current directory with all detailed information i.e. permission, owner, file created and etc. like we have output for ls -l
    - After that convert all the python files in the existing directory to the text files in the same location
    - After updating python files, Move all the python files to some specific folder/ location
    - Make sure your code output must have intuitive logs for the users

NOTE: Use OS module for performing various operations.

"""


#################

# Code Here
# import os
# import shutil

# # Define the target folder to move renamed Python files
# target_folder = "files3/"

# # Create the target folder if it doesn't exist
# if not os.path.exists(target_folder):
#     os.makedirs(target_folder)
#     print(f"[INFO] Created target folder: {target_folder}")

# # Get the current working directory
# current_directory = os.getcwd()

# # Initialize counters for user-friendly logs
# files_processed = 0
# files_moved = 0

# print("[INFO] Starting to process files...")

# # Iterate over all files in the current directory
# for filename in os.listdir(current_directory):
#     # Check if the file ends with .py
#     if filename.endswith(".py"):
#         # Construct the new filename by replacing .py with .txt
#         new_filename = filename[:-3] + ".txt"
#         old_path = os.path.join(current_directory, filename)
#         new_path = os.path.join(current_directory, new_filename)
        
#         # Rename the file
#         os.rename(old_path, new_path)
#         print(f"[RENAME] {filename} -> {new_filename}")
#         files_processed += 1
        
#         # Move the renamed file to the target folder
#         shutil.move(new_path, os.path.join(target_folder, new_filename))
#         print(f"[MOVE] {new_filename} -> {target_folder}")
#         files_moved += 1

# # Summary of the process
# print("\n[INFO] Process completed!")
# print(f"Total files processed: {files_processed}")
# print(f"Total files moved: {files_moved}")


#################
