#pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



#Running in Chrome Browser
#driver=webdriver.Chrome(ChromeDriverManager().install())


#Running in Firefox Browser
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("http://www.newtours.demoaut.com/") # Launch Browser

driver.find_element_by_xpath("asa").click()
import time
time.sleep(3)
driver.find_element_by_xpath("asa").send_keys("Value")
print(driver.title)  # Title of the Page
print(driver.current_url)  # URL of the page
#print(driver.page_source)  #HTMl code for  the page
driver.close()  # Close Browser