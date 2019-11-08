from selenium.webdriver.common.by import By
from POMDemoCommonLocators.Locators.locators import Locators
class LoginPage:

    __username_textbox=Locators.username_textbox_id
    __password_textbox=Locators.password_textbox_id
    __login_btn=Locators.welcome_lnk

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,user):
        self.driver.find_element_by_id(self.__username_textbox).clear()
        self.driver.find_element_by_id(self.__username_textbox).send_keys(user)

    def enter_password(self,pwd):
        self.driver.find_element_by_id(self.__password_textbox).clear()
        self.driver.find_element_by_id(self.__password_textbox).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_id(self.__login_btn).click()


