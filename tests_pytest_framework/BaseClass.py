__author__ = 'mbaranyak'

from selenium import webdriver
from configuration import PROJECT_ROOT
from configuration import BASE_URL


class BaseClass:
    @classmethod
    def set_up(cls):
        fp = webdriver.FirefoxProfile()
        fp.add_extension(extension=PROJECT_ROOT + '/firebug-2.0.8-fx.xpi')
        fp.set_preference("extensions.firebug.currentVersion", "2.0.8")
        cls.driver = webdriver.Firefox(firefox_profile=fp)
        cls.driver.maximize_window()
        cls.driver.get(BASE_URL)

    @classmethod
    def tear_down(cls):
        cls.driver.close()
