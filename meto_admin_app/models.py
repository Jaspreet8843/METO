from django.db import models
from meto_user_app.models import service,booking
from django.utils import timezone


class staff(models.Model):
	staff_id=models.AutoField(primary_key=True)
	staff_name=models.CharField(max_length=255)
	staff_phone=models.CharField(max_length=255,unique=True)
	staff_area = models.CharField(max_length=255)
	staff_city=models.CharField(max_length=255)
	staff_pincode=models.CharField(max_length=255)
	staff_job_status=models.CharField(max_length=255)

class worker(models.Model):
	service_id=models.ForeignKey(service, on_delete=models.CASCADE,default=1)
	worker_id=models.AutoField(primary_key=True)
	worker_name=models.CharField(max_length=255)
	worker_phone=models.CharField(max_length=255,unique=True)
	worker_area = models.CharField(max_length=255)
	worker_city=models.CharField(max_length=255)
	worker_pincode=models.CharField(max_length=255)

class assign(models.Model):
	booking_id=models.ForeignKey(booking,related_name='booking',on_delete=models.CASCADE,default=1)
	staff_id=models.ForeignKey(staff, related_name='staff', on_delete=models.CASCADE,default=1)
	worker_id=models.ForeignKey(worker, related_name='worker',on_delete=models.CASCADE,default=1)