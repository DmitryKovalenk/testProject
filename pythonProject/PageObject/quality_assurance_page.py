from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PageObject.base_page import BasePage


class QualityAssurancePage(BasePage):
    __url = "https://useinsider.com/careers/quality-assurance/"
    __get_a_demo_button_locator = (By.XPATH, "//a[text()='Get a Demo']")
    __accept_all_button = (By.ID, 'wt-cli-accept-all-btn')
    __see_all_QA_jobs_button_locator = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    __filter_by_location_locator = (By.ID, "select2-filter-by-location-container")
    __filter_by_department_locator = (By.ID, "select2-filter-by-department-container")
    __position_locator = (By.XPATH, "//div[@id='jobs-list']//p")
    __role_locator = (By.XPATH, "//div[@id='jobs-list']//p/following-sibling::span")
    __location_locator = (By.XPATH, "//div[@id='jobs-list']//p/following-sibling::div")
    __view_role_button_locator = (By.XPATH, "(//div[@class='position-list-item-wrapper bg-light'])[1]/a")
    __first_element = (By.XPATH, "(//div[@class='position-list-item-wrapper bg-light'])[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
        super()._click(self.__accept_all_button)
        super()._is_displayed(self.__get_a_demo_button_locator)

    def open_tab(self):
        super()._move_to_element(self.__see_all_QA_jobs_button_locator)
        super()._click(self.__see_all_QA_jobs_button_locator)

    def apply_filters(self, location, department):
        sleep(2)
        super()._click(self.__filter_by_location_locator)
        attempts = 0
        while attempts < 2:
            try:
                super()._click((By.XPATH, f"//span[@class='select2-results']/ul/li[contains(text(),'{location}')]"))
                break
            except:
                super()._click(self.__filter_by_location_locator)
                super()._click(self.__filter_by_location_locator)
                attempts += 1
        super()._click(self.__filter_by_department_locator)
        super()._click((By.XPATH, f"//span[@class='select2-results']/ul/li[contains(text(),'{department}')]"))
        sleep(2)

    def get_list_of_positions(self) -> list:
        my_elements = super()._find_collection(self.__position_locator)
        list_of_positions = []
        for el in my_elements:
            value = el.text
            list_of_positions.append(value)
        return list_of_positions

    def is_all_quality_assurance(self) -> bool:
        my_elements = super()._find_collection(self.__role_locator)
        list_of_roles = []
        for el in my_elements:
            value = el.text
            list_of_roles.append(value)
        return all('Quality Assurance' == list_of_roles[0] for el in list_of_roles)

    def is_all_location_istanbul(self) -> bool:
        my_elements = super()._find_collection(self.__location_locator)
        list_of_locations = []
        for el in my_elements:
            value = el.text
            list_of_locations.append(value)
        return all('Istanbul, Turkey' == list_of_locations[0] for el in list_of_locations)

    def open_view_role(self):
        super()._move_to_element(self.__first_element)
        super()._click(self.__view_role_button_locator)

    def verify_new_url(self) -> str:
        super()._switch_to_new_tab()
        return super().current_url
