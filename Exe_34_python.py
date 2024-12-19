#############################################################################################################
#Topic : BASIC PYTHON
#Exercise Number : 34
##PROBLEM STATEMENT:
# Convert below python_xml_exe.xml file to the equivalent csv file
# Python Version : 3.7
############################################################################################################

"""
NOTE: Use ElementTree for XML data handling.
USE : python-xml_exe.xml from files folder.

"""


#################

# Code Here
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('python_xml_exe.xml')
root = tree.getroot()
output_file = 'output.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write CSV header
    first_record = root.find('./RECORD')
    header = [child.tag for child in first_record]
    csv_writer.writerow(header)
    
    # Write CSV rows
    for record in root.findall('./RECORD'):
        row = [child.text for child in record]
        csv_writer.writerow(row)

print(f"CSV file generated at {output_file}")

#################
 
