from django.shortcuts import render
from django.http import HttpResponse
from .models import staff,worker
from meto_user_app.models import user, booking,service

# Create your views here.
def admin_index(request):
	return render(request,'management/admin_home.html')

def admin_login(request) :
	return render(request,'management/admin_login.html')