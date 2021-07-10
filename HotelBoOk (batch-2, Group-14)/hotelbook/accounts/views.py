from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from index.models import *
from hotels.models import *
from random import randint
from django.core.mail import send_mail
from hotelbook import settings


# Create your views here.
def resetpass(request):
    if request.method =='POST':
        otp1 = randint(1111, 9999)
        email = request.POST['email']
        request.session['otp1'] = otp1
        subject = 'Thank you for registering to our site'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('resetpass2')
    #else:
    return render(request,'resetpass.html')
def resetpass2(request):
    if request.method =='POST':
        otp4 = request.POST['otp5']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:

            if int(otp4) == int(request.session['otp1']):
                user=User.objects.get(email=email)
                user.set_password(password1)
                user.save();
            del request.session['otp1']

            return redirect('login')
        else :
            messages.info(request,'OTP not matched or password not match')
            return redirect('resetpass2')
    return render(request,'resetpass2.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else :
            messages.info(request,'invalid credential')
            return redirect('login')

    else :
        return render(request,'login.html')





def register(request):
    if request.method =='POST' :
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')

            else :

                 user = User.objects.create_user(username=username,password=password1,email=email)
                 user.is_active = False
                 request.session['email'] = email

                 otp = randint(1111, 9999)
                 request.session['otp']= otp
                 subject = 'Thank you for registering to our site'
                 message = str(otp)
                 email_from = settings.EMAIL_HOST_USER
                 recipient_list = [email, ]
                 send_mail(subject, message, email_from, recipient_list)
                 user.save();
                 print("created")
                 return redirect('emailverf')
                 #return render(request,'emailverf.html')
        else :
             messages.info(request,'password not matched')
             return redirect('register')


    return render(request,'register.html')


def emailverf(request):
    if request.method =='POST' :
        otp = request.POST['otp2']
        email = request.POST['email']
        if int(otp) == int(request.session['otp']):
            user=User.objects.get(email=email)
            user.is_active=True
            user.save();
            del request.session['otp']

            return redirect('login')
        else :
            messages.info(request,'OTP not matched')
            return redirect('emailverf')
    return render(request,'emailverf.html')



def logout(request) :

    auth.logout(request)
    return redirect('/')