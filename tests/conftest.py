from pytest import fixture
from selenium import webdriver
from pages.home_page import HomePageLocators
from pages.home_page import HomePage


@fixture(scope='session')
def setup_chrome_options():
    """
    Provides options for ChromeDriver.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-save-password-bubble')
    options.page_load_strategy = 'normal'
    return options


@fixture(scope='module')
def driver(setup_chrome_options):
    """
    Yields a driver object with applied options from setup_chrome_options fixture.
    """
    options = setup_chrome_options
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@fixture(scope='class')
def registered_user(driver):
    """
    Register a user and provide their user_name and password
    """
    page = HomePage(driver, HomePageLocators.URL)
    page.open_page()
    return page.register_user()


@fixture(scope='function')
def logged_in_user(registered_user, driver):
    """
    Logs in with provided credentials and returns a driver object.
    """
    page = HomePage(driver, HomePageLocators.URL)
    page.open_page()
    page.login_with_credentials(registered_user[0], registered_user[1])
    return driver
