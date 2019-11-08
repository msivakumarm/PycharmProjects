from selenium import webdriver
from selenium.webdriver.common.by import By


#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()


driver.get("http://demo.automationtesting.in/Register.html") # Launch Browser

#Working with RadioButtons
ele=driver.find_element(By.XPATH,"//input[@value='Male']")
print(ele.is_selected())

ele.click()
print(ele.is_selected())

#Working with CheckBoxes
driver.find_element(By.XPATH,"//input[@value='Cricket']").click()


print(driver.find_element(By.XPATH,"//input[@value='Hockey']").is_selected())
driver.find_element(By.XPATH,"//input[@value='Hockey']").click()
print(driver.find_element(By.XPATH,"//input[@value='Hockey']").is_selected())



