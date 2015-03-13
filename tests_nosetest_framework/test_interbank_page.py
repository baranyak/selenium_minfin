__author__ = 'mbaranyak'

from tests_nosetest_framework.BaseClass import BaseClass
from pages import InterbankPage


class TestInterbankPage(BaseClass):

    def test_title_of_interbank_page(self):
        interbank_page = InterbankPage(self.driver)
        assert interbank_page.is_title_matches(), "title doesn't match."

    def test_usd_graph_presence(self):
        interbank_page = InterbankPage(self.driver)
        assert interbank_page.usd_graph_presence(), 'usd graph is missing'

    def test_main_header_presence(self):
        interbank_page = InterbankPage(self.driver)
        assert interbank_page.usd_graph_presence(), 'main header is missing'
