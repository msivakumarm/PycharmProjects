from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Frames.html") # Launch Browser

#Single Iframe
driver.switch_to.frame("singleframe")  #Switch to frame using id or name
driver.find_element(By.XPATH,"//div[@class='col-xs-6 col-xs-offset-5']//input").send_keys("Siva")

#Switch focus to browser
driver.switch_to.default_content()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

time.sleep(3)
frames=driver.find_elements_by_tag_name("iframe")
print(len(frames))
counter=0
for f in frames:
    print(f.get_attribute("src"))
    print(counter)
    counter=counter+1


# #Iframe with in an frame
driver.switch_to.frame(1)  #Switch to frame using index
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//div[@class='col-xs-6 col-xs-offset-5']//input").send_keys("Kumar")