import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session")
def init_browser():
	# browser.config.driver_name = 'firefox'

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option("useAutomationExtension", False)

	browser.config.driver_options = options
	yield browser
	browser.close()


@pytest.fixture(scope="function")
def site(init_browser):
	open_browser = browser.open("https://demoqa.com/automation-practice-form")
	return open_browser
