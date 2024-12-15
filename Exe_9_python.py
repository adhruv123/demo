#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 11
##PROBLEM STATEMENT:
#  Write a Python code to convert a given string to a tuple. Do not include spaces or tabs in the tuple.
# NOTE : Tuple wil contain each character from "string_given".
# Python Version : 3.7
############################################################################################################

a = 'Hello,this is your Program      . I am  Program'

#################

# Code Here

e=tuple(''.join(a.split())) #split uses spliting a string and  join uses to concate string where '' it present
print(e)

#################

