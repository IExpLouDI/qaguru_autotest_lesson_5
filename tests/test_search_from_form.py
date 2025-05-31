import selene
from selenium.webdriver.common.keys import Keys


def test_search(site):
	site.element('[id=firstName]').type("start")
	site.element('[id=lastName]').type("start2")
	site.element('[id=userEmail]').type("start3")
	site.element("input[value='Male'] + label").click()
	site.element('[id=userNumber]').type("7689334332")
	site.element('[id=dateOfBirthInput]').press(Keys.SHIFT + Keys.HOME).press(Keys.NUMPAD1).set_value("0.10.1999")
	site.element('input[id = subjectsInput]').type("Com").press_enter()
	site.element('input[id = subjectsInput]').type("Eng").press_enter()
