from django.shortcuts import render,redirect
from django.http import HttpResponse
from meto_admin_app.models import user,service,booking,staff,worker

# Create your views here.
def login(request):
	return render(request,'customer/login.html')

def signup(request):
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



