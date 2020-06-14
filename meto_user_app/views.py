from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user,service,booking
from meto_admin_app.models import staff,worker
from .validator import valid_login,valid_signup

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
				user_obj = user.objects.filter(user_phone=user_phone,user_password=user_password)
				if user_obj.exists():
					user_id = user_obj['user_id']
					request.session['user_id']=user_id
					return redirect('index')
			else:
				print(False)
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
				user_obj = user(user_name=user_name,user_email=user_email,user_phone=user_phone,
					user_password=user_password)
				user_obj.save()
				user_obj = user.objects.filter(user_phone=user_phone,user_password=user_password)
				user_id = user_obj['user_id']
				request.session['user_id']=user_id
				return redirect('index')
			else:
				print(False)
				return redirect('signup')
		return render(request,'customer/login.html')

def index(request):
	return render(request,'customer/index.html')

def profile(request):
	return render(request,'customer/profile.html')

def edit_profile(request):
	return render(request,'customer/edit_profile.html')

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



