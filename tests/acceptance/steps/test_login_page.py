from behave import *
from selenium import webdriver

from pages.login_page import LoginPage
from driver import chromedriver

"""
Testing the login function and moving to the user panel
"""

@given('User is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=chromedriver)
    page = LoginPage(context.driver)
    context.driver.get(page.url)


@then('User is on the login page')
def step_impl(context):
    page = LoginPage(context.driver).url
    expected = 'https://twojzegarek.eu/moje-konto'
    assert page == expected


@step('User types in login and password')
def step_impl(context):
    user_name = "test_user01"
    password = "pass123selenium!"

    page_log = LoginPage(context.driver)
    page_log.user_data(user_name, password)
    # checking if the user can log in using correct credentials
    # user has to be created before testing and the credentials should be included above


@step('User types in wrong login and password')
def step_impl(context):
    user_name = "test_user01"
    password = "wrong_password"

    page_log = LoginPage(context.driver)
    page_log.user_data(user_name, password)
    # checking if the user can log in using incorrect credentials


@step('User clicks log in button')
def step_impl(context):
    LoginPage(context.driver).login.click()


@then('Login error page is displayed')
def step_impl(context):
    LoginPage(context.driver).error_login.is_displayed()


@then('"My Account" page is displayed')
def step_impl(context):
    LoginPage(context.driver).correct_login.is_displayed()
