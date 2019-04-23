'''
STAGE 0 of PIPELINE 2
This apporach uses the data API to get the data directly
'''

import os
import json
from requests import Response, get


# Get data api URL from website
api_url: str = 'https://solarsystem.nasa.gov/api/v1/resources/' + \
    '?page=0&per_page=999999&order=created_at+desc&search=' + \
    '&tags=dawn%3Aceres&condition_1=1%3Ais_in_resource_list&category=51'

# Call api and get JSON content from response
response: Response = get(api_url)
# content: str = response.content.decode("windows-1256").strip()
content: str = response.content.decode("utf-8").strip()

# Save json to output file
dir_path: str = os.path.dirname(os.path.realpath(__file__))
output_file: str = dir_path+'/data1/output.json'
with open(output_file, 'w') as the_file:
    the_file.write(content)
