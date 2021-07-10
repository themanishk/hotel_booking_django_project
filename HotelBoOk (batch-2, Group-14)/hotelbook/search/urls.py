from django.urls import path , include
from . import views
urlpatterns =[
    path('', views.search, name = "search"),
    path('contact', views.contact, name = "contact"),
    path('about', views.about, name = "about"),

]
