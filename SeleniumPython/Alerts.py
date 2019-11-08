from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()


driver.get("http://testautomationpractice.blogspot.com/") # Launch Browser
driver.find_element(By.XPATH,"//button[contains(text(),'Click Me')]").click()
time.sleep(5)

#driver.switch_to.alert.accept()  #Closes alert window using OK button
driver.switch_to.alert.dismiss()  #Closes alert window using Cancel button

