from selenium.webdriver.common.by import By


class HomePageLocators:
    URL = 'https://www.demoblaze.com/'
    GLOBAL_NAVIGATION_SIGNUP = (By.ID, 'signin2')
    GLOBAL_NAVIGATION_LOGIN = (By.ID, 'login2')
    GLOBAL_NAVIGATION_LOGOUT = (By.ID, 'logout2')
    GLOBAL_NAVIGATION_WELCOME = (By.ID, 'nameofuser')
    SIGNUP_POPUP = (By.ID, 'signInModal')
    SIGNUP_USERNAME = (By.ID, 'sign-username')
    SIGNUP_PASSWORD = (By.ID, 'sign-password')
    SIGNUP_BUTTON = (By.XPATH, '//*[@onclick="register()"]')
    SIGNUP_SUCCESSFUL_ALERT_TEXT = 'Sign up successful.'
    LOGIN_POPUP = (By.ID, 'logInModal')
    LOGIN_USERNAME = (By.ID, 'loginusername')
    LOGIN_PASSWORD = (By.ID, 'loginpassword')
    LOGIN_BUTTON = (By.XPATH, '//*[@onclick="logIn()"]')
    CATEGORIES_LEFT_MENU = (By.XPATH, '//*[contains(@class, "list-group") and a[@id="cat"]]')
    CATEGORIES_LEFT_MENU_MONITORS = (By.XPATH, '//*[@onclick="byCat(\'monitor\')"]')
    CATEGORIES_ITEMS_TILE = (By.ID, 'tbodyid')
    ITEMS_PRICES = (By.XPATH,
                    f'//*[@id="{CATEGORIES_ITEMS_TILE[-1]}"]//*[contains(@class, "card")]//h5[starts-with(text(), "$")]'
                    )
    ITEM_NAME_BY_PRICE_XPATH = ('(//*[@id="tbodyid"]//*[contains(@class, "card")]//h4[./following-sibling::h5['
                                'contains(text(), "{}")]])[1]')
