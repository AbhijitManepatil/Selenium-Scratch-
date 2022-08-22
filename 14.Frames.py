#Handle Frames
#
'''
Example from :https://the-internet.herokuapp.com

Frames are embedded HTML which seats on top over base HTML,
We can not directly access to the frames, need to switch from driver to the frame.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

#Step 1:
driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")

#Step 2:
# Open sample url for Frame Example
driver.get("https://the-internet.herokuapp.com/iframe")

#Step 3:
#Switch control from Driver to Frame 
driver.switch_to.frame("mce_0_ifr")# use frame ID/name  .frame

#Step 4:
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am Abhijit, Testing for frame Automation")


#Switch from frame to normal window back
driver.switch_to.default_content() #back to original controll