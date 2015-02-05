__author__ = 'User_name'

import unittest
from selenium import webdriver
import selenium_minfin.pages as pages


class TestMinfinComUa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://minfin.com.ua/")

    def test_title_of_main_page(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.is_title_matches(), "minfin.com.ua title doesn't match."

    def test_entrance_window(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.click_entrance_button(), "login page is not displayed"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
