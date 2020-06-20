from django.urls import path
from . import views

urlpatterns = [
	path('',views.admin_index,name="admin_index"),
	path('admin_login/',views.admin_login,name="admin_login"),
	path('admin_logout/',views.admin_logout,name="admin_logout"),
	path('assign_worker/<int:service_id>',views.assign_workers,name="assign_workers"),
	path('assign_staff/',views.assign_staffs,name="assign_staff"),
	path('assign_worker/<int:worker_id>/<int:booking_id>',views.assign_worker_to_booking,name="assign_worker_to_booking"),
	path('workers/',views.workers,name="workers"),
]