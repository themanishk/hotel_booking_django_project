from django.db import models
from django.contrib.auth.models import User
# Create your models here
from index.models import *
import datetime


class Booking(models.Model):
    hotel_id = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    roomtype = models.CharField(max_length=255,default='standard')
    totalPrice = models.IntegerField(default = 0)
    guestFirstName = models.CharField(max_length=255,default='NONE')
    guestLastName = models.CharField(max_length=255,default='NONE')




class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    comment = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default = 0)


class Room(models.Model):
    hotel_id = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    RoomType = models.CharField(max_length  = 255)
    Capacity = models.IntegerField(default = 0)
    BedOption = models.CharField(max_length  = 255)
    Price= models.IntegerField(default = 0)
    TotalRooms = models.CharField(max_length  = 255)
    photo = models.ImageField(upload_to='pics', default=0)
    smart_tv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    pools = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



