from behave import *

from pages.home_page import HomePage
from pages.store_page import StorePage

"""
Moving between elements of the page
"""

@when('User clicks "My Account"')
def step_impl(context):
    context.driver.maximize_window()
    HomePage(context.driver).my_account_button.click()


@when('User hovers over "Men\'s watches" button')
def step_impl(context):
    HomePage(context.driver).store_page()


@step('"Zagarki meskie na pasku" category is selected')
def stem_impl(context):
    HomePage(context.driver).mens_watches()


@then('User is on the catalogue page')
def step_impl(context):
    expected_url = "https://twojzegarek.eu/zegarki-meskie-na-pasku/"
    assert context.driver.current_url == expected_url





