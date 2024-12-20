#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 7
##PROBLEM STATEMENT:
#   Find the Percentage

# Python Version : 3.7
############################################################################################################

"""
name_keys : [Values are set of marks]
Example: 
    Raj : [80,77,49]
    Yash : [60,67,69]
    Rohit : [30,67,89]

query_name = Key i.e "Rohit"
Average score for query_name = (30+67+89)/3 = 62.0

Input Constraints : 
The first line contains the integer n , the number of students' records. 
The next n lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.
       
        2 <= n <= 10
    # marks[i] = List of marks
        0 <= marks[i] <= 100
    # Length of marks array = 3

Required Output Format : 
    Print one line: The average of the marks obtained by the particular student correct to 2 decimal place.

"""


if __name__ == '__main__':
    # Step 1: Read number of students
    n = int(input())
    
    # Step 2: Initialize a dictionary to store student marks
    student_marks = {}
    
    # Step 3: Input student records (name and marks)
    for _ in range(n):
        # Read the student's data (name and marks)
        name, marks = input().split()
        # Convert marks to integers and store in dictionary
        student_marks[name] = list(map(int, marks))
    
    # Step 4: Read the query_name to find the student's average marks
    query_name = input()
    
    # Step 5: Calculate the average marks for query_name
    if query_name in student_marks:
        marks = student_marks[query_name]
        average = sum(marks) / len(marks)
        # Print the average rounded to 2 decimal places
        print(f"{average:.2f}")

            
            
            


   

        


