from selenium import webdriver
import pytest
import time
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class TestLogin():

    @pytest.fixture(scope='class')  #scope='function'
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("Test Completed")


    def test_login(self,test_setup):
        Url = "https://opensource-demo.orangehrmlive.com/"
        driver.get(Url)
        lp = LoginPage(driver)
        lp.enter_username("Admin")
        lp.enter_password("admin123")
        lp.click_login()


    def test_logout(self,test_setup):
        hp = HomePage(driver)
        hp.click_welcome()
        hp.click_Logout()