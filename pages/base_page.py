from typing import Tuple, List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from abc import abstractmethod


class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=30)

    @abstractmethod
    def page_is_ready(self) -> None:
        """
        Explicit wait for page to be ready for interactions.
        """
        raise NotImplementedError

    @property
    def current_url(self) -> str:
        """
        Current page url.
        """
        return self.driver.current_url

    def open_page(self) -> None:
        """
        Opens page using provided url.
        """
        self.driver.get(self.url)
        self.page_is_ready()

    def click_element(self, locator: Tuple[str, str]) -> None:
        """
        Explicitly waits until an element is clickable and then clicks the element using given locator.
        """
        return self.wait.until(ec.element_to_be_clickable(locator)).click()

    def get_text(self, locator: Tuple[str, str]) -> str:
        """
        Explicitly waits until an element is present and then clicks the element using given locator.
        """
        return self.wait.until(ec.presence_of_element_located(locator)).text

    def send_text(self, locator: Tuple[str, str], value: str):
        """
        Explicitly waits until an element is clickable and then enters the given text into
        the element using given locator.
        """
        self.wait.until(ec.element_to_be_clickable(locator)).send_keys(value)

    def find_visible_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """
        Explicitly waits until all the elements located by provided locator are visible and then return a list of
        WebElement objects.
        """
        try:
            return self.wait.until(ec.visibility_of_all_elements_located(locator))
        except ValueError:
            return [self.wait.until(ec.visibility_of_element_located(locator))]

    def find_visible_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Explicitly waits until an element located by provided locator is visible and then return WebElement object.
        """
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except ValueError:
            return self.wait.until(ec.visibility_of_element_located(locator))
