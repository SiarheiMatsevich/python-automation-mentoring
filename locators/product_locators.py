from selenium.webdriver.common.by import By


class ProductPageLocators:
    URL = 'https://www.demoblaze.com/prod.html?idp_='
    PRODUCT_NAME = (By.XPATH, '//h2[contains(@class, "name") and ./parent::*[@id="tbodyid"]]')
    PRODUCT_PRICE = (By.XPATH, '//h3[contains(@class, "price-container")]')
    ADD_TO_CART_BY_ID_BUTTON_XPATH = '//a[@onclick="addToCart({})"]'
    PRODUCT_ADDED_ALERT_TEXT = 'Product added.'
    GLOBAL_NAVIGATION_CART = (By.XPATH, '//a[@href="cart.html"]')
