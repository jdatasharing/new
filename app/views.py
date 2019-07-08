from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *

# Create your views here.

def indexpage(request):
    return render(request,"app/temp.html")
def indexpage1(request):
    return render(request,"app/inex.html")
def registerpage(request):
    return render(request,"app/register.html")
def teamregister(request):
    return render(request,"app/teamregistration.html")
def schedule(request):
    return render(request,"app/schedule.html")





def Registeruser(request):
    fname=request.POST['fanme']
    lname=request.POST['lanme']
    address=request.POST['add']
    email=request.POST['email']
    password=request.POST['password']

    newuser=User.objects.create(fname=fname,lname=lname,address=address,email=email,password=password)
    return render(request,"app/app.html")

def teamregistration(request):
    tname=request.POST['tname']
    cname=request.POST['cname']
    hname=request.POST['hname']
    oname=request.POST['oname']
    email=request.POST['email']

    newuser=Team.objects.create(tname=tname,cname=cname, hname=hname,oname=oname,email=email)
    return render(request,"app/app1.html")

def teamschedule(request):
    match=request.POST['match']
    team1=request.POST['team1']
    team2=request.POST['team2']
    ground=request.POST['ground']

    newuser=Match.objects.create(match=match,team1=team1,team2=team2,ground=ground)
    return HttpResponseRedirect(reverse('showmatch'))
    
def ShowMatch(request):
    all_match=Match.objects.all()
    print("All Match------------> ",all_match)
    return render(request,"app/show.html",{'all_match':all_match})

