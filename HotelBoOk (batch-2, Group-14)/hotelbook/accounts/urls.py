from django.urls import path , include
from . import views
urlpatterns =[
    path("register",views.register,name = "register"),
    path("login",views.login, name = "login"),
    path("logout",views.logout, name = "logout"),
    path("emailverf",views.emailverf , name= "emailverf"),
    path("resetpass", views.resetpass , name= "resetpass"),
    path("resetpass2", views.resetpass2 , name= "resetpass2"),
    
    #path("index",views.index, name = "index"),
]