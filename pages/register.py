import os
from selenium.webdriver.common.by import By

class TweetCloneRegisterPage:

    URL = os.environ['BASE_URL'] + '/register'

    REGISTER_BTN = (By.CSS_SELECTOR, "form > button")
    FORM_TITLE = (By.CSS_SELECTOR, "div > h1")
    NAME_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Name"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Username"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Password"]')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Confirm Password"]')
    ERROR_LABEL = (By.XPATH, '(//div/label)[11]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_form_title(self):
        return self.browser.find_element(*self.FORM_TITLE).text

    def press_register_btn(self):
        return self.browser.find_element(*self.REGISTER_BTN).click()

    def fill_register_form(self, name, username, email, password):
        self.browser.find_element(*self.NAME_INPUT).send_keys(name)
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(password)

    def get_error_label_text(self):
        return self.browser.find_element(*self.ERROR_LABEL).text

