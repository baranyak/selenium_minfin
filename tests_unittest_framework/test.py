__author__ = 'User_name'

import unittest
from selenium import webdriver

import selenium_minfin.pages as pages


class TestMinfinComUa(unittest.TestCase):

    def setUp(self):
        fp = webdriver.FirefoxProfile()
        fp.add_extension(extension='../firebug-2.0.8-fx.xpi')
        fp.set_preference("extensions.firebug.currentVersion", "2.0.8")

        self.driver = webdriver.Firefox(firefox_profile=fp)
        self.driver.maximize_window()
        self.driver.get("http://minfin.com.ua/")

    def test_title_of_main_page(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.is_title_matches(), "minfin.com.ua title doesn't match."

    def test_entrance_window(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.click_entrance_button(), "login page is not displayed"

    def test_login(self):
        main_page = pages.MainPage(self.driver)
        main_page.click_entrance_button()
        main_page.log_in('testlogin', '101160235r')
        assert main_page.user_bar_presence(), 'fail to login'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
