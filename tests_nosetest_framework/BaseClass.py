__author__ = 'mbaranyak'

from selenium import webdriver
from config import PROJECT_ROOT
from config import INTERBANK_URL


class BaseClass:

    def setup(self):
        fp = webdriver.FirefoxProfile()
        fp.add_extension(extension=PROJECT_ROOT + '/firebug-2.0.8-fx.xpi')
        fp.set_preference("extensions.firebug.currentVersion", "2.0.8")
        self.driver = webdriver.Firefox(firefox_profile=fp)
        self.driver.maximize_window()
        self.driver.get(INTERBANK_URL)

    def teardown(self):
        self.driver.close()
