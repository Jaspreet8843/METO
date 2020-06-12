from django.shortcuts import render
from django.http import HttpResponse
from .models import staff,worker
from meto_user_app.models import user, booking,service

# Create your views here.
def index(request):
	return render(request,'admin_home.html')

def login(request) :
	return render(request,'admin_login.html')