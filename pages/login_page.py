from locators.login_locators import LoginLocator
from pages.base_page import BasePage

"""
Actions necessary to test the login functionality
"""

class LoginPage(BasePage):

    @property
    def url(self):
        return super(LoginPage, self).url + '/moje-konto'
    # setting up 'main account' as a starting page for the test

    @property
    def login(self):
        return self.driver.find_element_by_css_selector(
            LoginLocator.BUTTON
        )

    @property
    def username(self):
        return self.driver.find_element_by_css_selector(
            LoginLocator.USER_LOGIN
        )

    @property
    def paste_password(self):
        return self.driver.find_element_by_css_selector(
            LoginLocator.USER_PASSWORD
        )

    def user_data(self, name, password):
        self.username.click()
        self.username.send_keys(name)
        self.paste_password.click()
        self.paste_password.send_keys(password)
    # pasting the username and the password to the login page

    @property
    def correct_login(self):
        return self.driver.find_element_by_css_selector(
            LoginLocator.USER_LOGGED
        )
    # searching for the element proving that the user has logged in

    @property
    def error_login(self):
        return self.driver.find_element_by_css_selector(
            LoginLocator.LOGIN_ERROR
        )
    # searching for the error message
