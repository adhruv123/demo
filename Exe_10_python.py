#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 12
##PROBLEM STATEMENT:
#  Write a Python code to read an integer n from user and print the following values for each integer from 1 to n:
#    Decimal
#    Octal
#    Hexadecimal (capitalized)
#    Binary
    

# Python Version : 3.7
############################################################################################################

"""

 Sample Input:
        4
    Sample Output:
        1     1     1     1
        2     2     2    10
        3     3     3    11
        4     4     4   100

"""

#################

# Code Here
n=4
for x in range(n+1):
    if x!= 0:
        c=x
        d=oct(c).removeprefix('0o')
        e=hex(c).removeprefix('0x')
        f=bin(c).removeprefix('0b')
        print(f"{c} {d} {e} {f}")

#################

