from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from datetime import datetime,date

class Advisor(models.Model):
    Assigned_User = (
        ('0', 'Yes'),
        ('1', 'No')
    )
    Advisorid = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    isdelete=models.BooleanField(default=False)
    AssignUser=models.CharField(max_length=1,choices=Assigned_User)
    

class User(models.Model):
    Assigned_User = (
        ('0', 'Yes'),
        ('1', 'No')
    )
    Userid = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    isdelete=models.BooleanField(default=False)
    AssignAdvisor=models.CharField(max_length=1,choices=Assigned_User)
    

class booking(models.Model):
    Advisorid=models.ForeignKey(Advisor, on_delete=models.CASCADE)
    Userid=models.ForeignKey(User, on_delete=models.CASCADE)
    createdon=models.DateTimeField(auto_now_add=True)
    modifyon=models.DateTimeField(auto_now_add=True)
    isdelete=models.BooleanField(default=False)
    bookingTime=models.DateTimeField(auto_now_add=True,auto_now=False)
    
