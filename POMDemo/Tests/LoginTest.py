from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from POMDemo.Pages.LoginPage import *
from POMDemo.Pages.HomePage import *

#Browser Intialization
driver=webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)


#Login with Valid
Url = "https://opensource-demo.orangehrmlive.com/"
driver.get(Url)

#LoginPage
lp=LoginPage(driver)
lp.enter_username("Admin")
lp.enter_password("admin123")
lp.click_login()


#HomePage
hp=HomePage(driver)
hp.click_welcome()
hp.click_Logout()

time.sleep(2)

#Close browser
driver.close()
driver.quit()
print("Test Completed")
