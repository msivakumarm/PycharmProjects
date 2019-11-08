from selenium import webdriver
import pytest
import time

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
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()


    def test_logout(self,test_setup):
        driver.find_element_by_link_text('Welcome Admin').click()
        driver.find_element_by_link_text("Logout").click()
        time.sleep(2)



