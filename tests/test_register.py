from datetime import datetime

import pytest

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("kiran","ppp",self.generate_email_with_time_stamp(),"5555555","12345","12345","no","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_created_confirm_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("kiran","ppp",self.generate_email_with_time_stamp(),"5555555","12345","12345","yes","select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_created_confirm_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("kiran","ppp","kpp2015@gmail.com","1221111","1234567","1234567","yes","select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("","","","","","","no","no")
        expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning().__contains__(
            expected_privacy_policy_warning_message)
        expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning().__eq__(
            expected_first_name_warning_message)
        expected_last_name_warning_message = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning().__eq__(
            expected_last_name_warning_message)
        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning().__eq__(
            expected_email_warning_message)
        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning().__eq__(
            expected_telephone_warning_message)
        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning().__eq__(
            expected_password_warning_message)

