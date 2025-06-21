from model.pages.registration_page import RegistrationPage
from utils.paths import PATH_PICTURE


def test_registration_page(case_data, init_browser):
	registration_page = RegistrationPage(init_browser)
	user = case_data["test"]
	should_result = case_data["check"]

	registration_page.open_form()

	# fill personal data
	registration_page.fill_first_name(user["firstName"])
	registration_page.fill_last_name(user["lastName"])
	registration_page.fill_user_email(user["userEmail"])
	registration_page.fill_user_mobile_number(user["mobile_phone"])
	registration_page.select_gender(user["gender"])

	registration_page.select_birthday(user["birthDay"].split())
	registration_page.type_subjects()
	registration_page.select_hobbies()
	registration_page.upload_file(PATH_PICTURE)
	registration_page.type_current_address()
	registration_page.select_state(user["state"])
	registration_page.select_city(user["city"])
	registration_page.press_submit()
	registration_page.should_person_info(should_result)
