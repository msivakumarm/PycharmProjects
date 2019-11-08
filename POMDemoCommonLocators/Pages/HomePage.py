import time

from selenium.webdriver.common.by import By
from POMDemoCommonLocators.Locators.locators import Locators
class HomePage:

    __welcome_lnk=Locators.welcome_lnk
    __Logout_lnk=Locators.Logout_lnk

    def __init__(self,driver):
        self.driver=driver

    def click_welcome(self):
        self.driver.find_element_by_link_text(self.__welcome_lnk).click()

    def click_Logout(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(self.__Logout_lnk).click()



