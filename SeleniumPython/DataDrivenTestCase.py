from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtils

path="D:\SeleniumPython\dummyfiles\Login.xlsx"
sheetname="Sheet1"
expected_title="Find a Flight: Mercury Tours:"


#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

rows=XLUtils.RowCount(path,sheetname)
cols=XLUtils.ColumnCount(path,sheetname)
print("No of rows :",rows)
print("No of columns :",cols)


driver.get("http://www.newtours.demoaut.com/")  # Launch Browser

for r in range(2,rows+1):
    username=XLUtils.readData(path,sheetname,r,1)
    password = XLUtils.readData(path, sheetname, r, 2)

    driver.find_element(By.NAME,"userName").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.NAME,"login").click()

    if driver.title==expected_title:
        XLUtils.writeData(path,sheetname,r,3,"Pass")
    else:
        XLUtils.writeData(path, sheetname, r, 3, "Fail")
    driver.find_element(By.LINK_TEXT,"Home").click()

driver.quit()