from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

#Step 1:
driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")

#Step 2:
# Open sample url for Frame Example
driver.get("https://the-internet.herokuapp.com")

#Step 3:
#take a Screenshot of the current view (page)
driver.get_screenshot_as_file("screeshot.jpg")