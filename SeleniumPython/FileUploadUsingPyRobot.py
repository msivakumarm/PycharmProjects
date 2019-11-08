


from selenium import webdriver
from selenium.webdriver.common.by import By
from pyrobot import Robot
import time


# Driver Intialization
driver = webdriver.Chrome(executable_path="D:\SeleniumPython\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://m.4shared.com/")  # Launch Browser
driver.find_element_by_xpath("//label[@class='big-button w-b']").click()
robot=Robot()
time.sleep(5)
robot.type_string("D:\SeleniumPython\dummyfiles\Desert.jpg")
robot.key_press(key="ENTER")

