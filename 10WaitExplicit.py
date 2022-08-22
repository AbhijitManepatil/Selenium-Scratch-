from multiprocessing.connection import wait
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
driver.find_element(by=By.XPATH, value="//input[@id='twotabsearchtextbox']").send_keys("kids wear") #search
driver.find_element(by=By.XPATH, value ="//input[@id='nav-search-submit-button']").click() # search click

###********* Explicit Wait
# - Only applied to specific function call
# - Implicit is for all but explicit for only specific fun
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"specific value (class name, text box, label"))

# time.sleep(4)
# coount= len(
driver.find_element(by=By.XPATH, value ="//span[contains(text(),\"Simple Joys by Carter's Girls and Toddlers' 4-Piec\")]").click() #choice
# time.sleep(2)
driver.find_element(by=By.XPATH,value="//input[@id='add-to-cart-button']").click() #Add cart