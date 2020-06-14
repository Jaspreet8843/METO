def valid_login(phone,password):
	try:
		if len(phone) == 10:
			phone = int(phone)
			phone = True
		if len(password) >=8 and len(password) <= 20:
			password = True
		if phone == True and password == True:
			return True
		return False
	except:
		return False

def valid_signup(name,email,phone,password):
	try:
		if len(phone) == 10:
			phone = int(phone)
			phone = True
		if len(password) >=8 and len(password) <= 20:
			password = True
		if phone == True and password == True and email == True and name == True:
			return True
		return False
	except:
		return False