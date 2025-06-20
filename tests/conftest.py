import pytest
from selene import browser
from selenium import webdriver
import random


@pytest.fixture(scope="session")
def init_browser():
	# browser.config.driver_name = 'firefox'

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	# options.add_argument("--headless")
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


def get_state():
	states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
	return states[random.randint(0, len(states) - 1)]


def get_city(state):
	city_dict = {
		"NCR": ("Delhi", "Gurgaon", "Noida"),
		"Uttar Pradesh": ("Agra", "Lucknow", "Merrut"),
		"Haryana": ("Karnal", "Panipat"),
		"Rajasthan": ("Jaipur", "Jaiselmer")
    }

	city = city_dict[state][random.randint(0, len(city_dict[state]) - 1)]
	return {state: city, "check": state + " " + city}


def get_gender():
	return random.choice(["Male", "Female", "Other"])


def get_month():
	return random.choice(["January", "February", "March",
						  "April", "May", "June", "July",
						  "August", "September", "October",
						  "November", "December"])


def get_year():
	return random.randint(1900, 2100)


def get_user_date():
	gender = get_gender()
	location = get_city(get_state())
	birthday = "01 " + get_month() + " " + str(get_year())

	if gender == "Male":
		return {"firstName": "Игорь",
				"lastName": "Тестов",
				"userEmail": "test@mail.ru",
				"gender": "Male",
				"birthDay": birthday,
				"mobile_phone": "8989567453",
				"location": location
				}
	elif gender == "Female":
		return {"firstName": "Лара",
				"lastName": "Тестова",
				"userEmail": "lara_t@mail.ru",
				"gender": "Female",
				"birthDay": birthday,
				"mobile_phone": "8939777453",
				"location": location
				}
	else:
		return {"firstName": "Пользователь",
				"lastName": "Неопределён",
				"userEmail": "secret_g@mail.ru",
				"gender": "Other",
				"birthDay": birthday,
				"mobile_phone": "8939777666",
				"location": location
				}


@pytest.fixture(scope='function')
def data():
	# Create person data
	person = get_user_date()
	person_date = person["birthDay"].split()
	# Check_filling_form
	check_result = [
		'Student Name', person["firstName"] + " " + person["lastName"],
		'Student Email', person["userEmail"],
		'Gender', person["gender"],
		'Mobile', person["mobile_phone"],
		'Date of Birth', f'{person_date[0]} {person_date[1]},{person_date[2]}',
		'Subjects', 'Computer Science, English',
		'Hobbies', 'Reading',
		'Picture', 'picture.jpg',
		'Address', 'https://demoqa.com/automation-practice-form',
		'State and City', person["location"]["check"]
		]

	return {"test": person,
			"check": check_result}
