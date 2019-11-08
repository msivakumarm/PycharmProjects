from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC



#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")

driver.maximize_window()


driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver");
assert  "ExplicitlyWait Practice page in Selenium Webdriver" in driver.title #Compaare Strings

driver.find_element(By.ID,"display-other-button").click()

#driver.find_element(By.ID,"hidden").click()
#driver.find_element_by_id("hidden").click()  # Message: element not interactable

#Explicit Waut
wait=WebDriverWait(driver,20)

element=wait.until(EC.element_to_be_clickable((By.ID,"hidden")))
element.click()
