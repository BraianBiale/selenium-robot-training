import json
import os
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login import TweetCloneLoginPage
from pages.register import TweetCloneRegisterPage
from pages.home import TweetCloneHomePage


def test_register_btn_redirect(browser):
    login_page = TweetCloneLoginPage(browser)
    register_page = TweetCloneRegisterPage(browser)

    login_page.load()

    login_page.press_register_btn()

    assert register_page.get_form_title() == "Create your account"


def test_valid_login_redirect(browser):
    login_page = TweetCloneLoginPage(browser)
    home_page = TweetCloneHomePage(browser)
    mock_data = json.load(open('mock_data.json'))

    login_page.load()

    login_page.do_login(mock_data['valid_login_data']['username'], mock_data['valid_login_data']['password'])

    WebDriverWait(browser, 10).until(
        EC.url_to_be(os.environ['BASE_URL'] + '/')
    )

    assert home_page.get_page_title() == "Home"


def test_invalid_login(browser):
    login_page = TweetCloneLoginPage(browser)
    mock_data = json.load(open('mock_data.json'))

    login_page.load()

    login_page.do_login(mock_data['invalid_login_data']['username'], mock_data['invalid_login_data']['password'])

    assert login_page.get_error_label_text() == "Sorry, your username or password was incorrect. Please try again."
    assert login_page.get_username_label().value_of_css_property("color") == "rgba(224, 60, 57, 1)"
    assert login_page.get_password_label().value_of_css_property("color") == "rgba(224, 60, 57, 1)"
    assert login_page.get_username_input_container().value_of_css_property("border") == "1px solid rgb(224, 60, 57)"
    assert login_page.get_password_input_container().value_of_css_property("border") == "1px solid rgb(224, 60, 57)"
