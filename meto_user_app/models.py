from django.db import models
from django.utils import timezone

class user(models.Model):
    user_id=models.CharField(max_length=255,primary_key=True)
    user_name=models.CharField(max_length=255)
    user_password=models.CharField(max_length=255)
    user_dp=models.CharField(max_length=255,blank=True)
    user_email=models.CharField(max_length=255,unique=True)
    user_phone=models.CharField(max_length=255,unique=True)
    user_gender=models.CharField(max_length=255,default=None)
    user_area=models.CharField(max_length=255,blank=True)
    user_city=models.CharField(max_length=255,blank=True)
    user_pincode=models.CharField(max_length=255,blank=True)
    user_since=models.DateField(default=timezone.now)

class service(models.Model):
	service_id=models.CharField(max_length=255,primary_key=True)
	service_name=models.CharField(max_length=255)
	service_status=models.CharField(max_length=255,default="Available")

class booking(models.Model):
	booking_id=models.CharField(max_length=255,primary_key=True)
	user_id=models.ForeignKey(user, related_name='user', on_delete=models.CASCADE)
	service_id=models.ForeignKey(service, on_delete=models.CASCADE)
	booking_date=models.DateField(default=timezone.now)
	booking_desc=models.CharField(max_length=255,blank=True)
	booking_phone=models.CharField(max_length=255)
	booking_area=models.CharField(max_length=255)
	booking_city=models.CharField(max_length=255)
	booking_pincode=models.CharField(max_length=255)
	booking_status=models.CharField(max_length=255,default="Processing")
	staff_id=models.ForeignKey('meto_admin_app.staff', related_name='staff', on_delete=models.CASCADE, blank=True)
	worker_id=models.ForeignKey('meto_admin_app.worker', related_name='worker',on_delete=models.CASCADE, blank=True)
