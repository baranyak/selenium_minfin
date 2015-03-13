__author__ = 'mbaranyak'

from locators import MainPageLocators
from locators import InterbankPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        return self.driver.page_source


class MainPage(BasePage):

    def is_title_matches(self):
        return "Минфин — деловое сообщество, банки, валюта, личные финансы" in self.driver.title

    def click_entrance_button(self):
        entrance_button = self.driver.find_element(*MainPageLocators.ENTRANCE_BUTTON)
        entrance_button.click()
        login_window = self.driver.find_element(*MainPageLocators.LOGIN_WINDOW)
        return login_window.is_displayed()

    def log_in(self, username, password):
        self.driver.find_element(*MainPageLocators.LOGIN).send_keys(username)
        self.driver.find_element(*MainPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).submit()
        return LoginPage(self.driver)

    def user_bar_presence(self):
        return self.driver.find_element(*MainPageLocators.USER_PICTOGRAM).is_displayed()


class InterbankPage(BasePage):

    def is_title_matches(self):
        return 'Межбанк онлайн, межбанковский курс валют в Украине, котировки межбанка — Минфин:' == self.driver.title


class LoginPage(BasePage):

    def login_error_message_presence(self):
        return self.driver.find_element(*InterbankPageLocators.ERROR_MESSAGE_LOGIN).is_displayed()