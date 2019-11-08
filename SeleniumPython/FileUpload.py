from selenium import webdriver
from selenium.webdriver.common.by import By


# Driver Intialization
driver = webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")  # Launch Browser

driver.find_element(By.NAME,"upload").send_keys("D:\SeleniumPython\dummyfiles\Desert.jpg")

