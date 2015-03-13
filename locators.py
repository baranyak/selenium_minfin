__author__ = 'mbaranyak'

from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTRANCE_BUTTON = (By.CLASS_NAME, 'jsmz-toggleAuthDropdown')
    LOGIN_WINDOW = (By.XPATH, '//span[text()="ВХОД"]')
    LOGIN = (By.NAME, 'Login')
    PASSWORD = (By.NAME, 'Password')
    REMIND_ME_CHECKBOX = (By.XPATH, '//label[text()="Запомнить меня"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'mfz-form-submit-btn')
    USER_PICTOGRAM = (By.CLASS_NAME, 'js-mfz-userbar-toggle')

    # USD_SPOT_MARKET_RATE = (By.XPATH, '//section/a[1]')
    # USD_INTERBANK_RATE = (By.XPATH, '//section/a[2]')
    # RUS_RUBLE_RATES = (By.XPATH, '//section/a[3]')

    MAIN_NEWS_BLOCK = (By.XPATH, '//div[@class="mfz-news-list mfz-news-list-hot"]')
    NEWS_BLOCK = (By.XPATH, '//div[@class="mfz-news-list"]')


class LoginPageLocators:
    ERROR_MESSAGE_LOGIN = (By.XPATH, '//div[starts-with(.,"Неправильное имя пользователя или пароль!")]')


class InterbankPageLocators:
    USD_CURRENCY_GRAPH = (By.ID, 'chart-ibusdday')
    MAIN_HEADER = (By.ID, '//div[@class="clear mb-header"]')