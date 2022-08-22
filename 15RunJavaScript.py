#Run Javascript using Python

'''
Selenium does not provide a functionality to scroll the window, (scrolling happing from the javascript point)
We can execute a JavaScript from selenium

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

#Step 1:
driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")

#Step 2:
# Open sample url for Frame Example
driver.get("https://the-internet.herokuapp.com") 

#scroll above page, from selenium using JavaScript
# 1.# 
# driver.execute_script("window.scrollBy(0,500)") #this fn execute a javaScrip Code as parameter

# 2.#
# Scroll at the bottem of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")