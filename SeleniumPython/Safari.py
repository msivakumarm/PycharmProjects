from selenium import webdriver

driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
driver.get("https://www.google.com")
print(driver.title)
driver.quit()