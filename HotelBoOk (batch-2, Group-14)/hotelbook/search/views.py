from index.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import QuerySet

def search(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        budget = request.GET.get('budget')
        #arrival = request.GET.get('arrival')

        if city:
            hotels = Hotels.objects.filter(city__icontains=city )
        if budget:
            hotels = hotels.filter(price__lte=budget)
        return render(request ,'search.html',{ 'hotels' : hotels})


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')