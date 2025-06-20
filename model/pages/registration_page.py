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

	def

