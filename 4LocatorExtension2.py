#//tagname[text()=’xxx’]
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")

# Xpath by gettting text, use only when text in page is constant.
#tagnane[text()="text"]
##driver.find_element_by_xpath("//a[text()='Cancel']").click()  #old

# driver.find_element(By.XPATH, "//a[text()='Try for Free']").click()

#Xpath -> parent child   #note: be on same page(valid page)
print(driver.find_element(By.XPATH,"//form[@name='login']/div[1]/label").text)

#using ChroPath Plugin:
driver.find_element(By.XPATH,"//label[contains(text(),'Username')").text)
