######## Test script to check ################
## 1.) Entering a text string in a search bar
## 2.) Read a text string from the page


## Loading library
import time # library used to introduce delay
from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# Running a webdriver 
browser = webdriver.Ie('C:\\Users\\Saaransh\\Downloads\\chromedriver.exe') # Change it to your drive and load the exe file
browser.maximize_window()
browser.implicitly_wait(10)
browser.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in browser.title

# code to find the search bar and enter string
elem = browser.find_element_by_id("user-message")
elem.clear()
elem.send_keys("Test Python")
time.sleep(2)

# code to locate and click the button
elem2 = browser.find_element_by_css_selector('#get-input > .btn')
elem2.click()

# code to test the string present on the screen
elem3 = browser.find_element_by_id("display")
assert "Test Python" in elem3.text
time.sleep(3)

# code to close the browser 
browser.close()

# Display to show everything ran fine
print("Test ran successfully")
