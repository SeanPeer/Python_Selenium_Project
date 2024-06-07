from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException


class SafeFunctions:
    def __init__(self, site):
        self.driver = DriverFactory.get_driver()
        self.driver.get(f'http://{site}/')

    def safe_click(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return True
        except (TimeoutException, ElementClickInterceptedException, ElementNotInteractableException) as e:
            print(f"Error clicking element: {e}")
            return False

    def safe_read(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error reading element: {e}")
            return None

    def safe_insert_keys(self, locator, keys, timeout=10):
        """
        Attempts to insert keys into an element identified by the given locator within the specified timeout.

        :param locator: A tuple of (By, locator) to identify the element.
        :param keys: The keys to send to the element.
        :param timeout: Maximum time to wait for the element to be interactable.
        :return: True if keys are successfully inserted, False otherwise.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.clear()
            element.send_keys(keys)
            return True
        except (TimeoutException, ElementNotInteractableException, NoSuchElementException) as e:
            print(f"Error inserting keys: {e}")
            return False
