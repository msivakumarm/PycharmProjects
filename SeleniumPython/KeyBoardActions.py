from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#Driver Intialization

driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://testautomationpractice.blogspot.com/") # Launch Browser
ele_Field1=driver.find_element(By.XPATH,"//input[@id='field1']")
ele_Field2=driver.find_element(By.XPATH,"//input[@id='field2']")

actions=ActionChains(driver)
actions.click(ele_Field1).key_down(Keys.LEFT_CONTROL).send_keys("a").send_keys("c").click(ele_Field2).send_keys("v").key_up(Keys.LEFT_CONTROL).perform()
