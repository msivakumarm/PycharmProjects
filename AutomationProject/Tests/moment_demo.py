import os

from selenium import webdriver

screenshotName="xyz"
project_path = os.path.abspath(os.pardir)
project_path=project_path + "\\screenshots\\" + screenshotName + ".png"
print(project_path)

driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html") # Launch Browser

driver.get_screenshot_as_file(project_path)