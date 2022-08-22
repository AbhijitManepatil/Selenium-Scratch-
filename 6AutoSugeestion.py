##* NOT WORKING**********

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
# driver = webdriver.Chrome()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# # import timedriver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# # driver.implicitly_wait(0.5)
# driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")



 
import time
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# driver.get("https://www.google.com")
 
driver.get("http://www.blooddonors.in")
select = Select(driver.find_element_by_name('select'))
select.select_by_visible_text('Tamil Nadu')
drop = Select(driver.find_element_by_name('city'))
city_option = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//select[@name='city']/option[text()='Coimbotore']"))
city_option.click()