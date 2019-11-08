import time
from selenium import webdriver

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")


driver.get("http://demo.automationtesting.in/Register.html") # Launch Browser

print(driver.find_element_by_name("radiooptions").is_displayed())  #returns True/False   based on element status
print(driver.find_element_by_name("radiooptions").is_enabled())  #returns True/False   based on element status

ele=driver.find_element_by_name("radiooptions") #Create Webelement reference

time.sleep(3)
print(ele.is_selected())  #returns True/False   based on element status

time.sleep(3)
ele.click() # Select radio button

time.sleep(3)
print(ele.is_selected())



