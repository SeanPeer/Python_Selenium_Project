from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverFactory:
    @staticmethod
    def get_driver(browser_name='chrome'):
        if browser_name.lower() == 'chrome':
            service = Service(
                'C:/Users/seanp/PycharmProjects/SeleniumPythonProject/pythonProject1/utils/chromedriver.exe')
            return webdriver.Chrome(service=service)
