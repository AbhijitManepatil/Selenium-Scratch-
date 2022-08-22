#Drop-down

#static drop-down & dynamic drop-down

'''
Static drop-down :  https://www.rahulshettyacademy.com/angularpractice/
Dynamic drop-down : makemytrip.com
''' 
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.support.select import Select
# import timedriver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify dropdown with Select class
sel = Select(driver.find_element(by=By.XPATH, value="//select[@name='continents']"))
#select by select_by_visible_text() method
sel.select_by_visible_text("Europe")
# time.sleep(0.8)
#select by select_by_index() method
# sel.select_by_index(0)
# driver.close()


'''

#1. Static drop-down
#select class provide the method to handle the option in dropdown
from selenium.webdriver.support.select import Select
#select class (select class only used when method in <select> tag in HTML)
# title = driver.find_element(by=By.XPATH, value="productTitle")  # by=By.ID, By.TAG_NAME, By.CLASS_NAME, By.NAME
# val=driver.find_element(by=By.XPATH, value="productTitle")
dropdown=Select(driver.find_element(by=By.ID, value="exampleFormControlSelect1")) #provide the locator
#Multiple ways to select value
#1.
dropdown.select_by_visible_text("Female")
#2.
dropdown.select_by_index(1)
#3.
# dropdown.select_by_value()


driver.get("https://www.facebook.com/")
'''