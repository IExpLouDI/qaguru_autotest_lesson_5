from selene import be, have
from selenium.webdriver.common.keys import Keys
import os


def test_search(site, get_user_date):
	site.execute_script("$('#fixedban').remove()")
	site.execute_script("$('footer').remove()")
	location = list(get_user_date["location"].items())[0]

	site.element('[id=firstName]').type(get_user_date["firstName"])
	site.element('[id=lastName]').type(get_user_date["lastName"])
	site.element('[id=userEmail]').type(get_user_date["userEmail"])
	site.element(f"input[value='{get_user_date['gender']}'] + label").click()
	site.element('[id=userNumber]').type(get_user_date['mobile_phone'])
	# site.element('[id=dateOfBirthInput]').press(Keys.SHIFT + Keys.HOME).press(Keys.NUMPAD0).set_value(get_user_date['birthDay'])

	# Выбор даты рождения
	site.element('[id=dateOfBirthInput]').click()
	# Выбор года
	site.element(f"[value='{get_user_date['birthDay'].split()[2]}']").click()
	# Выбор месяца:
	site.element(".react-datepicker__month-select").element(f"//option[text()='{get_user_date['birthDay'].split()[1]}']").click()
	# Выбор дня:
	site.element(f".react-datepicker__day--0{get_user_date['birthDay'].split()[0]}").click()

	site.element('input[id = subjectsInput]').type("Com").press_enter().type("Eng").press_enter()
	site.element('input[id=hobbies-checkbox-2] ~ label').click()
	site.element("#uploadPicture").send_keys(os.path.abspath("../files/picture.jpg"))
	site.element("#currentAddress").type(f"{site.driver.current_url}")
	site.element('#state input').type(location[0]).press_enter()
	site.element('#city input').type(location[1]).press_enter()
	site.element('#submit').click()

	site.element(".table-responsive").all("td").should(have.exact_text(get_user_date["firstName"]))
	print(1)
