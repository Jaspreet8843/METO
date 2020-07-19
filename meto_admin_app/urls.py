from django.urls import path
from . import views

urlpatterns = [
	path('',views.admin_index,name="admin_index"),
	path('admin_login/',views.admin_login,name="admin_login"),
	path('admin_logout/',views.admin_logout,name="admin_logout"),
	path('assign_worker/<int:service_id>',views.assign_workers,name="assign_workers"),
	path('assign_staff/',views.assign_staffs,name="assign_staff"),
	path('workers/',views.workers,name="workers"),
	path('all_bookings/',views.all_bookings,name="all_bookings"),
	path('service_delivered/<int:booking_id>',views.service_delivered,name="service_delivered"),
	path('ratings/',views.all_ratings,name="all_ratings"),
	path('googlea43fccb7d901a9b7.html/',views.verify,name="verify"),
]