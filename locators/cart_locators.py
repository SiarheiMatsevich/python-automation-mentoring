from selenium.webdriver.common.by import By


class CartPageLocators:
    URL = 'https://www.demoblaze.com/cart.html'
    PRODUCTS_GRID = (By.XPATH, '//*[contains(@class, "table-responsive")]')
    GRID_BODY = (By.ID, 'tbodyid')
    GRID_ENTRIES = (By.XPATH, '//tbody/tr')
    ITEM_BY_NAME_AND_PRICE_XPATH = '//tbody/tr[td[text()="{}"] and td[text()="{}"]]'
