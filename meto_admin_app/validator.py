import re

def valid_login(phone,password):
	try:
		phone_regex = '[0-9]{10}'
		if re.search(phone_regex,phone) and len(password) >=8 and len(password) <= 20:
			return True
		return False
	except:
		return False