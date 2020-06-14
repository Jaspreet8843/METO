from django.urls import path
from . import views

urlpatterns = [
	path('',views.admin_index,name="admin_index"),
	path('admin_login/',views.admin_login,name="admin_login"),
]