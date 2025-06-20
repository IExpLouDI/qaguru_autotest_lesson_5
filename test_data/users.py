from random import randint, choice


class UserInfo:

	def __init__(self):
		self.user_info = self.get_user()


	@property
	def state(self):
		states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
		return choice(states)

	@property
	def city(self, state=state):
		city_dict = {
			"NCR": ("Delhi", "Gurgaon", "Noida"),
			"Uttar Pradesh": ("Agra", "Lucknow", "Merrut"),
			"Haryana": ("Karnal", "Panipat"),
			"Rajasthan": ("Jaipur", "Jaiselmer")
		}

		city = city_dict[state][randint(0, len(city_dict[state]) - 1)]
		return {state: city, "check": state + " " + city}

	@property
	def gender(self):
		return choice(["Male", "Female", "Other"])

	@property
	def month(self):
		return choice(["January", "February", "March",
							  "April", "May", "June", "July",
							  "August", "September", "October",
							  "November", "December"])
	@property
	def year(self):
		return randint(1900, 2100)

	def get_user(self):
		gender = self.gender
		location = self.city
		birthday = "01 " + self.month + " " + str(self.year)

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