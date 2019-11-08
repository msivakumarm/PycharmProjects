import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def test_setup(request):
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")