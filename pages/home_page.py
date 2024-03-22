from typing import Tuple, List
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from random import choices
from string import ascii_letters, digits
import re
from pages.product_page import ProductPage
from time import sleep
from locators.home_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def page_is_ready(self) -> None:
        assert self.current_url == HomePageLocators.URL
        self.find_visible_elements(HomePageLocators.CATEGORIES_LEFT_MENU)

    def open_signup_popup(self) -> None:
        """
        Opens the 'Sign up' pop up.
        """
        self.click_element(HomePageLocators.GLOBAL_NAVIGATION_SIGNUP)
        self.wait.until(ec.visibility_of_element_located(HomePageLocators.SIGNUP_POPUP))

    def open_login_popup(self) -> None:
        """
        Opens 'Log in' pop up.
        """
        self.click_element(HomePageLocators.GLOBAL_NAVIGATION_LOGIN)
        self.wait.until(ec.visibility_of_element_located(HomePageLocators.LOGIN_POPUP))
        self.wait.until(ec.visibility_of_element_located(HomePageLocators.LOGIN_USERNAME))
        self.wait.until(ec.visibility_of_element_located(HomePageLocators.LOGIN_PASSWORD))

    def open_monitors_category(self) -> None:
        """
        Opens monitors category. Implicitly waits two secs for page to be updated.
        """
        self.click_element(HomePageLocators.CATEGORIES_LEFT_MENU_MONITORS)
        sleep(2)

    def get_prices(self) -> List:
        """
        Get prices of all currently present elements and returns them as a list.
        """
        prices = [element.text for element in self.find_visible_elements(HomePageLocators.ITEMS_PRICES)]
        return list(prices)

    def get_the_most_expensive_item_name_and_price(self) -> Tuple[str, str]:
        """
        Provides the most expensive item name and its price from currently visible cards as a Tuple object.
        """
        prices = self.get_prices()
        max_price = max(map(lambda x: re.search('\\$(.*)', x).group(1), prices))
        locator = (By.XPATH, HomePageLocators.ITEM_NAME_BY_PRICE_XPATH.format(max_price))
        item_name = self.get_text(locator)
        return item_name, max_price

    def open_item_page(self, locator) -> ProductPage:
        """
        Opens item page by provided locator and returns ProductPage object.
        """
        self.click_element(locator)
        product_page = ProductPage(self.driver, self.current_url)
        product_page.page_is_ready()
        return product_page

    def register_user(self) -> Tuple[str, str]:
        """
        Opens 'Sign up' pop up and registers a new user and return their username and password as a Tuple object.
        """
        user_name = ''.join(choices(ascii_letters + digits, k=12))
        password = ''.join(choices(ascii_letters + digits, k=8))
        self.open_signup_popup()
        self.send_text(HomePageLocators.SIGNUP_USERNAME, user_name)
        self.send_text(HomePageLocators.SIGNUP_PASSWORD, password)
        self.click_element(HomePageLocators.SIGNUP_BUTTON)
        alert = self.wait.until(ec.alert_is_present())
        if alert.text == HomePageLocators.SIGNUP_SUCCESSFUL_ALERT_TEXT:
            alert.accept()
            self.wait.until(ec.invisibility_of_element_located(HomePageLocators.SIGNUP_POPUP))
            return user_name, password
        raise ValueError(alert.text)

    def login_with_credentials(self, username, password) -> None:
        """
        Opens 'Log in' pop up, enters provided username and password and pushes 'Log in' button
        """
        self.open_login_popup()
        self.send_text(HomePageLocators.LOGIN_USERNAME, username)
        self.send_text(HomePageLocators.LOGIN_PASSWORD, password)
        self.click_element(HomePageLocators.LOGIN_BUTTON)
        self.wait.until(ec.invisibility_of_element_located(HomePageLocators.LOGIN_POPUP))
        self.wait.until(ec.visibility_of_element_located(HomePageLocators.GLOBAL_NAVIGATION_WELCOME))
        self.wait.until(ec.visibility_of_element_located(HomePageLocators.GLOBAL_NAVIGATION_LOGOUT))
