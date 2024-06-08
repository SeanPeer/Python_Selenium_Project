from selenium.webdriver.common.by import By

class LocatorMap:
    def __init__(self, locator_dict):
        for key, value in locator_dict.items():
            setattr(self, key, value)
