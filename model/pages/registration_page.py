from selene import have


class RegistrationPage:
	def __init__(self, browser):
		self.__browser = browser

	def open_form(self):
		self.__browser.open("https://demoqa.com/automation-practice-form")
		self.__browser.execute_script("$('#fixedban').remove()")
		self.__browser.execute_script("$('footer').remove()")
		return self


	def fill_first_name(self, value):
		self.__browser.element('[id=firstName]').type(value)
		return self

	def fill_last_name(self, value):
		self.__browser.element('[id=lastName]').type(value)
		return self

	def fill_user_email(self, value):
		self.__browser.element('[id=userEmail]').type(value)
		return self

	def select_gender(self, value):
		self.__browser.element(f"input[value='{value}'] + label").click()
		return self

	def fill_user_mobile_number(self, value):
		self.__browser.element('[id=userNumber]').type(value)
		return self

	def select_birthday(self, values:list):
		year = values[2]
		month = values[1]
		day = values[0]
		# Выбор даты рождения
		self.__browser.element('[id=dateOfBirthInput]').click()
		# Выбор года
		self.__browser.element(f"[value='{year}']").click()
		# Выбор месяца:
		self.__browser.element(".react-datepicker__month-select").element(
			f"//option[text()='{month}']").click()
		# Выбор дня:
		self.__browser.element(f".react-datepicker__day--0{day}").click()

		return self

	def type_subjects(self):
		self.__browser.element('input[id = subjectsInput]').type("Com").press_enter().type("Eng").press_enter()
		return self

	def select_hobbies(self):
		self.__browser.element('[for=hobbies-checkbox-2]').click()
		return self

	def upload_file(self, path):
		self.__browser.element("#uploadPicture").send_keys(path)
		return self

	def type_current_address(self,):
		self.__browser.element("#currentAddress").type(f"{self.__browser.driver.current_url}")
		return self

	def select_state(self, value):
		self.__browser.element('#state input').type(value).press_enter()
		return self

	def select_city(self, value):
		self.__browser.element('#city input').type(value).press_enter()
		return self

	def press_submit(self):
		self.__browser.element('#submit').click()
		return self

	def should_person_info(self, person_info):
		self.__browser.element(".table-responsive").all("td").should(have.exact_texts(person_info))
