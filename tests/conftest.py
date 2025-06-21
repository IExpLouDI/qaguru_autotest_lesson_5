import pytest
from selene import browser
from selenium import webdriver

from test_data.users import UserInfo


@pytest.fixture(scope="session")
def init_browser():

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	# options.add_argument("--headless")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option("useAutomationExtension", False)

	browser.config.driver_options = options
	yield browser
	browser.close()


# @pytest.fixture(scope='function')
# def case_data():
# 	user = UserInfo().get_user()
# 	user_birthday = user["birthDay"].split()
# 	# Check_filling_form
# 	check_result = [
# 		'Student Name', user["firstName"] + " " + user["lastName"],
# 		'Student Email', user["userEmail"],
# 		'Gender', user["gender"],
# 		'Mobile', user["mobile_phone"],
# 		'Date of Birth', f'{user_birthday[0]} {user_birthday[1]},{user_birthday[2]}',
# 		'Subjects', 'Computer Science, English',
# 		'Hobbies', 'Reading',
# 		'Picture', 'picture.jpg',
# 		'Address', 'https://demoqa.com/automation-practice-form',
# 		'State and City', " ".join([user["state"], user["city"]])
# 	]
#
# 	return {"test": user,
# 			"check": check_result}
