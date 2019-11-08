from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Driver Intialization
fp=webdriver.FirefoxOptions()
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', "text/plain,application/pdf")  #Mime type
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', "D:\SeleniumPython\dummyfiles")
fp.set_preference('browser.download.folderList', 2) # custom location
fp.set_preference('pdfjs.disabled',True)

driver=webdriver.Firefox(executable_path="D:\SeleniumPython\drivers\geckodriver.exe",options=fp)

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





