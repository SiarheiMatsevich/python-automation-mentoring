from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.cart_locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def page_is_ready(self) -> None:
        assert self.find_visible_element(CartPageLocators.PRODUCTS_GRID)

    @property
    def cart_is_empty(self) -> bool:
        """
        Checks if there are any items are added to the cart and return bool value.
        """
        table_body = self.find_visible_element(CartPageLocators.GRID_BODY)
        return False if table_body else True

    @property
    def items_qty_in_cart(self) -> int:
        """
        Counts all items in the cart and returns the quantity.
        """
        if self.cart_is_empty:
            return 0
        return len(self.find_visible_elements(CartPageLocators.GRID_ENTRIES))

    def product_is_in_cart(self, product_name: str, product_price: str) -> bool:
        """
        Checks if product with provided name and price is currently present in the cart.
        """
        assert not self.cart_is_empty
        products = self.find_visible_elements(
            (By.XPATH, CartPageLocators.ITEM_BY_NAME_AND_PRICE_XPATH.format(product_name, product_price)))
        return True if products else False
