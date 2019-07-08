
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.registerpage,name="register"),
    path("index/",views.indexpage,name="temp"),
    path("index1/",views.indexpage1,name="temp1"),
    path("register/",views.Registeruser,name="register"),
    path("team/",views.teamregister,name="team"),
    path("teams/",views.schedule,name="teams"),
    path("user/",views.teamregistration,name="user"),
    path("user1/",views.teamschedule,name="user1"),
    path("showmatch/",views.ShowMatch,name="showmatch")

    
]
