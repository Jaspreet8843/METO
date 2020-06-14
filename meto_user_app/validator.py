import re

def valid_login(phone,password):
	try:
		phone_regex = '[0-9]{10}'
		if re.search(phone_regex,phone):
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
		name_regex = '[a-zA-Z ]'
		email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
		phone_regex = '[0-9]{10}'
		if re.search(name_regex,name):
			name =  True
		if re.search(email_regex,email):
			email = True
		if re.search(phone_regex,phone):
			phone = True
		if len(password) >=8 and len(password) <= 20:
			password = True
		if phone == True and password == True and email == True and name == True:
			return True
		return False
	except:
		return False