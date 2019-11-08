from selenium.webdriver.common.by import By
class LoginPage:

    __username_textbox="txtUsername" #private variable
    __password_textbox="txtPassword"
    __login_btn="btnLogin"

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


