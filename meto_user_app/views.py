from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user, service, booking, recovery, feedback
from meto_admin_app.models import staff, worker, assign_staff, assign_worker, date
from .validator import valid_login, valid_signup, valid_details, valid_booking
import bcrypt
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from datetime import datetime
from django.utils import timezone
from django.contrib import messages

# Create your views here.

#LOGIN --------------------------------------------------------
def login(request):
    if request.session.has_key('user_id'):
        return redirect('index')
    else:
        if request.method == 'POST':
            user_phone = request.POST.get('login_phone')
            user_password = request.POST.get('login_pass')
            if valid_login(user_phone, user_password):
                # print(True)
                try:
                    user_obj = user.objects.get(user_phone=user_phone)
                    u_id = user_obj.user_id
                    user_hash_password = user_obj.user_password
                    user_hash_password = str(user_hash_password)
                    user_hash_password = user_hash_password[2:len(user_hash_password) - 1]
                    check_pass = bcrypt.checkpw(user_password.encode('utf8'), bytes(user_hash_password, 'utf-8'))
                    if check_pass:
                        request.session['user_id'] = u_id
                        return redirect('index')
                    else:
                        messages.info(request,"Incorrect password!!")
                        #print("Incorrect Password")
                        return redirect('login')
                except Exception as e:
                    messages.error(request,"Number not registered!!")
                    print(e)
                    #print("User doesn't exist")
                    return redirect('login')
            else:
                # print(False)
                # print("Invalid entries")
                messages.error(request,"Invalid entries")
                return redirect('login')
        return render(request, 'customer/login.html')


#SIGNUP --------------------------------------------------------
def signup(request):
    if request.session.has_key('user_id'):
        return redirect('index')
    else:
        if request.method == 'POST':
            user_name = request.POST.get('new_name')
            user_email = request.POST.get('new_email')
            user_phone = request.POST.get('new_phone')
            user_password = request.POST.get('new_pass')
            user_gender = request.POST.get('new_gender')
            user_pincode = request.POST.get('new_pincode')
            user_city = request.POST.get('new_city')
            user_area = request.POST.get('new_area')
            if valid_signup(user_name, user_email, user_phone, user_password):
                # print(True)
                if user.objects.filter(user_phone=user_phone).count()!=0:
                    messages.error(request,"Number already registered")
                    return redirect('login')
                if user.objects.filter(user_email=user_email).count()!=0:
                    messages.error(request,"Email already registered")
                    return redirect('login') 
                user_hash_password = bcrypt.hashpw(user_password.encode('utf8'), bcrypt.gensalt())
                try:
                    user_obj = user(user_name=user_name, user_email=user_email, user_phone=user_phone,
                                    user_password=user_hash_password,user_gender=user_gender,
                                    user_pincode=user_pincode,user_city=user_city,user_area=user_area)
                    user_obj.save()
                    user_obj = user.objects.get(user_phone=user_phone)
                    u_id = user_obj.user_id
                    request.session['user_id'] = u_id
                    return redirect('index')
                except Exception as e:
                    print(e)
                    # print("Failed query")
                    messages.error(request,"Internal error. Try again")
                    return redirect('login')
            else:
                # print(False)
                # print("Invalid entries")
                messages.error(request,"Invalid entries")
                return redirect('login')
        return render(request, 'customer/login.html')

#LOGOUT --------------------------------------------------------
def logout(request):
    if request.session.has_key('user_id'):
        del request.session['user_id']
    return redirect('index')

#HOMEPAGE --------------------------------------------------------
def index(request):
    if request.session.has_key('user_id'):
        user_obj = user.objects.get(user_id=request.session['user_id'])
        return render(request, 'customer/index.html', ({'user': user_obj}))
    return render(request, 'customer/index.html')

#PROFILE & EDIT PROFILE & BOOKINGS & RATING------------------------------------------
def profile(request):
    if request.session.has_key('user_id'):
        user_obj = user.objects.get(user_id=request.session['user_id'])
        booking_obj = booking.objects.filter(user_id=user_obj).order_by('-booking_id')
        return render(request, 'customer/newprofile.html', ({'bookings': booking_obj, 'user': user_obj}))
    return redirect('index')


def edit_profile(request):
    if request.session.has_key('user_id'):
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            user_phone = request.POST.get('user_phone')
            user_email = request.POST.get('user_email')
            user_gender = request.POST.get('user_gender')
            user_area = request.POST.get('user_area')
            user_city = request.POST.get('user_city')
            user_pincode = request.POST.get('user_pincode')
            user_old_pass = request.POST.get('user_old_pass')
            user_new_pass = request.POST.get('user_new_pass')
            user_obj = user.objects.get(user_id=request.session['user_id'])
            if valid_details(user_name, user_phone, user_email, user_gender, user_area,
                             user_city, user_pincode, user_old_pass, user_new_pass):
                # print(True)
                try:
                    check_unique = user.objects.get(user_phone=user_phone)
                    if check_unique.user_phone != user_obj.user_phone:
                        messages.error(request,"Number already registered!!")
                        return redirect('profile')
                except:
                    pass
                try:
                    check_unique = user.objects.get(user_email=user_email)
                    if check_unique.user_email != user_obj.user_email:
                        messages.error(request,"Email already registered!!")
                        return redirect('profile')
                except:
                    pass
                user_password = user_obj.user_password
                if len(user_old_pass) >= 8 and len(user_new_pass) >= 8:
                    user_hash_password = str(user_password)
                    user_hash_password = user_hash_password[2:len(user_hash_password) - 1]
                    check_pass = bcrypt.checkpw(user_old_pass.encode('utf8'), bytes(user_hash_password, 'utf-8'))
                    if check_pass:
                        user_password = bcrypt.hashpw(user_new_pass.encode('utf8'), bcrypt.gensalt())
                    else:
                        messages.error(request,"Invalid current password!!")
                        return redirect('profile')
                user_obj = user.objects.filter(user_id=request.session['user_id'])
                user_obj.update(user_name=user_name, user_phone=user_phone, user_email=user_email,
                                user_gender=user_gender, user_area=user_area, user_city=user_city,
                                user_pincode=user_pincode,
                                user_password=user_password)
                return redirect('profile')
            else:
                # print("Invalid details")
                messages.error(request,"Invalid details!!")
                return redirect('profile')
        # else:
        #     user_obj = user.objects.get(user_id=request.session['user_id'])
        #     return render(request, 'customer/edit_profile.html', ({'user': user_obj}))
    return redirect('index')

