from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user,service,booking
from meto_admin_app.models import staff,worker

# Create your views here.
def login(request):
	if request.session.has_key('user_id'):
		return redirect('index')
	else:
		if request.method=='POST':
			user_phone = request.POST.get('login_phone')
			user_pass = request.POST.get('login_pass')
		return render(request,'customer/login.html')

def signup(request):
	if request.session.has_key('user_id'):
		return redirect('index')
	else:
		if request.method=='POST':
			user_name = request.POST.get('new_name')
			user_email = request.POST.get('new_email')
			user_phone = request.POST.get('new_phone')
			user_pass = request.POST.get('new_pass')
		return HttpResponse("Under construction")

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



