from selenium import webdriver


#Driver Intialization


driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/") # Launch Browser
driver.implicitly_wait(10)
driver.maximize_window()


#Scroll down the Page by pixel
#driver.execute_script("window.scrollBy(0,500)","")

#Scroll down the Page till element found
# ele=driver.find_element_by_xpath("//select[@name='skills']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)

#Scroll to end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

