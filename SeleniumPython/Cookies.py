from selenium import webdriver

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")  # Launch Browser

#Capture all cookies created by browser
cookies=driver.get_cookies()

print("No of Cookies :",len(cookies))   #Count number of Cookies have been created
print(cookies)  # Print all the cookie pairs

#Add new cookie to browser
cookie={'name':'MyCookie', 'value':'siva'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()


print("No of Cookies :",len(cookies))   #Count number of Cookies after adding new cookie
print(cookies)  # Print all the cookie pairs


#Delete cookie
#driver.delete_cookie("csm-hit")
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("No of Cookies :",len(cookies))   #Count number of Cookies after Deleting new cookie
print(cookies)  # Print all the cookie pairs



driver.quit()

