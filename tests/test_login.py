from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from tests.conftest import setup_and_teardown

class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application("kpp2015@gmail.com","12345")
        assert account_page.display_status_of_successful_login()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(),"12345")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_no_email_match_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("kpp2015@gmail.com","12345111")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_no_email_match_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("","")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_no_email_match_warning_message().__contains__(expected_warning_message)


        #Another method
        #timestamp = datetime.datetime.now()
        #formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S").replace("-","_").replace(" ","_").replace(":","_")
        #return "kiranpp"+formatted_timestamp+"@gmail.com"



