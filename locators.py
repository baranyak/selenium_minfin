__author__ = 'User_name'
from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTRANCE_BUTTON = (By.CLASS_NAME, 'jsmz-toggleAuthDropdown')
    LOGIN_WINDOW = (By.XPATH, '//span[text()="ВХОД"]')
    LOGIN = (By.NAME, 'Login')
    PASSWORD = (By.NAME, 'Password')
    REMIND_ME_CHECKBOX = (By.XPATH, '//label[text()="Запомнить меня"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'mfz-form-submit-btn')
    USER_PICTOGRAM = (By.CLASS_NAME, 'js-mfz-userbar-toggle')

    USD_SPOT_MARKET_RATE = (By.XPATH, "//section/a[1]")
    USD_INTERBANK_RATE = (By.XPATH, "//section/a[2]")
    RUS_RUBLE_RATES = (By.XPATH, "//section/a[3]")