from selenium import webdriver
import pytest
import time
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from utils import utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver=self.driver
        driver.get(utils.Url)
        lp = LoginPage(driver)
        lp.enter_username(utils.username)
        lp.enter_password(utils.password)
        lp.click_login()



    def test_logout(self):
        driver=self.driver
        x = driver.title
        assert x == "abc"
        hp = HomePage(driver)
        hp.click_welcome()
        hp.click_Logout()
