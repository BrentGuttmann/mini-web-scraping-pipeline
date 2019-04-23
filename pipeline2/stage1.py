'''
STAGE 1 of PIPELINE 2
This apporach uses the data API to get the data directly
'''

import os
import json
import typing

dir_path: str = os.path.dirname(os.path.realpath(__file__))
input_file: str = dir_path+'/data1/output.json'

with open(input_file, 'r') as json_file:
    data = json.load(json_file)
    # print(type(data))
    # print(data['items'][0]['short_description'])

items = data['items']

text_entries: typing.List[str] = []

for item in items:
    # print(item['short_description'].trim())
    text_entries.append(item['short_description'].strip())

# print(text_entries)


# Establish input text location
output_file: str = dir_path+"/data2/extracted-text.txt"

with open(output_file, "w") as text_file:
    for entry in text_entries:
        print(entry, file=text_file)
