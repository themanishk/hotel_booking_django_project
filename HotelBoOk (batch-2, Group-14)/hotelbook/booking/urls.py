from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path("bookroom/<hotelid>/<roomtype>",views.bookroom,name="bookroom"),
    path("new/<hotelid>/<roomid>/<totalcost>/",views.storeBooking,name='storeBooking'),
    path("mybookings",views.mybookings,name='mybookings'),
    url(r'^mybookings/cancel/(?P<bid>[0-9]+)$', views.cancelbooking, name='cancelbooking'),

]
