from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "http://newtours.demoaut.com/"
underConsTitle = "Under Construction: Mercury Tours"

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseUrl)


linkElements = driver.find_elements(By.TAG_NAME,"a")
print(len(linkElements)) #no of links
# for e in linkElements:
#     print(e.text)  #name of link

linkTexts=list()

#extract the link texts of each link element
for e in linkElements:
    linkTexts.append(e.text)

print(linkTexts)
#
#
# #test each link
for t in linkTexts:
    driver.find_element_by_link_text(t).click()
    time.sleep(1)
    if driver.title==underConsTitle:
        print(  "\"" + t + "\""+ " is under construction.")
    else:
        print("\"" + t + "\""+ " is working.")
    driver.back()
    time.sleep(1)

driver.quit()