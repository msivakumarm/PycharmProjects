from selenium import webdriver
from selenium.webdriver.common.by import By


#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()


driver.get("http://www.newtours.demoaut.com/") # Launch Browser

#How Many Links Present
links=driver.find_elements(By.TAG_NAME,"a")
print("No of Links Present :",len(links))

#Capture Links
for link in links:
    print(link.text)

#Click on Links
driver.find_element(By.LINK_TEXT,"REGISTER").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()


