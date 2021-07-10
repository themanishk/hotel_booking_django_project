# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models







class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    vehicle_no = models.CharField(max_length=15, blank=True, null=True)
    mob_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'driver'









class Guide(models.Model):
    guide_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    languages = models.CharField(max_length=100, blank=True, null=True)
    charges = models.IntegerField(blank=True, null=True)
    mob_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'guide'

class Hotels(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pincode = models.IntegerField(default=0)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='pics', default=0)
    price = models.IntegerField(default=0)

    description = models.TextField(default='hotel')

    class Meta:
        managed = True
        db_table = 'hotels'







class Pickup(models.Model):
    cust_id = models.IntegerField( primary_key=True)
    driver_id = models.ForeignKey('Driver',on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    time = models.TimeField(default=0)
    date = models.DateField(default=0)

    class Meta:
        managed = True
        db_table = 'pickup'

class Guests(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    hotel_id = models.ForeignKey('Hotels', on_delete=models.CASCADE)
    cust_name = models.CharField(max_length=30)
    mob_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'guests'


class Tourist(models.Model):
    cust_id = models.IntegerField( primary_key=True)
    guide_id = models.ForeignKey('Guide', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'tourist'