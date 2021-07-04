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


@when('User hovers over "store" button')
def step_impl(context):
    HomePage(context.driver).store_page()


@step('"Men\'s watches" category is selected')
def stem_impl(context):
    HomePage(context.driver).mens_watches()


@then('User is on the catalogue page')
def step_impl(context):
    expected_url = StorePage(context.driver).url
    assert context.driver.current_url == expected_url





