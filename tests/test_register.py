import json

from pages.register import TweetCloneRegisterPage


def test_already_exists_user(browser):
    register_page = TweetCloneRegisterPage(browser)
    mock_data = json.load(open('mock_data.json'))

    register_page.load()

    register_page.fill_register_form(mock_data["already_register_data"]["name"],
                                     mock_data["already_register_data"]["username"],
                                     mock_data["already_register_data"]["email"],
                                     mock_data["already_register_data"]["password"])

    register_page.press_register_btn()

    assert register_page.get_form_title() == "Create your account"
    assert register_page.get_error_label_text() == "User already exists"

