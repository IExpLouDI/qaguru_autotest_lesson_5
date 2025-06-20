from selene import browser


class RegistrationPage:
	def open_form(self):
		browser.open("/automation-practice-form")
		return self


	def fill_first_name(self, value):
		browser.element('[id=firstName]').type(value)
		return self

	def fill_last_name(self, value):
		browser.element('[id=firstName]').type(value)
		return self

	def fill_user_email(self, value):
		browser.element('[id=userEmail]').type(value)
		return self

	def select_gender(self, value):
		browser.element(f"input[value='{value}'] + label").click()
		return self

	def fill_user_mobile_number(self, value):
		browser.element('[id=userNumber]').type(value)
		return self

	def select_birthday(self, year, month, day):
		# Выбор даты рождения
		browser.element('[id=dateOfBirthInput]').click()
		# Выбор года
		browser.element(f"[value='{year}']").click()
		# Выбор месяца:
		browser.element(".react-datepicker__month-select").element(
			f"//option[text()='{month}']").click()
		# Выбор дня:
		browser.element(f".react-datepicker__day--0{day}").click()

		return self
