from selenium.webdriver.common.by import By

class TweetCloneHomePage:

    PAGE_TITLE = (By.CSS_SELECTOR, "div > h1")

    def __init__(self, browser):
        self.browser = browser

    def get_page_title(self):
        page_title = self.browser.find_element(*self.PAGE_TITLE).text
        return page_title

