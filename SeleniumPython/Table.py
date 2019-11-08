from selenium import webdriver
from selenium.webdriver.common.by import By

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://techcanvass.com/examples/webtable.html") # Launch Browser
driver.implicitly_wait(10)


rows=len(driver.find_elements(By.XPATH,"//table[@id='t01']/tbody/tr"))
print("No of rows:",rows)

cols=len(driver.find_elements(By.XPATH,"//table[@id='t01']/tbody/tr[1]/th"))
print("No of Columns:",cols)

for r in range(2,rows+1):
    for c in range(1,cols+1):
       value=driver.find_element_by_xpath("//table[@id='t01']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
       print(value,end=" | ")
    print()


        



