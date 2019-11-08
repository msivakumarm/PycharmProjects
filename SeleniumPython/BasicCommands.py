import time
from selenium import webdriver

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")


driver.get("http://demo.automationtesting.in/Windows.html") # Launch Browser

print(driver.title)  # Title of the Page
print(driver.current_url)  # URL of the page
#print(driver.page_source)  #HTMl code for  the page


driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()
time.sleep(5)
#driver.close()  # Closes currently focussed browser
driver.quit()  # Close all the browsers
