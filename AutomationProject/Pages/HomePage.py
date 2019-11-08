import time

from selenium.webdriver.common.by import By
class HomePage:

    __welcome_lnk="Welcome Admin" #private variable
    __Logout_lnk="Logout"
    #__Logout_lnk = "Logout1" # broken link report - no such element exception

    def __init__(self,driver):
        self.driver=driver

    def click_welcome(self):
        self.driver.find_element_by_link_text(self.__welcome_lnk).click()

    def click_Logout(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(self.__Logout_lnk).click()



