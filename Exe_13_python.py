#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 10
##PROBLEM STATEMENT:
#  Write a Python code to check whether dictionary/List is empty or not.

# Python Version : 3.7
############################################################################################################

dic_1 = {}
dic_2 = {'raj':'[24,56,78]'}
list_1 = []
list_2 = ['1','4','a','#']

#################

input_structure=input("Enter above variable name you want to check whether it is empty or not:")
# Code Here
if  len(input_structure)== 0:
    print(f"{input_structure} is empty")
else:
    print(f"{input_structure} is not empty")


#################

