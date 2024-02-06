from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _find_collection(self, locator: tuple) -> list:
        return self._driver.find_elements(*locator)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_clickable(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _move_to_element(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))
        actions = ActionChains(self._driver)
        element_to_move = self._find(locator)
        actions.move_to_element(element_to_move).perform()

    def _switch_to_new_tab(self):
        self._driver.switch_to.window(self._driver.window_handles[-1])
