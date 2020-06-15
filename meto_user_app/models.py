from django.db import models
from django.utils import timezone

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=255)
    user_password=models.CharField(max_length=255)
    user_dp=models.CharField(max_length=255,blank=True)
    user_email=models.CharField(max_length=255,unique=True)
    user_phone=models.CharField(max_length=255,unique=True)
    user_gender=models.CharField(max_length=255,blank=True)
    user_area=models.CharField(max_length=255,blank=True)
    user_city=models.CharField(max_length=255,blank=True)
    user_pincode=models.CharField(max_length=255,blank=True)
    user_since=models.DateField(default=timezone.now)

class service(models.Model):
	service_id=models.IntegerField(primary_key=True)
	service_name=models.CharField(max_length=255)
	service_status=models.CharField(max_length=255,default="Available")

class booking(models.Model):
	booking_id=models.AutoField(primary_key=True)
	user_id=models.ForeignKey(user, related_name='user', on_delete=models.CASCADE,default=1)
	service_id=models.ForeignKey(service, related_name='service',on_delete=models.CASCADE,default=1)
	booking_date=models.DateField(default=timezone.now)
	booking_desc=models.CharField(max_length=255,blank=True)
	booking_phone=models.CharField(max_length=255)
	booking_area=models.CharField(max_length=255)
	booking_city=models.CharField(max_length=255)
	booking_pincode=models.CharField(max_length=255)
	booking_status=models.CharField(max_length=255,default="Processing")
