import time

from selenium import webdriver


#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")

driver.implicitly_wait(20)  #Seconds

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

assert  "ExplicitlyWait Practice page in Selenium Webdriver" in driver.title #Compaare Strings

driver.find_element_by_id("display-other-button").click()
driver.find_element_by_id("hidden").click()