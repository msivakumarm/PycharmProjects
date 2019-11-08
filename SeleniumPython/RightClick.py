from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html") # Launch Browser
ele_RightClickMe=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

actions=ActionChains(driver)
actions.context_click(ele_RightClickMe).perform()
