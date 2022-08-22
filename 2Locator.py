# https://www.rahulshettyacademy.com/angularpractice/

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#by ID
driver.find_element_by_id("exampleCheck1").click() #Automate checkbox
#driver.find_element_by_name("name").send_keys("Rahul")
#by Name
driver.find_element_by_name("name").send_keys("Abhijit")
# driver.find_element_by_name("email").send_keys("acm15aug@gmail.com")

#JAVA
# driver.findElementByName().sendKeys()

#by CSS #check and validate the css_selector from Inspect->console-> $("input[name='email']")
driver.find_element_by_css_selector("input[name='email']").send_keys("acm15aug@gmail.com")

#by Xpath check Xpath at console: $x("//input[@type='submit']")
driver.find_element_by_xpath("//input[@type='submit']").click()

#ChroPath extension
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys("@123456")
# //input[@id='exampleInputPassword1']
