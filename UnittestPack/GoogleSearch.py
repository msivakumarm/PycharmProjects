from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Search(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Siva")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    def test_Search_dummy(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Kumar")
        self.driver.find_element_by_name("btnK1").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("C:/Users/SIVA/PycharmProjects/reports/"))
    #HTML reports fe