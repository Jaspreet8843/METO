from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(user)
admin.site.register(service)
admin.site.register(dates)
admin.site.register(booking)

