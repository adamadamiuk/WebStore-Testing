import time
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from driver import chromedriver

from pages.store_page import StorePage
from pages.home_page import HomePage
from locators.home_locators import HomePageLocators

"""
Testing interactions with store's functionalities
"""

@when('User clicks "agree"')
def step_impl(context):
    HomePage(context.driver).gdpr_acceptance.click()


@then('The GDPR prompt disappears')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 2).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, HomePageLocators.GDPR)))
        not_found = True
    except:
        not_found = False

    assert not_found
    # checking if the information about cookies disappears once "accept" clicked


@given('User is on the "Man\'s watches" page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=chromedriver)
    page = StorePage(context.driver)
    context.driver.maximize_window()
    context.driver.get(page.url)


@when('"Show filters" is selected')
def step_impl(context):
    StorePage(context.driver).show_filters.click()


@step('Price range 370 - 420 is selected')
def step_impl(context):
    action = StorePage(context.driver)
    action.move_filter_slider()

    assert str(action.verify_filter_min)[0:3] == "370"
    assert str(action.verify_filter_max)[0:3] == "420"


@then('The list of products in correct range is displayed')
def step_impl(context):
    action = StorePage(context.driver)
    action.product_verification()


@step('Searching for "Smartwatch" in the catalogue of products')
def step_impl(context):
    action = StorePage(context.driver)
    action.search('smartwatch')


@when('The list of retrieved products includes smartwatches')
def step_impl(context):
    action = StorePage(context.driver)
    action.search_pages('smartwatch')


@then('User adds a product to the basket')
def step_impl(context):
    action = StorePage(context.driver)
    action.add_basket()


@step('The item counter in the basket is 1')
def step_impl(context):
    action = HomePage(context.driver)
    basket_one = action.basket_num
    expected = '1'
    assert str(basket_one) == expected


@when('User removes an item from the basket')
def step_impl(context):
    time.sleep(1)
    action = StorePage(context.driver)
    action.remove_basket()
