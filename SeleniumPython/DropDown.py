from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#Driver Intialization
driver=webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()


driver.get("http://demo.automationtesting.in/Register.html") # Launch Browser


ele=driver.find_element(By.ID,"Skills")
drp=Select(ele)

#drp=Select(driver.find_element_by_id("Skills"))

#Select one option

#Select by Visible Text
#drp.select_by_visible_text("Adobe Photoshop")

# #Select by Index
#drp.select_by_index(1)

#Select by Value
#drp.select_by_value("Backup Management")


#Count no of options present
print(len(drp.options))

#Capture Options from dropdown
all_options=drp.options

for option in all_options:
    print(option.text)


# a=0
# for option in all_options:
#     print(option.text)
#     if option.text=="Windows1":
#         a=1
#         break
#
# if a==1:
#     print("pass")
# else:
#     print("fail")

driver.quit()

