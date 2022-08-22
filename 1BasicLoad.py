# Python program to demonstrate
# selenium
import time
# import webdriver
from selenium import webdriver
 
# create webdriver object
# /usr/bin/chromedriver

#Step1: Create diver object
driver = webdriver.Chrome()
# get google.co.in
#Step2: call url
driver.get("https://www.facebook.com/")

#
print(driver.title)
print(driver.current_url)

# time.sleep(2)
driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
#minimize window
# driver.minimize_window()
#back
# time.sleep(2)
driver.back()
#referesh
# time.sleep(2)
driver.refresh()
#close current window
# driver.close()
#close all windows
# driver.quit()
#ref: https://stackoverflow.com/questions/60296873/sessionnotcreatedexception-message-session-not-created-this-version-of-chrome