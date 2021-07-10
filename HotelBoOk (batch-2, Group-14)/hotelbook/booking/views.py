from index.models import *
from hotels.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from hotels.models import Booking,Review
import datetime
from django import forms
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.core.signing import Signer
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q

from django.views import View
from django.template.loader import get_template


from django.shortcuts import render

# Create your views here.
def bookroom(request,hotelid,roomtype):
    FirstDate = request.session['arrival']
    SecDate =  request.session['departure']
    if FirstDate and SecDate:
        Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
        Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
    else:
        Checkin = datetime.date.today()
        Checkout = Checkin + datetime.timedelta(days=1)
        request.session['arrival'] = str(Checkin)
        request.session['departure'] = str(Checkout)

    timedeltaSum = Checkout - Checkin

    StayDuration = int(timedeltaSum.days)

    hotel = Hotels.objects.get(hotel_id__exact=hotelid)
    rooms = Room.objects.filter(hotel_id__exact=hotelid).filter(RoomType__exact=roomtype)
    for room in rooms:
        price = room.Price
    TotalCost = StayDuration * int(price)


    context = {'checkin': Checkin, 'checkout':Checkout,'stayduration':StayDuration,'hotel':hotel,'rooms':rooms , 'price':price,'totalcost':TotalCost}
    return render(request, 'booking.html', context)



def storeBooking(request,hotelid,roomid,totalcost):
    if request.method == 'POST' and request.user.is_authenticated:


        Firstname = request.POST.get('firstname')
        Lastname = request.POST.get('lastname')
        checkin = request.session['arrival']
        checkout = request.session['departure']
        user = request.user
        hotel = Hotels.objects.get(hotel_id__exact=hotelid)
        room = Room.objects.get(id = roomid)
        cost = totalcost
        newReservation = Booking.objects.create(hotel_id=hotel,roomtype=room.RoomType,user=user,guestFirstName=Firstname,guestLastName=Lastname,CheckIn=checkin,
                                                CheckOut=checkout,totalPrice=cost)
        #newReservation.hotel_id = hotel
        #newReservation.roomtype = room.RoomType
        #newReservation.user = user
        #newReservation.guestFirstName = Firstname
        #newReservation.guestLastName = Lastname
        #newReservation.CheckIn = checkin
        #newReservation.CheckOut = checkout
        #newReservation.totalPrice = cost
        newReservation.save();
        #Deletes the session variables.
        #del request.session['arrival']
        #del request.session['departure']
        bid = newReservation.id
        bookings = Booking.objects.filter(id=bid)

        return render(request,'mybookings.html',{ 'bookings': bookings})
    else:
        return redirect('/accounts/login')

def mybookings(request):
    bookings = Booking.objects.filter(user = request.user)
    context = {'bookings':bookings}
    return render(request, 'mybookings.html', context)

def cancelbooking(request,bid):
    booking = Booking.objects.filter(id = bid)
    booking.delete()
    return redirect('/booking/mybookings')


