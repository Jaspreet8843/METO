import re

def valid_login(phone,password):
	try:
		phone_regex = '[0-9]{10}'
		if re.search(phone_regex,phone) and len(password) >=8 and len(password) <= 20:
			return True
		return False
	except:
		return False

def valid_signup(name,email,phone,password):
	try:
		name_regex = '[a-zA-Z ]{2,50}'
		email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
		phone_regex = '[0-9]{10}'
		if re.search(name_regex,name) and re.search(email_regex,email) and re.search(phone_regex,phone) and len(password) >=8 and len(password) <= 20:
			return True
		return False
	except:
		return False

def valid_details(name,phone,email,gender,area,city,pincode,old_pass,new_pass):
	try:
		info_ps = False
		add_ps = False
		psd_ps = False
		name_regex = '[a-zA-Z ]{2,50}'
		phone_regex = '[0-9]{10}'
		email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
		city_regex = '[a-zA-Z ]{2,30}'
		pincode_regex = '[0-9]{6}'
		if re.search(name_regex,name) and re.search(email_regex,email) and re.search(phone_regex,phone):
			info_ps=True
		if len(city)>0 and len(pincode)>0:
			if re.search(city_regex,city) and re.search(pincode_regex,pincode):
				add_ps=True
		if len(old_pass) >=8 and len(old_pass) <= 20 and len(new_pass) >=8 and len(new_pass) <= 20:
			psd_ps = True
		if len(old_pass)==0:
			psd_ps=True
		if info_ps and add_ps and psd_ps:
			return True
		return False
	except:
		return False

def valid_booking(pincode,phone):
	try:
		pincode_regex = '[0-9]{6}'
		phone_regex = '[0-9]{10}'
		if re.search(pincode_regex,pincode) and re.search(phone_regex,phone):
			return True
		return False
	except:
		return False