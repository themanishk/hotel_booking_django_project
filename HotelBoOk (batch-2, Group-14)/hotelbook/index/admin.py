from django.contrib import admin
from index.models import *
from hotels.models import *


# Register your models here.
admin.site.register(Hotels)
admin.site.register(Driver)
admin.site.register(Guide)
admin.site.register(Booking)
admin.site.register(Room)