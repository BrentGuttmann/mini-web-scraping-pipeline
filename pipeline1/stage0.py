'''
STAGE 0 of PIPELINE 1
Load html source and extract text in divs
'''

import os
import typing
from bs4 import BeautifulSoup

# Read contents of 'source.html' into string 'html'
dir_path: str = os.path.dirname(os.path.realpath(__file__))
source_file: str = dir_path+'/data0/source.html'
with open(source_file, 'r') as input_steam:
    html: str = input_steam.read()

# Use BeautifulSoup to find all divs in html with class 'rollover_description_inner'
soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
text_entries: typing.List[str] = []
for link in soup.find_all("div", {"class": "rollover_description_inner"}):
    text: str = link.text
    # DOnt include with dud text "Click for more"
    if not "Click for more" in text:
        # Use 'strip' method to remove superfluous white spaces
        text_entries.append(text.strip())


# Establish input text location
output_file: str = dir_path+"/data1/extracted-text.txt"

with open(output_file, "w") as text_file:
    for entry in text_entries:
        print(entry, file=text_file)
