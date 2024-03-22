from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import re
from pages.cart_page import CartPageLocators, CartPage
from locators.product_locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def page_is_ready(self) -> None:
        assert ProductPageLocators.URL in self.current_url
        self.wait.until(ec.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME))

    @property
    def item_id(self) -> str:
        """
        Extracts id of currently opened item and returns it as a string object.
        """
        return re.search(r'(\d+)$', self.current_url).group(1)

    @property
    def product_name(self) -> str:
        """
        Returns a name of the product.
        """
        return self.get_text(ProductPageLocators.PRODUCT_NAME)

    @property
    def product_price(self) -> str:
        """
        Returns the price of currently opened product.
        """
        price_number = re.search(r'\$(\d+|\.|,).*', self.get_text(ProductPageLocators.PRODUCT_PRICE)).group(1)
        return price_number

    def add_item_to_cart(self) -> None:
        """
        Adds currently opened item to the cart.
        """
        self.click_element((By.XPATH, ProductPageLocators.ADD_TO_CART_BY_ID_BUTTON_XPATH.format(self.item_id)))
        alert = self.wait.until(ec.alert_is_present())
        if alert.text != ProductPageLocators.PRODUCT_ADDED_ALERT_TEXT:
            raise ValueError(alert.text)
        alert.accept()

    def open_cart_page(self) -> CartPage:
        """
        Opens cart page and return CartPage object.
        """
        self.click_element(ProductPageLocators.GLOBAL_NAVIGATION_CART)
        self.wait.until(ec.url_to_be(CartPageLocators.URL))
        cart_page = CartPage(self.driver, self.current_url)
        cart_page.page_is_ready()
        return cart_page
