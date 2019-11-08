from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Browser Intialization
driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)


#Login with Valid
Url = "https://opensource-demo.orangehrmlive.com/"
driver.get(Url)

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

driver.find_element_by_link_text('Welcome Admin').click()
driver.find_element_by_link_text("Logout").click()
time.sleep(2)

#Close browser
driver.close()
driver.quit()
print("Test Completed")
