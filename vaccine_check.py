from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from PIL import Image
from pytesseract import image_to_string 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#User inputs
file_path = '/my_path' #Edit path here
sleep_time = 600 #Sets 10 min time gap between search iterations
timeout = 5 #Time to wait for webpage to load
target_text = 'There are no vaccination appointments available for this clinic' #Text flag to decide on success/failure

#Processing path
options = Options()
options.headless = True
driver = webdriver.Firefox( executable_path = file_path, options = options )

#Examples of some provider links for Santa Clara County, can change this based on requirements
provider_links = [ 'https://vax.sccgov.org/mvcc', 'https://vax.sccgov.org/berger', 
                   'https://vax.sccgov.org/levis', 'https://vax.sccgov.org/gilroyhs',
                    'https://vax.sccgov.org/vhcev', 'https://vax.sccgov.org/vhctully',
                    'https://vax.sccgov.org/vsc' ]

#Begins continuous loop that checks for availability and reports results
avail_count = 0
print( 'Beginning Loop: ')
while True:
    curr_time = time.strftime("%H:%M:%S", time.localtime()) #Timestamp
    print( 'Time: ' + curr_time + '        ' + 'Total Slots: ' + str( avail_count ) )
    for provider in provider_links:
        driver.get( provider )
        #Waiting for page to fully load
        try:
            element_present = EC.presence_of_element_located((By.ID, 'element_id'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            pass
        el = driver.find_element_by_tag_name('body')
        el.screenshot( 'temp.png' ) #Saves image of webpage
        temp_text = image_to_string(Image.open('temp.png'),lang='eng') #Processes text in image
        print( 'Provider: ' + str( provider ) )
        if target_text in temp_text: #Searches for target text
            print( 'Result: No' )
        else: #Saves hit result if successful
            print( 'Result: Yes' )
            avail_count = avail_count + 1
            with open( 'success_text.txt', 'a' ) as myfile:
                temp_text = provider + '\n' + temp_text + '\n \n \n'
                myfile.write( temp_text )
    print( '\n' )
    time.sleep( sleep_time )