def bookings(request):
    if request.session.has_key('user_id'):
        user_obj = user.objects.get(user_id=request.session['user_id'])
        booking_obj = booking.objects.filter(user_id=user_obj).order_by('-booking_id')
        return redirect('not_found')
        return render(request, 'customer/bookings.html', ({'bookings': booking_obj, 'user': user_obj}))
    return redirect('index')

def rate_booking(request):
    if request.session.has_key('user_id'):
        if request.method=='POST':
            booking_id = request.POST['btn']
            rating = request.POST.get('star')
            comment = request.POST.get('comment')
            try:
                booking_obj = booking.objects.get(booking_id=booking_id)
                try:
                    feedback_obj = feedback.objects.get(booking_id=booking_id)
                    return redirect('not_found')
                except Exception as e:
                    feedback_obj = feedback(booking_id=booking_obj, rating=rating, feedback=comment)
                    feedback_obj.save()
                    booking_obj = booking.objects.filter(booking_id=booking_id)
                    booking_obj.update(booking_status="Ticket closed")
                    date_obj = date.objects.filter(booking_id=booking_id)
                    date_obj.update(close_date=datetime.now().strftime('%Y-%m-%d'))
                    return redirect('profile')
            except:
                pass
    return redirect('not_found')

#BOOK SERVICE -----------------------------------------------------------
def book(request):
    if request.session.has_key('user_id'):
        if request.method == 'POST':
            booking_desc = request.POST.get('booking_desc')
            booking_area = request.POST.get('booking_area')
            booking_city = request.POST.get('booking_city')
            booking_pincode = request.POST.get('booking_pincode')
            booking_phone = request.POST.get('booking_phone')
            service_id = request.POST.get('service_id')
            if valid_booking(booking_pincode, booking_phone):
                # print(True)
                try:
                    user_obj = user.objects.get(user_id=request.session['user_id'])
                    service_obj = service.objects.get(service_id=service_id)
                    booking_obj = booking(user_id=user_obj, service_id=service_obj,
                                          booking_desc=booking_desc, booking_phone=booking_phone,
                                          booking_area=booking_area,
                                          booking_city=booking_city, booking_pincode=booking_pincode)
                    booking_obj.save()
                    date_obj = date(booking_id=booking_obj)
                    date_obj.save()
                    return render(request, 'customer/booking_success.html')
                except Exception as e:
                    print(e)
                    # print("Failed booking")
            else:
                # print("Invalid details")
                messages.error(request,"Invalid details!!")
            return redirect('index')
        # user_obj = user.objects.get(user_id=request.session['user_id'])
        # service_obj = service.objects.get(service_id=service_id)
        # return render(request, 'customer/book_ticket.html', ({'user': user_obj, 'service': service_obj}))
    return redirect('login')

#FORGOT PASS --------------------------------------------------------
def forgotpass(request):
    if request.method=='POST':
        phone = request.POST.get('recovery_phone')
        try:
            user_obj = user.objects.get(user_phone=phone)
            try:
                email = user.objects.get(user_phone=phone).user_email
                sender="metojrt@gmail.com"
                subject = "Reset your password"
                site="https://meto-jrt.herokuapp.com/reset/"
                recovery_id = str(get_random_string(length=32))+str(datetime.now().strftime('%Y%m%d%H%M%S'))
                msg="Go to the link below to reset your password.\n\nDo not share the link with anyone.\n"+site+recovery_id
                send_mail(subject,msg,sender,[email],fail_silently=False)
                recovery_obj = recovery.objects.filter(email_id=email)
                if recovery_obj.exists():
                    recovery_obj.update(recovery_id=recovery_id)
                else:
                    recovery_obj = recovery(email_id=email,recovery_id=recovery_id)
                    recovery_obj.save()
                return render(request,'customer/password_reset_email.html')
            except Exception as e:
                print(e)
        except Exception as e:
            raise e
            messages.error(request,"Number not registered!!")
            return redirect('login')
    return redirect('not_found')

#RESET PASS --------------------------------------------------------
def resetpass(request,recovery_id):
    if request.method=='POST':
        new_pass = request.POST.get('new_password')
        try:
            recovery_obj = recovery.objects.get(recovery_id=recovery_id)
            email = recovery_obj.email_id
            user_password = bcrypt.hashpw(new_pass.encode('utf8'), bcrypt.gensalt())
            user_obj = user.objects.filter(user_email=email)
            user_obj.update(user_password=user_password)
            recovery_obj.delete()
        except Exception as e:
            print(e)
        return redirect('login')
    return render(request,'customer/password_reset.html')

def not_found(request,exception):
    return render(request,'404.html')

