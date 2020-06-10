from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
	return render(request,'login.html')

def signup(request):
	return HttpResponse("Under construction")

def index(request):
	return render(request,'index.html')

def profile(request):
	return render(request,'profile.html')

def edit_profile(request):
	return render(request,'edit_profile.html')

def book(request,service_id):
	return HttpResponse("Under construction")

def bookings(request):
	return render(request,'bookings.html')

def feedback(request):
	return HttpResponse("Under construction")

def about(request):
	return HttpResponse("Under construction")



