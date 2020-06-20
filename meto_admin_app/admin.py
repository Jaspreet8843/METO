from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(staff)
admin.site.register(worker)
admin.site.register(assign_staff)
admin.site.register(assign_worker)
admin.site.register(date)