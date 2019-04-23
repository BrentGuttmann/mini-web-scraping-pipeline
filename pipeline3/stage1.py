'''
STAGE 0 of PIPELINE 3
This approach downloads the bare html then triggers the JS in our python script to populate the full html
'''

import os
import time
import typing
from selenium import webdriver

# Set the url for the javascript-enriched webpage
urlpage: str = 'https://solarsystem.nasa.gov/missions/dawn/galleries/images/?' + \
    'page=0&per_page=25&order=created_at+desc&search=&' + \
    'tags=dawn%3Aceres&condition_1=1%3Ais_in_resource_list&category=51'

# Set up our browser driver
# Note: if 'chromedriver' is not in your $PATH paths, then you need to set here:
# driver = webdriver.Chrome('/path/to/chromedriver')
driver: typing.Any = webdriver.Chrome()

# Get the web page with Chrome; Chrome will execute the automatically triggered JS as normal
driver.get(urlpage)

# Sleep for ~2 seconds to ensure the page is fully loaded
time.sleep(2)

# The driver will enable us to control our Chrome instance programmatically
# Here, we execute a JS command to tell the browser to scroll to just above the 'MORE'
# button. The value of 3000 (pixels) has been tuned to place the MORE button in the
# bottom of the browser view on a 15'' monitor; adjust this value accordingly
driver.execute_script(
    """
        window.scrollTo(
            {
                top: document.body.scrollHeight - 3000,
                left: 0,
                behavior: 'smooth'
            }
        );
    """
)
time.sleep(2)

# We need to simulate clicking on the 'MORE' button in order to load multiples of items
# from the API. Note: unfortunately, the page will reroute if you try to increase the
# number of items/page, so 25 is the apparent maximum. We therefore need to loop through
# multiples of 25 up to some number larger (1000 here) than items that can be served
for i in range(1, int(1000/25)):
    print("=============")
    print("Page Number:  "+str(i))
    print("Items Loaded: "+str(i*25))
    print("Searching for the 'MORE' button...")
    try:
        # Look for MORE link (styled as a button)
        link = driver.find_element_by_link_text('MORE')
        # Try clicking it; this will raise an exception if no link was found
        link.click()
        # Sleep to let new data load
        time.sleep(1)
        # Scroll to new position of MORE button
        driver.execute_script(
            """
                window.scrollTo(
                    {
                        top: document.body.scrollHeight - 3000,
                        left: 0,
                        behavior: 'smooth'
                    }
                );
            """
        )
        time.sleep(1)
    except:
        print(
            '''
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                MORE BUTTON NOT FOUND
                    (this implies all available items got loaded)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            '''
        )
        break

# Final delay for contemplation of some awesome JS loading
time.sleep(2)

# Extract html as it now stands in Chrome browser
html_source: str = driver.page_source

# Close Chrome now that we're done
driver.quit()

# Save extracted javascript-enriched html to output file
dir_path: str = os.path.dirname(os.path.realpath(__file__))
output_file: str = dir_path+'/data1/computed.html'
with open(output_file, 'w') as the_file:
    the_file.write(html_source)
