#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 28
##PROBLEM STATEMENT:
#  Write a Python code to parse the given json_exercise.json. Parse the json file and print the tags list from the json.
# Python Version : 3.7
############################################################################################################

"""

 - Add the below friend (in friends key) in given json and update the existing json file
        id = 1, name = "Faye Adams"
Use : "json_exercise.json" from files folder.

"""


#################
import json
# Code Here
with open('json_exercise.json','r+') as f:
        x = json.load(f)
        y=dict(x)
        dict1={'id':1,'name':'faye adam'}
        for key,value in y.items():
                if key == 'friends':
                        z=list(value)
                        z.append(dict1)
                        y['friends']=z
                        print(y)
                        f.seek(0) #override the file content
                        z=json.dump(y,f)
                        

                        
                        

                                 
       
   