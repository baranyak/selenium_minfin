__author__ = 'User_name'

import unittest
from selenium import webdriver

import pages
from locators import MainPageLocators
from configuration import PROJECT_ROOT
from configuration import BASE_URL


class TestMainPageElementsPresence(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fp = webdriver.FirefoxProfile()
        fp.add_extension(extension=PROJECT_ROOT + '/firebug-2.0.8-fx.xpi')
        fp.set_preference("extensions.firebug.currentVersion", "2.0.8")
        cls.driver = webdriver.Firefox(firefox_profile=fp)
        cls.driver.maximize_window()
        cls.driver.get(BASE_URL)

    def test_title_of_main_page(self):
        main_page = pages.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches(), "title doesn't match.")

    def test_usd_spot_market_rate_presence(self):
        self.assertTrue(self.driver.find_element(*MainPageLocators.USD_SPOT_MARKET_RATE).is_displayed(),
                        "Block 'USD spot market rate' element is not presence.")

    def test_usd_interbank_rate_presence(self):
        self.assertTrue(self.driver.find_element(*MainPageLocators.USD_INTERBANK_RATE).is_displayed(),
                        "Block 'USD interbank rate' element is not presence.")

    def test_russian_ruble_rates_presence(self):
        self.assertTrue(self.driver.find_element(*MainPageLocators.RUS_RUBLE_RATES).is_displayed(),
                        "Block 'Ruble rates' element is not presence.")

    def test_main_news_block_presence(self):
        self.assertTrue(self.driver.find_element(*MainPageLocators.MAIN_NEWS_BLOCK).is_displayed(),
                        "Main news block is not presence.")

    def test_main_news_block_presence(self):
        self.assertTrue(self.driver.find_element(*MainPageLocators.NEWS_BLOCK).is_displayed(),
                        "News block is not presence.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./reports'))