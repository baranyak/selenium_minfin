__author__ = 'mbaranyak'

import pages
from tests_pytest_framework.BaseClass import BaseClass
from configuration import USERNAME, PASSWORD


class TestLogIn(BaseClass):
    def test_login(self):
        main_page = pages.MainPage(self.driver)
        main_page.click_entrance_button()
        main_page.log_in(USERNAME, PASSWORD)
        assert main_page.user_bar_presence(), 'fail to login'

    def test_entrance_window(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.click_entrance_button(), "login page is not displayed"
