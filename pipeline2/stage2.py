'''
STAGE 1 of PIPELINE 2
This approach uses the site's data API to get the data directly 
(without having to scrape and parse any html)
'''

import os
import json
import typing
from bs4 import BeautifulSoup

# Read in data from JSON file as a python dictionary
dir_path: str = os.path.dirname(os.path.realpath(__file__))
input_file: str = dir_path+'/data1/output.json'
with open(input_file, 'r') as json_file:
    data: typing.Dict = json.load(json_file)

# Extract 'short_description' items from nested list
text_entries: typing.List[str] = []
for item in data['items']:
    # Get text item and use bs4 to transoform any html artefacts
    soup = BeautifulSoup(item['short_description'], 'html.parser')
    # Extract text and strip it of any superfluous white space
    text_entries.append(soup.get_text().strip())

# Output list of items to text file
output_file: str = dir_path+"/data2/target-text.txt"
with open(output_file, "w") as text_file:
    for entry in text_entries:
        print(entry, file=text_file)
