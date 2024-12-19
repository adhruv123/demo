#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 33
##PROBLEM STATEMENT:
# Convert below xml string to the json file, generate the json file at given location.
# Python Version : 3.7
############################################################################################################

"""
  xml_str = '''
        <cars>
            <car type="A" value="32"/>
            <car type="B" value="42"/>
            <car type="C" value="55"/>
            <car type="D" value="23"/>
        </cars>
    '''

    Output json file will contain as below
    { 'A': 32, 'B': 42, 'C': 55, 'D': 23 }

    NOTE: Use ElementTree for XML data handling

"""


#################

# Code Here
import xml.etree.ElementTree as ET
import json

# XML string
xml_str = '''
    <cars>
        <car type="A" value="32"/>
        <car type="B" value="42"/>
        <car type="C" value="55"/>
        <car type="D" value="23"/>
    </cars>
'''

# Parse the XML string
root = ET.fromstring(xml_str)

# Convert XML to dictionary
car_dict = {}
for car in root.findall('car'):
    car_type = car.get('type')
    car_value = int(car.get('value'))
    car_dict[car_type] = car_value

# Specify the output file path
output_file = 'output.json'

# Write the dictionary to a JSON file
with open(output_file, 'w') as json_file:
    json.dump(car_dict, json_file)

print(f"JSON file generated at {output_file}")




#################
