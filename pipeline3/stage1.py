'''
STAGE 1 of PIPELINE 3
Having saved the html by running it in a locally controlled browser, we can now
use BeautifulSoup as before to parse and extract our desired data.
'''

import os
import typing
from bs4 import BeautifulSoup

# Read contents of 'computed.html' into string 'html'
dir_path: str = os.path.dirname(os.path.realpath(__file__))
input_file: str = dir_path+'/data1/computed.html'
with open(input_file, 'r') as input_steam:
    html: str = input_steam.read()

# Use BeautifulSoup to find all divs in html with class 'rollover_description_inner'
# The key line here is marked † below; it uses the beautiful soup parser to select
# all html elements with class 'rollover_description_inner' that have a parent li
# element with class 'slide'. This selection criterion was determined by examining
# the html structure from data0/source.html and doing some trial and error"
soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
text_entries: typing.List[str] = []
for link in soup.select('li.slide .rollover_description_inner'):  # †
    text: str = link.text
    # Don't include entries with dud text "Click for more"
    if not "Click for more" in text:
        # Use 'strip' method to remove superfluous white space, and add to our string array
        text_entries.append(text.strip())


# Loop through our string array and print entries to output file
output_file: str = dir_path+"/data2/extracted-text.txt"
with open(output_file, 'w') as text_file:
    for entry in text_entries:
        print(entry, file=text_file)
