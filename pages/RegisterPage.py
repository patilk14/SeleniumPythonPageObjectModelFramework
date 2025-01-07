from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    privacy_policy_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_subscribe_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"


    def enter_first_name(self,first_name):
        self.type_into_element(first_name,"first_name_id",self.first_name_id)

    def enter_last_name(self,last_name):
        self.type_into_element(last_name,"last_name_id",self.last_name_id)

    def enter_email_id(self,email_id):
        self.type_into_element(email_id,"email_id",self.email_id)

    def enter_telephone_number(self,telephone_no):
        self.type_into_element(telephone_no,"telephone_id",self.telephone_id)

    def enter_password(self,password):
        self.type_into_element(password,"password_id",self.password_id)

    def enter_confirm_password(self,confirm_password):
        self.type_into_element(confirm_password,"confirm_password_id",self.confirm_password_id)

    def click_on_privacy_policy(self):
        self.element_click("privacy_policy_name",self.privacy_policy_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def click_on_newsletter_subscribe_radio_box(self):
        self.element_click("newsletter_subscribe_xpath",self.newsletter_subscribe_xpath)

    def register_an_account(self,first_name,last_name,email_id,telephone_no,password,confirm_password,yes_or_no,privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_id(email_id)
        self.enter_telephone_number(telephone_no)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no.__eq__("yes"):
            self.click_on_newsletter_subscribe_radio_box()
        if privacy_policy.__eq__("select"):
            self.click_on_privacy_policy()
        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self):
        return self.retrieve_element_text("duplicate_email_warning_xpath",self.duplicate_email_warning_xpath)

    def retrieve_privacy_policy_warning(self):
        return self.retrieve_element_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath)

    def retrieve_first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_xpath",self.first_name_warning_xpath)

    def retrieve_last_name_warning(self):
        return self.retrieve_element_text("last_name_warning_xpath",self.last_name_warning_xpath)

    def retrieve_email_warning(self):
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    def retrieve_telephone_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)

    def retrieve_password_warning(self):
        return self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)




