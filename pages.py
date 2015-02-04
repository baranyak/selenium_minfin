__author__ = 'User_name'

from locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Минфин — деловое сообщество, банки, валюта, личные финансы" in self.driver.title

    def click_entrance_button(self):
        entrance_button = self.driver.find_element(*MainPageLocators.ENTRANCE_BUTTON)
        entrance_button.click()
        login_window = self.driver.find_element(*MainPageLocators.LOGIN_WINDOW)
        return login_window.is_displayed()


class CurrencyPage(BasePage):

    def bla(self):
        pass
