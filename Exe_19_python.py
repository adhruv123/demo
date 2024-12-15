#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 19
##PROBLEM STATEMENT:
#   Write a Python function to check whether two given strings are anagram of each other or not. Code must not contain sort or any other sorted inbuilt functions.
#   NOTE: An anagram of a string is another string that contain the same characters in the same frequency, 
#   only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

# Python Version : 3.7
############################################################################################################



#################

# Code Here
def anagram(string1,string2):
    
    count1=0
    count2=0
    for x in string1:
        if x in string2:
            count1+=1
             
        else:
            count1-=1
    
    for y in string2:
        if y in string1:
           count2+=1
           
        else:
            count2-=1
    
    if count1 == count2:
        print("string is anagram")
    else:
        print("string is not anagram")


string1=input("Enter a string1:")
string2=input("Enter a string2:")

anagram(string1,string2)



#################

