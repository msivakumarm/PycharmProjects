

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Chrome Browser
#driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

#Headless chrome
# chrome_options=Options()
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe",chrome_options=chrome_options)


#Running in Firefox Browser
#driver=webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

#Running in Firefox Browser - Headless
# firefox_options=webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
#driver=webdriver.Firefox(executable_path="../drivers/geckodriver.exe",firefox_options=firefox_options)



#Running in IE Browser
#driver=webdriver.Ie(executable_path="../drivers/IEDriverServer.exe")

#Running in IE Browser - Desired Capabilities
caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True

driver=webdriver.Ie(executable_path="../drivers/IEDriverServer.exe",desired_capabilities=caps)


time.sleep(3)
driver.get("http://www.newtours.demoaut.com/") # Launch Browser
time.sleep(3)
print(driver.title)  # Title - Welcome: Mercury Tours

time.sleep(3)

driver.get("http://www.google.co.in/")
print(driver.title)  # Title - Google

time.sleep(3)
driver.back()
print(driver.title)  # Title - Welcome: Mercury Tours

time.sleep(3)
driver.forward()
print(driver.title)  # Title - Google