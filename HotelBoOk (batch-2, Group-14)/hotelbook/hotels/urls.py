from django.urls import path , include
from . import views
from django.conf.urls import url
urlpatterns =[
    path("<hotel_id>/",views.hotels,name = "hotels"),



]
