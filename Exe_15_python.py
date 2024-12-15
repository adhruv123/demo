#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 15
##PROBLEM STATEMENT:
#   Write a Python code to check whether a given key already exists in a dictionary.

# Python Version : 3.7
############################################################################################################



#################

# Code Here
dict1={'k1':'k5','k6':'k7'}
key=input()
for key1,value in dict1.items():
    if key1 == key:
        print("key is existed")
        break
    else:
        print("key is not existed")
        break

#################

