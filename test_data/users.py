from random import randint, choice


class UserInfo:

	def __init__(self):
		self.user_info = self.get_user()


	@property
	def state(self):
		states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
		return choice(states)


	def city(self, state):

		city_dict = {
			"NCR": ("Delhi", "Gurgaon", "Noida"),
			"Uttar Pradesh": ("Agra", "Lucknow", "Merrut"),
			"Haryana": ("Karnal", "Panipat"),
			"Rajasthan": ("Jaipur", "Jaiselmer")
		}

		return city_dict[state][randint(0, len(city_dict[state]) - 1)]

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
		state = self.state
		city = self.city(state)
		# location = self.city
		birthday = "01 " + self.month + " " + str(self.year)

		if gender == "Male":
			return {"firstName": "Игорь",
					"lastName": "Тестов",
					"userEmail": "test@mail.ru",
					"gender": "Male",
					"birthDay": birthday,
					"mobile_phone": "8989567453",
					"city": city,
					"state": state
					}
		elif gender == "Female":
			return {"firstName": "Лара",
					"lastName": "Тестова",
					"userEmail": "lara_t@mail.ru",
					"gender": "Female",
					"birthDay": birthday,
					"mobile_phone": "8939777453",
					"city": city,
					"state": state
					}
		else:
			return {"firstName": "Пользователь",
					"lastName": "Неопределён",
					"userEmail": "secret_g@mail.ru",
					"gender": "Other",
					"birthDay": birthday,
					"mobile_phone": "8939777666",
					"city": city,
					"state": state
					}