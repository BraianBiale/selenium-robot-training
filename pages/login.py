import json
import os

from selenium.webdriver.common.by import By

class TweetCloneLoginPage:

    URL = os.environ['BASE_URL'] + '/login'

    LOGIN_BTN = (By.CSS_SELECTOR, "form > button")
    REGISTER_BTN = (By.CSS_SELECTOR, "div > button")
    USERNAME_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    ERROR_LABEL = (By.XPATH, "(//form/label)[1]")
    USERNAME_LABEL = (By.XPATH, "(//div/label)[1]")
    PASSWORD_LABEL = (By.XPATH, "(//div/label)[2]")
    USERNAME_INPUT_CONTAINER = (By.XPATH, "(//form/div)[1]")
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "(//form/div)[2]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def press_register_btn(self):
        self.browser.find_element(*self.REGISTER_BTN).click()

    def do_login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BTN).click()

    def get_error_label_text(self):
        return self.browser.find_element(*self.ERROR_LABEL).text

    def get_username_label(self):
        return self.browser.find_element(*self.USERNAME_LABEL)

    def get_password_label(self):
        return self.browser.find_element(*self.PASSWORD_LABEL)

    def get_username_input_container(self):
        return self.browser.find_element(*self.USERNAME_INPUT_CONTAINER)

    def get_password_input_container(self):
        return self.browser.find_element(*self.PASSWORD_INPUT_CONTAINER)


