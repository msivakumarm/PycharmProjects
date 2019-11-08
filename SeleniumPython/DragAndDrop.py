from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://testautomationpractice.blogspot.com/") # Launch Browser
source_element=driver.find_element(By.XPATH,"//p[contains(text(),'Drag me to my target')]")
target_element=driver.find_element(By.XPATH,"//div[@id='droppable']")

actions=ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()