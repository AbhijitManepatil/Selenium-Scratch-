# https://login.salesforce.com/

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")


#by CSS if ID is there:
#1. by - #
# driver.find_element_by_css_selector("#username").send_keys("Abhi") #old version
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Abhi")
#2. by - .
## driver.find_element_by_css_selector(".password").send_keys("@123") #old
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("@123")

#3. get link by Text
#driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot Your Password?").click()


#to clear
# driver.find_element_by_css_selector(".password").clear()