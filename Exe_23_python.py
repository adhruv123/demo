#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 23
##PROBLEM STATEMENT:
#  You are given a space separated list of integers. 
# If all the integers are positive, then you need to check if any integer is a palindromic integer.

# Python Version : 3.7
############################################################################################################

"""

Input Format:
        The first line contains an integer N .N is the total number of integers in the list.
        The second line contains the space separated list of  integers.

    Output Format:
        Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

    Sample Input:
        5
        12 9 61 5 14 
    
    Sample Output:
        True

"""

#################
total_numbers=input("Enter how many numbers you want in list")
for x in len(total_numbers):
   list1=list(input("Enter a number:"))

for x in list1:
   if x>0:
      num=x
      temp=num
      reverse=0
      while temp > 0:
         remainder=temp % 10
         reverse= (reverse*10) +remainder
         temp = temp // 10
      if num == reverse:
        print(f"{num} is palindrom")
      else:
         print(f"{num} is not palindrome")


         

         


# Code Here


#################

