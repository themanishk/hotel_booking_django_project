from django.shortcuts import render
from django.template.loader import render_to_string
from index.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from hotels.models import *
import datetime
from django import forms
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.core.signing import Signer
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q

from django.views import View
from django.template.loader import get_template

# Create your views here.
def hotels(request,hotel_id):
    hotels = Hotels.objects.get(hotel_id__exact=hotel_id)
    rooms = Room.objects.filter(hotel_id__exact=hotel_id)
    theuser = request.user
    if theuser.is_authenticated:
        RecentReservation = Booking.objects.filter(hotel_id__exact=hotel_id).filter(user=theuser)
        if RecentReservation:
            allowReview = True
        else:
            allowReview = False
    else:
        allowReview = False

    reviews = Review.objects.filter(hotel_id__exact=hotel_id)
    current_user = request.user
    if request.method == "GET":
            arrival = request.GET.get('arrival1')
            departure = request.GET.get('departure1')
            #if departure < arrival:
                #return redirect(request.path_info)
            request.session['arrival'] = arrival
            request.session['departure'] = departure
            #if arrival is None:
                #arrival=datetime.datetime.now()
            #if departure is None:
                #departure=datetime.datetime.now()

            roomsbookeda = Booking.objects.filter(hotel_id__exact=hotel_id)
            if arrival and departure:
                roomsbookeda = roomsbookeda.filter(CheckIn__lte=departure, CheckOut__gte=arrival)
            for room in rooms:
                roomsbookeda = roomsbookeda.filter(roomtype__exact=room.RoomType)
                #roomsbookedn = Booking.objects.filter(hotel_id__exact=hotel_id)
                #if arrival and departure:
                #roomsbookedn = roomsbookedn.filter(CheckIn__lte=departure, CheckOut__gte=arrival).filter(room__exact='non_ac')
                counta = roomsbookeda.count()
                roomsa = room.TotalRooms
                #for hotel in hotels:
                #roomsa = hotel.ac_rooms
                #roomsb = hotel.non_ac_rooms
                roomsa = int(roomsa)
                rooma = roomsa - counta
                #countb = roomsbookedn.count()
                #roomsb = int(roomsb)
                #roomn = roomsb - countb
                room.avai = rooma
            return render(request, 'hotels.html', {'hotel': hotels,'rooms' : rooms,'reviews':reviews,'user':current_user,'allowReview':allowReview})
    else:
        return render(request,'hotels.html',{'hotel': hotels,'reviews':reviews,'user':current_user,'allowReview':allowReview} )




# Stores the confirmed booking  into the database




