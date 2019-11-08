from selenium import webdriver


#Running in Chrome Browser
#driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")


#Running in Firefox Browser
#driver=webdriver.Firefox(executable_path="D:\SeleniumPython\drivers\geckodriver.exe")


#Running in IE Browser
driver=webdriver.Ie(executable_path="D:\SeleniumPython\drivers\IEDriverServer.exe")

driver.get("http://www.newtours.demoaut.com/") # Launch Browser

print(driver.title)  # Title of the Page
print(driver.current_url)  # URL of the page
#print(driver.page_source)  #HTMl code for  the page
driver.close()  # Close Browser