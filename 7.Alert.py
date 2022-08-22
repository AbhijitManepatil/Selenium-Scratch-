
# import webdriver
from turtle import clear
from selenium import webdriver
  
# import Alert 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
# create webdriver object
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
  
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#to refresh the browser
driver.refresh()
#click on submit button
# driver.find_element_by_xpath("//button[@name='submit']").click()
driver.find_element(by=By.XPATH, value="//button[@name='submit']").click()
# alert object creation and switching focus to alert
a = driver.switch_to.alert
# accept the alert
a.accept()
driver.close()