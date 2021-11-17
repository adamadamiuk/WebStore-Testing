from behave import *
from selenium import webdriver
import time
from driver import chromedriver

from pages.home_page import HomePage

"""
Testing the content of the main page
"""

@given('User is on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=chromedriver)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@step('Menu bar is visible')
def step_impl(context):
    HomePage(context.driver).menu_bar.is_displayed()


@step('"My account" button is visible')
def step_impl(context):
    HomePage(context.driver).my_account_button.is_displayed()


@step('GDPR prompt informing about cookies is visible')
def step_impl(context):
    HomePage(context.driver).gdpr_info.is_displayed()


@step('User can see the basket')
def step_impl(context):
    HomePage(context.driver).basket.is_displayed()


@then('The item counter in the basket is 0')
def step_impl(context):
    time.sleep(1)
    basket_zero = HomePage(context.driver).basket_num
    expected = '0'
    assert str(basket_zero) == expected
