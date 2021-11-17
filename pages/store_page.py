import math
import time
import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_locators import HomePageLocators
from pages.base_page import BasePage
from locators.catalogue_locators import CatalogueLocators

"""
Interactions on the Shop page, such as filtering, searching and verification of results
"""

class StorePage(BasePage):

    @property
    def url(self):
        return super(StorePage, self).url + '/zegarki-meskie/'
    # setting up the main store page


    def show_filters(self):
        filter_menu = self.driver.find_element_by_css_selector(
            CatalogueLocators.FILTER
        )
        ActionChains(self.driver).move_to_element(filter_menu).click(filter_menu).perform()
        time.sleep(2)
    # opening the filters panel

    def move_filter_slider(self):
        try:
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located
                ((By.CSS_SELECTOR, CatalogueLocators.FILTER_PRODUCTS
                  )))
            pass
        except:
            raise NoSuchElementException("Failed to locate necessary elements on the side panel.")
        # awaiting for the filter panel to load

        left_slider = self.driver.find_element_by_css_selector(
            CatalogueLocators.LEFT_SLIDER
        )
        right_slider = self.driver.find_element_by_css_selector(
            CatalogueLocators.RIGHT_SLIDER
        )

        move = ActionChains(self.driver)

        move.click_and_hold(right_slider).move_by_offset(-60, 0).release()
        time.sleep(2)
        move.click_and_hold(left_slider).move_by_offset(145, 0).release().perform()
        StorePage(self.driver).apply_filter.click()
        # setting up the filter to desired values

    @property
    def apply_filter(self):
        return self.driver.find_element_by_css_selector(
            CatalogueLocators.FILTER_PRODUCTS
        )

    @property
    def verify_filter_min(self):
        return self.driver.find_element_by_css_selector(
            CatalogueLocators.MIN_AMOUNT
        ).text
    # checking the min amount filtered

    @property
    def verify_filter_max(self):
        return self.driver.find_element_by_css_selector(
            CatalogueLocators.MAX_AMOUNT
        ).text
    # checking the max amount filtered


    def product_verification(self):
        # checking if prices of products received in filtered search are in the range

        price_class = self.driver.find_elements_by_class_name('price')

        for e in price_class:
            pattern = '([0-9]+[\,][0-9]+)([a-z][ł])(.)([0-9]+[\,][0-9]+)([a-z][ł])'
            try:
                match = re.search(pattern, e.text)
                changed = re.sub(',', '.', str(match.group(4)))
                assert float(changed) >= 370.00 and float(changed) <= 420.00
                print(changed)
            except:
                one_pattern = '([0-9]+[\,][0-9]+)([a-z][ł])'
                match = re.search(one_pattern, e.text)
                changed = re.sub(',', '.', str(match.group(1)))
                assert float(changed) >= 370.00 and float(changed) <= 420.00
                print(changed)

    def search(self, load):
        field = self.driver.find_element_by_css_selector(
            CatalogueLocators.SEARCH
        )
        field.click()
        field.send_keys(load)
        field.send_keys(Keys.ENTER)
    # searching for the desired product

        try:
            WebDriverWait(self.driver, 6).until(
                EC.visibility_of_element_located((
                    By.XPATH, CatalogueLocators.SEARCH_COMPL
                )))
            search_result = self.driver.find_element_by_css_selector(
                CatalogueLocators.SEARCH_RES
            )
            pattern_search = 'Wyniki dla smartwatch'
            assert (re.search(pattern_search, search_result.text)).group(0) == pattern_search
        except:
            raise NoSuchElementException('Failed to present the result of the search.')
    # awaiting for the list of products to load and appropriate message to be displayed

    def search_results(self, load):
        pattern = f'{load}'
        prods = self.driver.find_elements_by_class_name('woocommerce-loop-product__title')
        for elem in prods:
            res = (str(elem.text)).lower()
            word = re.search(pattern, res)
            assert word.group(0).lower() == f'{load}'
    # verifying if all results have the keyword in the name


    def count_page(self):
        pattern = '(Wyświetlanie 1–50 z )([0-9]+)( wyników)'
        items_num = self.driver.find_element_by_css_selector(
            CatalogueLocators.PAGER
        ).text
        match = (re.search(pattern, items_num)).group(2)

        counted = math.ceil(int(match) / 50)
        if counted == 0:
            return 1
        else:
            return int(counted)
    # checking the number of pages by calculating the number of results

    def search_pages(self, load):
        counter = StorePage.count_page(self)
        counter = int(counter)
        for page in range(0, int(counter)):
            self.driver.get(f'https://twojzegarek.eu/page/{page + 1}/?s={load}&post_type=product')
            StorePage.search_results(self, load)
    # moving through the result pages

    def add_basket(self):
        add = self.driver.find_element_by_css_selector(
            CatalogueLocators.ADD_BASKET
        )
        add.click()
        time.sleep(4)
    # adding to the basket

    def remove_basket(self):
        try:
            self.driver.find_element_by_css_selector(
                HomePageLocators.BASKET
            ).click()
        except:
            pass
        time.sleep(1)
        remove = self.driver.find_element_by_css_selector(
            CatalogueLocators.REMOVE_ITEM
        )
        remove.click()
    # removing from the basket


