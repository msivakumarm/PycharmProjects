from selenium import webdriver

import time
import pytest

#If  ran from command line will get error,    from POMDemo.Pages.LoginPage import *
#ModuleNotFoundError: No module named 'POMDemo'. To handle this import below statements
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from SampleProject.Pages.LoginPage import LoginPage
from SampleProject.Pages.HomePage import HomePage

@pytest.yield_fixture()
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()
    driver.quit()
    print("Test Completed")


def test_login_valid(setup):
    #Login with Valid
    Url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(Url)

    #LoginPage
    lp=LoginPage(driver)
    lp.enter_username("Admin")
    lp.enter_password("admin123")
    lp.click_login()


    #HomePage
    hp=HomePage(driver)
    hp.click_welcome()
    hp.click_Logout()

    time.sleep(2)

#
# pytest --html=report.html
# pytest --html=report1.html --self-contained-html