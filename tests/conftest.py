import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session")
def init_browser():

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	# options.add_argument("--headless")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.page_load_strategy = "eager"
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option("useAutomationExtension", False)

	browser.config.driver_options = options
	yield browser
	browser.close()
