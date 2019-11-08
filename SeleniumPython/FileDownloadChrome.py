from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options

# Driver Intialization
chromeOptions=Options()
prefs = {"download.default_directory" : "D:\SeleniumPython\dummyfiles"}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe",options=chromeOptions)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://demo.automationtesting.in/FileDownload.html")  # Launch Browser


#Generate and Download Text File
driver.find_element(By.XPATH,"//textarea[@id='textbox']").send_keys("Generate Text File")
driver.find_element(By.XPATH,"//button[@id='createTxt']").click()
driver.find_element(By.XPATH,"//a[@id='link-to-download']").click()



#Generate and Download PDF File
driver.find_element(By.XPATH,"//textarea[@id='pdfbox']").send_keys("Generate PDF File")
driver.find_element(By.XPATH,"//button[@id='createPdf']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@id='pdf-link-to-download']").click()





