#Headless mode

'''
Running browser in background/ 
Running in background meaning in headless
Running headless mode is make to execute script faster

experiment: test time complexity using both 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

#* 
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument('headless')

#Step 1:
#*
driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://the-internet.herokuapp.com/windows")

#Step 2:
# Open sample url for Frame Example
driver.get("https://the-internet.herokuapp.com") 

#
print("I am completed")
driver.close()