from selenium import webdriver
from selenium.webdriver.common.by import By

#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html") # Launch Browser
driver.implicitly_wait(10)
print(driver.title)
driver.find_element(By.XPATH,"//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()
#print(driver.title)

print(driver.current_window_handle)  #Returns current window handle- Parent Browser

handles=driver.window_handles  #Returns all handles of opened browser windows


for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()  #Close only Parent Browser


#driver.quit()
#
