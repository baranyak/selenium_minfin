__author__ = 'User_name'
from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTRANCE_BUTTON = (By.CLASS_NAME, 'jsmz-toggleAuthDropdown')
    LOGIN_WINDOW = (By.XPATH, '//span[text()="ВХОД"]')


class SearchResultsPageLocators:
    pass
