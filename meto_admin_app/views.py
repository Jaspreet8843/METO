from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import staff, worker, assign_staff, assign_worker, date
from meto_user_app.models import user, booking, service, recovery, feedback
from .validator import valid_login
from datetime import datetime
from django.contrib import messages

# Create your views here.
def admin_index(request):
    if request.session.has_key('staff_id'):
        staff_obj = staff.objects.get(staff_id=request.session['staff_id'])
        service_obj = service.objects.all()
        count_dict = {}
        for i in service_obj:
            count_dict[i.service_id] = booking.objects.filter(service_id=i).count()
        # print(count_dict)
        return render(request, 'management/admin_home.html', ({'staff': staff_obj,'count':count_dict}))
    return redirect('admin_login')


def admin_login(request):
    if request.session.has_key('staff_id'):
        return redirect('admin_index')
    else:
        if request.method == 'POST':
            staff_phone = request.POST.get('staff_phone')
            staff_password = request.POST.get('staff_password')
            if valid_login(staff_phone, staff_password):
                # print(True)
                try:
                    staff_obj = staff.objects.get(staff_phone=staff_phone)
                    s_id = staff_obj.staff_id
                    db_password = staff_obj.staff_password
                    # staff_hash_password=str(staff_hash_password)
                    # staff_hash_password=staff_hash_password[2:len(staff_hash_password)-1]
                    # check_pass = bcrypt.checkpw(staff_password.encode('utf8'),bytes(staff_hash_password,'utf-8'))
                    if staff_password == db_password:
                        request.session['staff_id'] = s_id
                        return redirect('admin_index')
                    else:
                        messages.error(request,"Incorrect password")
                        # print("Incorrect Password")
                        return redirect('admin_login')
                except Exception as e:
                    messages.error(request,"Number not registered!!")
                    print(e)
                    # print("User doesn't exist")
                    return redirect('admin_login')
            else:
                # print(False)
                messages.error(request,"Invalid entries")
                print("Invalid entries")
                return redirect('admin_login')
        return render(request, 'management/admin_login.html')


def admin_logout(request):
    del request.session['staff_id']
    return redirect('admin_login')


def assign_workers(request, service_id):
    if request.method == 'POST':
        worker_id = request.POST.get('work_id_form')
        booking_id = request.POST.get('book_id_form')
        visiting_date = request.POST.get('visiting_date_form')
        technician_assigned_date = datetime.now().strftime('%Y-%m-%d')
        worker_obj = worker.objects.get(worker_id=worker_id)
        booking_obj = booking.objects.filter(booking_id=booking_id)
        booking_obj.update(booking_status="Worker assigned")
        booking_obj = booking.objects.get(booking_id=booking_id)
        assign_worker_obj = assign_worker(booking_id=booking_obj,worker_id=worker_obj)
        assign_worker_obj.save()
        date_obj = date.objects.filter(booking_id=booking_obj)
        date_obj.update(visiting_date=visiting_date, technician_assigned_date=technician_assigned_date)
        return redirect('assign_workers',service_id=booking_obj.service_id.service_id)
    service_obj = service.objects.get(service_id=service_id)
    booking_obj = booking.objects.filter(service_id=service_obj, booking_status="Processing")
    worker_obj = worker.objects.filter(service_id=service_obj)
    work_count = []
    for i in worker_obj:
        work_count.append(assign_worker.objects.filter(worker_id=i).count())
    z = zip(worker_obj,work_count)
    worker_and_count = []
    for i,j in z:
        worker_and_count.append([i,j])
    return render(request, 'management/assign_worker.html', ({'bookings': booking_obj, 'workers': worker_and_count}))

def workers(request):
    worker_obj = worker.objects.all()
    work_count = []
    for i in worker_obj:
        work_count.append(assign_worker.objects.filter(worker_id=i).count())
    z = zip(worker_obj, work_count)
    worker_and_count = []
    for i, j in z:
        print(i,j)
        worker_and_count.append([i, j])
    return render(request, 'management/workers.html', ({'workers': worker_and_count}))

def all_bookings(request):
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_till = request.POST.get('date_till')
        status_filter = request.POST.get('status_filter')
        sort_filter = request.POST.get('sort_filter')
        if sort_filter == "asc":
            sort = 'booking_date'
        else:
            sort = '-booking_date'
        if date_from == '':
            date_from = str("2020-06-01")
        if date_till == '':
            date_till = datetime.now().strftime('%Y-%m-%d')
        if status_filter == "default":
            booking_obj = booking.objects.filter(booking_date__gte=date_from,
                booking_date__lte=date_till).order_by(sort)
        else:
            booking_obj = booking.objects.filter(booking_status=status_filter,booking_date__gte=date_from,
                booking_date__lte=date_till).order_by(sort)
    else:
        booking_obj=booking.objects.all().order_by('-booking_date')
    soln=[]
    for i in booking_obj:
        try:
            id=assign_worker.objects.get(booking_id=i.booking_id).worker_id.worker_id
            name=assign_worker.objects.get(booking_id=i.booking_id).worker_id.worker_name

            soln.append([i,id,name])
        except:
            soln.append([i,' ',' '])
    return render(request, 'management/all_bookings.html', ({'bookings': soln}))


def assign_staffs(request):
    # if request.method == 'POST':
    #     booking_id = request.POST.get('booking_id')
    #     staff_id = request.POST.get('staff_id')
    #     staff_assigned_date = datetime.now().strftime('%Y-%m-%d')
    #     booking_obj = booking.objects.get(booking_id=booking_id)
    #     staff_obj = booking.objects.get(staff_id=staff_id)
    #     assign_staff_obj = assign_staff(staff_id=staff_obj, booking_id=booking_obj)
    #     assign_staff_obj.save()
    #     booking_obj.update(booking_status="Staff")
    #     date_obj = date.objects.filter(booking_id=booking_obj)
    #     date_obj.update(staff_assigned_date=staff_assigned_date)
    #     return HttpResponse("assigned")
    # booking_obj = booking.objects.filter(booking_status="Processing")
    # staff_obj = staff.objects.all()
    # return render(request,'management/assign_staff.html',({'bookings':booking_obj,'staffs':staff_obj}))
    return HttpResponse("assign staff")
