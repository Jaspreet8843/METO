from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user,service,booking
from meto_admin_app.models import staff,worker
from .validator import valid_login,valid_signup,valid_details
import bcrypt

# Create your views here.
def login(request):
	if request.session.has_key('user_id'):
		return redirect('index')
	else:
		if request.method=='POST':
			user_phone = request.POST.get('login_phone')
			user_password = request.POST.get('login_pass')
			if valid_login(user_phone,user_password):
				print(True)
				try:
					user_obj = user.objects.get(user_phone=user_phone)
					u_id = user_obj.user_id
					user_hash_password = user_obj.user_password
					user_hash_password=str(user_hash_password)
					user_hash_password=user_hash_password[2:len(user_hash_password)-1]
					check_pass = bcrypt.checkpw(user_password.encode('utf8'),bytes(user_hash_password,'utf-8'))
					print("check",check_pass)
					if check_pass:
						request.session['user_id']=u_id
						return redirect('index')
					else:
						print("Incorrect Password")
						return redirect('login')
				except Exception as e:
					print(e)
					print("User doesn't exist")
					return redirect('login')
			else:
				print(False)
				print("Invalid entries")
				return redirect('login')
		return render(request,'customer/login.html')

def signup(request):
	if request.session.has_key('user_id'):
		return redirect('index')
	else:
		if request.method=='POST':
			user_name = request.POST.get('new_name')
			user_email = request.POST.get('new_email')
			user_phone = request.POST.get('new_phone')
			user_password = request.POST.get('new_pass')
			if valid_signup(user_name,user_email,user_phone,user_password):
				print(True)
				user_hash_password = bcrypt.hashpw(user_password.encode('utf8'),bcrypt.gensalt())
				try:
					user_obj = user(user_name=user_name,user_email=user_email,user_phone=user_phone,
						user_password=user_hash_password)
					user_obj.save()
					user_obj = user.objects.get(user_phone=user_phone)
					u_id = user_obj.user_id
					request.session['user_id']=u_id
					return redirect('index')
				except Exception as e:
					print(e)
					print("Failed query")
					return redirect('signup')
			else:
				print(False)
				print("Invalid entries")
				return redirect('signup')
		return render(request,'customer/login.html')

def logout(request):
	del request.session['user_id']
	return redirect('index')

def index(request):
	if request.session.has_key('user_id'):
		user_obj = user.objects.get(user_id=request.session['user_id'])
		return render(request,'customer/index.html',({'user':user_obj}))
	return render(request,'customer/index.html')

def profile(request):
	if request.session.has_key('user_id'):
		user_obj = user.objects.get(user_id=request.session['user_id'])
		return render(request,'customer/profile.html',({'user':user_obj}))
	return redirect('index')

def edit_profile(request):
	if request.session.has_key('user_id'):
		if request.method=='POST':
			user_name = request.POST.get('user_name')
			user_phone = request.POST.get('user_phone')
			user_email = request.POST.get('user_email')
			user_gender = request.POST.get('user_gender')
			user_area = request.POST.get('user_area')
			user_city = request.POST.get('user_city')
			user_pincode = request.POST.get('user_pincode')
			user_old_pass = request.POST.get('user_old_pass')
			user_new_pass = request.POST.get('user_new_pass')
			user_obj = user.objects.get(user_id=request.session['user_id'])
			if valid_details(user_name,user_phone,user_email,user_gender,user_area,
				user_city,user_pincode,user_old_pass,user_new_pass,user_obj):
				print(True)
				return HttpResponse("Under construction")
			return HttpResponse("Under construction")
		else:
			user_obj = user.objects.get(user_id=request.session['user_id'])
			return render(request,'customer/edit_profile.html',({'user':user_obj}))
	return redirect('index')

def book(request,service_id):
	return HttpResponse("Under construction")

def bookings(request):
	return render(request,'customer/bookings.html')

def book_ticket(request):
    return render(request, 'customer/book_ticket.html')

def feedback(request):
	return HttpResponse("Under construction")

def about(request):
	return HttpResponse("Under construction")



