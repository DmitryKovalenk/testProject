import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session', autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' ot 'firefox', but got {browser}")
    my_driver.implicitly_wait(10)
    my_driver.maximize_window()
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to execute tests (chrome, firefox)"
    )
