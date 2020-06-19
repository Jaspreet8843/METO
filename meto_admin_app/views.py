from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import staff,worker,assign,date
from meto_user_app.models import user, booking, service, recovery, feedback
from .validator import valid_login
from datetime import datetime

# Create your views here.
def admin_index(request):
	if request.session.has_key('staff_id'):
		staff_obj = staff.objects.get(staff_id=request.session['staff_id'])
		return render(request,'management/admin_home.html',({'staff':staff_obj}))
	return redirect('admin_login')

def admin_login(request) :
	if request.session.has_key('staff_id'):
		return redirect('admin_index')
	else:
		if request.method=='POST':
			staff_phone = request.POST.get('staff_phone')
			staff_password = request.POST.get('staff_password')
			if valid_login(staff_phone,staff_password):
				print(True)
				try:
					staff_obj = staff.objects.get(staff_phone=staff_phone)
					s_id = staff_obj.staff_id
					db_password = staff_obj.staff_password
					# staff_hash_password=str(staff_hash_password)
					# staff_hash_password=staff_hash_password[2:len(staff_hash_password)-1]
					# check_pass = bcrypt.checkpw(staff_password.encode('utf8'),bytes(staff_hash_password,'utf-8'))
					if staff_password==db_password:
						request.session['staff_id']=s_id
						return redirect('admin_index')
					else:
						print("Incorrect Password")
						return redirect('admin_login')
				except Exception as e:
					print(e)
					print("User doesn't exist")
					return redirect('admin_login')
			else:
				print(False)
				print("Invalid entries")
				return redirect('admin_login')
		return render(request,'management/admin_login.html')

def admin_logout(request):
	del request.session['staff_id']
	return redirect('admin_login')

def assign_worker(request,service_id):
	if request.method=='POST':
		worker_id = request.POST.get('worker_id')
		booking_id = request.POST.get('booking_id')
		visiting_date = request.POST.get('visiting_date')
		technician_assigned_date = datetime.now().strftime('%Y-%m-%d')
		worker_obj = worker.objects.get(worker_id=worker_id)
		booking_obj = booking.objects.get(booking_id=booking_id)
		assign_obj = assign(worker_id=worker_obj,booking_id=booking_obj)
		date_obj = date.objects.filter(booking_id=booking_obj)
		date_obj.update(visiting_date=visiting_date,technician_assigned_date=technician_assigned_date)
		return HttpResponse("assigned")
	service_obj = service.objects.get(service_id=service_id)
	booking_obj = booking.objects.filter(service_id=service_obj,booking_status="Processing")
	worker_obj = worker.objects.filter(service_id=service_obj)
	return render(request,'management/assign_worker.html',({'bookings':booking_obj,'workers':worker_obj}))

def workers(request):
	worker_obj = worker.objects.all()
	# return render(request,'management/workers.html',({'workers':worker_obj}))
	return HttpResponse("all workers")

def assign_staff(request):
	if request.method=='POST':
		booking_id = request.POST.get('booking_id')
		staff_id = request.POST.get('staff_id')
		staff_assigned_date = datetime.now().strftime('%Y-%m-%d')
		booking_obj = booking.objects.get(booking_id=booking_id)
		staff_obj = booking.objects.get(staff_id=staff_id)
		assign_obj = assign(booking_id=booking_obj,staff_id=staff_obj)
		date_obj = date.objects.filter(booking_id=booking_obj)
		date_obj.update(staff_assigned_date=staff_assigned_date)
		return HttpResponse("assigned")
	booking_obj = booking.objects.all()
	staff_obj = staff.objects.all()
	# return render(request,'management/assign_staff.html',({'bookings':booking_obj,'staffs':staff_obj}))
	return HttpResponse("assign staff")