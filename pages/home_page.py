import time
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.home_locators import HomePageLocators

"""
Basic interactions and elements on the main page
"""

class HomePage(BasePage):

    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def gdpr_acceptance(self):
        return self.driver.find_element_by_css_selector(
            HomePageLocators.GDPR_ACCEPT
        )

    @property
    def gdpr_info(self):
        return self.driver.find_element_by_css_selector(
            HomePageLocators.GDPR
        )

    @property
    def basket_num(self):
        time.sleep(1)
        return self.driver.find_element_by_css_selector(
            HomePageLocators.BASKET_EMPTY).text

    @property
    def basket(self):
        return self.driver.find_element_by_css_selector(
            HomePageLocators.BASKET
        )

    @property
    def menu_bar(self):
        return self.driver.find_element_by_css_selector(
            HomePageLocators.MENU_BAR
        )

    @property
    def my_account_button(self):
        return self.driver.find_element_by_xpath(
            HomePageLocators.LOGIN_BUTTON
        )

    def store_page(self):
        store_button = self.driver.find_element_by_css_selector(
            HomePageLocators.STORE_BUTTON
        )
        action = ActionChains(self.driver)
        action.move_to_element(store_button).perform()
    # hovering over "Store" button

    def mens_watches(self):
        action = ActionChains(self.driver)
        store_button = self.driver.find_element_by_css_selector(
            HomePageLocators.STORE_BUTTON
        )
        mens_watches = self.driver.find_element_by_css_selector(
            HomePageLocators.MENS_WATCHES
        )
        action.move_to_element(store_button).perform()
        action.move_to_element(mens_watches).perform()
        action.move_to_element(mens_watches).click().perform()
    # moving the cursor to Man's Watches button and clicking it

