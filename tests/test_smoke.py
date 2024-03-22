from pages.home_page import HomePage, HomePageLocators
from selenium.webdriver.common.by import By


class TestSmoke:

    def test_login(self, registered_user, driver):
        """
        Verifies log-in functionality
        """
        page = HomePage(driver, HomePageLocators.URL)
        page.login_with_credentials(registered_user[0], registered_user[1])
        actual_welcome_text = page.get_text(HomePageLocators.GLOBAL_NAVIGATION_WELCOME)
        assert actual_welcome_text == f'Welcome {registered_user[0]}'

    def test_add_item_to_cart(self, logged_in_user):
        """
        Verifies adding item to cart functionality
        """
        home_page = HomePage(logged_in_user, HomePageLocators.URL)
        home_page.open_monitors_category()
        item_card_name, item_card_price = home_page.get_the_most_expensive_item_name_and_price()
        product_page = home_page.open_item_page(
            (By.XPATH, HomePageLocators.ITEM_NAME_BY_PRICE_XPATH.format(item_card_price)))
        assert product_page.product_name == item_card_name
        assert product_page.product_price == item_card_price
        product_page.add_item_to_cart()
        cart_page = product_page.open_cart_page()
        assert cart_page.items_qty_in_cart == 1
        assert cart_page.product_is_in_cart(item_card_name, item_card_price)

