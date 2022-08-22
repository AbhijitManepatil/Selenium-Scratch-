# *** Tutorial No. : 61
#Handlding child window and Tabs
#***************** Ref: https://the-internet.herokuapp.com/


'''
window_handles is used for working with different windows. 
It stores the window ids that are used for switching.
switch_to.window method is used for switching between the 
windows with the help of window_handles ids.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")

# Open login yahoo for sample url
driver.get("https://the-internet.herokuapp.com/windows")  
  
# print title of yahoo window
print("First window title = " + driver.title)
  
# Clicks on privacy and it opens in new window
# driver.find_element_by_class_name("privacy").click()
driver.implicitly_wait(5)
driver.find_element(by=By.LINK_TEXT, value="Click Here").click()
  
# switch window in 7 seconds
# time.sleep(7)  

  
# window_handles[1] is a second window
driver.switch_to.window(driver.window_handles[1])
  
# prints the title of the second window
print("Second window title = " + driver.title)
  
# window_handles[0] is a first window
driver.switch_to.window(driver.window_handles[0])
  
# prints windows id
print(driver.window_handles)  