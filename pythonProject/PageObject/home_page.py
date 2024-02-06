from selenium.webdriver.remote.webdriver import WebDriver
from PageObject.base_page import BasePage


class HomePage(BasePage):
    __url = "https://useinsider.com/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    @property
    def expected_url(self) -> str:
        return self.__url
