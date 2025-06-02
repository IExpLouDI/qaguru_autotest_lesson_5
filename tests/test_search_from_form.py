from selene import have
import os


def test_insert_personal_data(site, data):
	site.execute_script("$('#fixedban').remove()")
	site.execute_script("$('footer').remove()")
	location = list(data["test"]["location"].items())[0]

	site.element('[id=firstName]').type(data["test"]["firstName"])
	site.element('[id=lastName]').type(data["test"]["lastName"])
	site.element('[id=userEmail]').type(data["test"]["userEmail"])
	site.element(f"input[value='{data['test']['gender']}'] + label").click()
	site.element('[id=userNumber]').type(data["test"]['mobile_phone'])

	# Выбор даты рождения
	site.element('[id=dateOfBirthInput]').click()
	# Выбор года
	site.element(f"[value='{data['test']['birthDay'].split()[2]}']").click()
	# Выбор месяца:
	site.element(".react-datepicker__month-select").element(f"//option[text()='{data['test']['birthDay'].split()[1]}']").click()
	# Выбор дня:
	site.element(f".react-datepicker__day--0{data['test']['birthDay'].split()[0]}").click()

	site.element('input[id = subjectsInput]').type("Com").press_enter().type("Eng").press_enter()
	site.element('[for=hobbies-checkbox-2]').click()
	site.element("#uploadPicture").send_keys(os.path.abspath("../files/picture.jpg"))
	site.element("#currentAddress").type(f"{site.driver.current_url}")
	site.element('#state input').type(location[0]).press_enter()
	site.element('#city input').type(location[1]).press_enter()
	site.element('#submit').click()

	site.element(".table-responsive").all("td").should(have.exact_texts(data["check"]))
