from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://demo.automationtesting.in/Register.html") # Launch Browser

ele_MoreTo=driver.find_element(By.XPATH,"//a[contains(text(),'More')]")
ele_Charts=driver.find_element(By.XPATH,"//a[contains(text(),'Charts')]")

actions=ActionChains(driver)


actions.move_to_element(ele_MoreTo).move_to_element(ele_Charts).click(ele_Charts).perform()