from selenium import webdriver
from selenium.webdriver.common.by import By

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")

driver.get("https://fs2.formsite.com/R1Tuim/form1/index.html") # Launch Browser
driver.implicitly_wait(10)
driver.maximize_window()

#How to provide value into textbox
driver.find_element(By.NAME,"RESULT_TextField-4").clear()  #Clear the text in textbox
driver.find_element(By.NAME,"RESULT_TextField-4").send_keys("Siva")
driver.find_element(By.NAME,"RESULT_TextField-5").send_keys("Kumar")

#How to get status of textbox
status=driver.find_element(By.NAME,"RESULT_TextField-4").is_displayed()
print("Displayed or not : ",status)

status=driver.find_element(By.NAME,"RESULT_TextField-4").is_enabled()
print("Enabled or not : ",status)

#Find No of textboxes present in WebPage
inputboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
print(len(inputboxes))







