import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome", help="Type in browser n(me e.g.chrome OR firefox")



@pytest.fixture(scope='class')
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver=webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
    else:
        driver=webdriver.Ie(executable_path="../drivers/IEDriverServer.exe")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")