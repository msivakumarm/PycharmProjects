from selenium import webdriver
from selenium.webdriver.common.by import By

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html") # Launch Browser
driver.implicitly_wait(10)


driver.switch_to.frame("packageListFrame")  #Switch to frame using id or name
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")  #Switch to frame using id or name
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")  #Switch to frame using id or name
driver.find_element(By.XPATH,"//div[@class='topNav']//a[contains(text(),'Deprecated')]").click()

