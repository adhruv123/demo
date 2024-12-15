#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 20
##PROBLEM STATEMENT:
#   Write a Python code to demonstrate the following dictionary operations.

# Python Version : 3.7
############################################################################################################

"""

  inventory = {
        'gold' : 500,
        'pouch' : ['flint', 'twine', 'gemstone'],
        'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }
    
    Try to do the followings:
        - Add a key to inventory called 'pocket'.
        - Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
        - Sort the items in the list stored under the 'backpack' key.
        - Then remove dagger from the list of items stored under the 'backpack' key.
        - Add 50 to the number stored under the 'gold' key.


"""

#################

# Code Here
inventory = {
        'gold' : 500,
        'pouch' : ['flint', 'twine', 'gemstone'],
        'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }
inventory['pocket']=['seashell','strange berry','lint']
list1=[]
for x,value1 in inventory.items():
    if x == 'backpack':
        list1=value1
        list1.sort()
        list1.remove('dagger')
    if x == 'gold':
        value1=50
        
    print(f"{x} {value1}")



        
    



#################

