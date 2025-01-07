from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    login_successful_message_link_text = "Edit your account information"

    def display_status_of_successful_login(self):
        return self.check_display_status_of_element("login_successful_message_link_text",self.login_successful_message_link_text)
