from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="index"),
	path('login/',views.login,name="login"),
	path('profile/',views.profile,name="profile"),
	path('edit_profile/',views.edit_profile,name="edit_profile"),
	path('bookings/',views.bookings,name="bookings"),
	path('book/<int:service_id>',views.book,name="book"),
	path('feedback/',views.feedback,name="feedback"),
	path('about/',views.about,name="about"),
]