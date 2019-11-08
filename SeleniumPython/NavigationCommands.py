import time
from selenium import webdriver

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")


driver.get("http://www.newtours.demoaut.com/") # Launch Browser
print(driver.title)  # Title - Welcome: Mercury Tours

time.sleep(3)

driver.get("http://www.google.co.in/")
print(driver.title)  # Title - Google

time.sleep(3)
driver.back()
print(driver.title)  # Title - Welcome: Mercury Tours

time.sleep(3)
driver.forward()
print(driver.title)  # Title - Google