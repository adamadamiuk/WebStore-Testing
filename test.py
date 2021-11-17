import math

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from locators.catalogue_locators import CatalogueLocators
from locators.home_locators import HomePageLocators
from pages.home_page import HomePage
from pages.store_page import StorePage
from selenium import webdriver
from driver import chromedriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

#
# pattern = "alba"
# tst = re.search(pattern, "sposob alba kanapka")
# print(tst.group(0))



driver = webdriver.Chrome(executable_path=chromedriver)
page = StorePage(driver)
driver.maximize_window()
driver.get(page.url)
action = StorePage(driver)
action.search('smartwatch')
action.add_basket()
action.remove_basket()


# assert str(action.verify_filter_min)[0:3] == "370"
# assert str(action.verify_filter_max)[0:3] == "420"

