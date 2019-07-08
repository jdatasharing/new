from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class Team(models.Model):
    tname=models.CharField(max_length=50)
    cname=models.CharField(max_length=50) 
    hname=models.CharField(max_length=50) 
    oname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

class Match(models.Model):
    match=models.CharField(max_length=50)
    team1=models.CharField(max_length=50)
    team2=models.CharField(max_length=50)
    ground=models.CharField(max_length=50)