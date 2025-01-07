from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    input_email_id = "input-email"
    input_password_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    no_match_email_message_xpath = "//div[@id='account-login']/div[1]"


    def enter_email_id(self,email_id):
        self.type_into_element(email_id,"input_email_id",self.input_email_id)

    def enter_password(self,password):
        self.type_into_element(password,"input_password_id",self.input_password_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath",self.login_button_xpath)
        return AccountPage(self.driver)

    def login_to_application(self,email_id,password):
        self.enter_email_id(email_id)
        self.enter_password(password)
        return self.click_on_login_button()

    def retrieve_no_email_match_warning_message(self):
        return self.retrieve_element_text("no_match_email_message_xpath",self.no_match_email_message_xpath)


