from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Substring 'login' is missing from the link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element \
            (By.ID, "id_registration-email")
        password_field = self.browser.find_element \
            (By.ID, "id_registration-password1")
        repeated_password_field = self.browser.find_element \
            (By.ID, "id_registration-password2")
        email_field.send_keys(email)
        password_field.send_keys(password)
        repeated_password_field.send_keys(password)
        registration_button = self.browser.find_element \
            (*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
