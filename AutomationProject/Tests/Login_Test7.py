from selenium import webdriver
import pytest
import time
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from utils import utils
import allure

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
        try:
            x = driver.title
            #assert x == "OrangeHRM"
            assert x == "abc"
            hp = HomePage(driver)
            hp.click_welcome()
            hp.click_Logout()
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("Some exception occurred")
        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute")


