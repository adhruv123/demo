#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 21
##PROBLEM STATEMENT:
#   Write a Python code to remove repetitive items from a list using for loop.

# Python Version : 3.7
############################################################################################################



#################

# Code Here
list1=["dhruv","antala","dhruv"]
list2=[]
for x in list1:
    if x  not in list2:
       list2.append(x)
print(list2)  
#################

