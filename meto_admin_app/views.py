from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import staff,worker,assign,date
from meto_user_app.models import user, booking, service, recovery, feedback
from .validator import valid_login

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