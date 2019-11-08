from selenium import webdriver


path_png="D:\SeleniumPython\dummyfiles\Image1.png"
path_jpg="D:\SeleniumPython\dummyfiles\Image2.jpg"

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.newtours.demoaut.com/")  # Launch Browser

driver.save_screenshot(path_png) #supports any extension
driver.save_screenshot(path_jpg) #supports any extension


# driver.get_screenshot_as_file(path_png)  #supports png extension
# driver.get_screenshot_as_file(path_jpg)  #Warning will come but file will generated
driver.quit()