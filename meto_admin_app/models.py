from django.db import models
from meto_user_app.models import service
from django.utils import timezone


class staff(models.Model):
	staff_id=models.CharField(max_length=255, primary_key=True)
	staff_name=models.CharField(max_length=255)
	staff_phone=models.CharField(max_length=255,unique=True)
	staff_city=models.CharField(max_length=255)
	staff_pincode=models.CharField(max_length=255)
	staff_job_status=models.CharField(max_length=255)

class worker(models.Model):
	service_id=models.ForeignKey(service, on_delete=models.CASCADE)
	worker_id=models.CharField(max_length=255, primary_key=True)
	worker_name=models.CharField(max_length=255)
	worker_phone=models.CharField(max_length=255,unique=True)
	worker_city=models.CharField(max_length=255)
	worker_pincode=models.CharField(max_length=255)

