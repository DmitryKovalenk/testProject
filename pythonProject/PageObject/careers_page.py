from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObject.base_page import BasePage


class CareersPage(BasePage):
    __company_navigation_menu_locator = (By.XPATH, "//ul[@class='navbar-nav']/li/a[contains(text(),'Company')]")
    __careers_menu_locator = (By.XPATH, "//a[contains(text(),'Careers')]")
    __our_locations_locator = (By.XPATH, "//h3[contains(text(),'Our Locations')]")
    __see_all_teams_button_locator = (By.XPATH, "//a[contains(text(), 'See all teams')]")
    __life_at_insider_locator = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_tab(self):
        super()._click(self.__company_navigation_menu_locator)
        super()._click(self.__careers_menu_locator)

    def is_block_our_locations_displayed(self) -> bool:
        return super()._is_displayed(self.__our_locations_locator)

    def is_button_see_all_teams_displayed(self) -> bool:
        return super()._is_displayed(self.__see_all_teams_button_locator)

    def is_life_at_insider_displayed(self) -> bool:
        return super()._is_displayed(self.__life_at_insider_locator)
