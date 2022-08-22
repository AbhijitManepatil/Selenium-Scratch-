from time import time
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# create webdriver object
# /usr/bin/chromedriver

#Step1: Create diver object
driver = webdriver.Chrome()
# get google.co.in
#Step2: call url
# driver.get("http://automationpractice.com/")
# driver.find_element(by=By.XPATH, value="//input[@id='search_query_top']").send_keys("summer")
# driver.find_element(by=By.XPATH, value ="//header/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
# time.sleep(4)
# coount= len()


###Amazon Automation
driver.get("http://amazon.com/")
driver.find_element(by=By.XPATH, value="//input[@id='twotabsearchtextbox']").send_keys("kids wear")
driver.find_element(by=By.XPATH, value ="//input[@id='nav-search-submit-button']").click()
time.sleep(4)
# coount= len(
driver.find_element(by=By.XPATH, value ="//span[contains(text(),\"Simple Joys by Carter's Girls and Toddlers' 4-Piec\")]").click()
time.sleep(2)
driver.find_element(by=By.XPATH,value="//input[@id='add-to-cart-button']").click()