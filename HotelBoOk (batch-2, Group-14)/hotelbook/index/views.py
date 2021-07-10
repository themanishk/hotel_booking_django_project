# Create your views here.
from django.shortcuts import render
from index.models import *
from hotels.models import *
def index(request):
    hotels = Hotels.objects.all()

    return render(request, "index.html",{'hotels' : hotels})