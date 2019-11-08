from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://testautomationpractice.blogspot.com/") # Launch Browser
ele_CopyText=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")

actions=ActionChains(driver)
actions.double_click(ele_CopyText).perform()
