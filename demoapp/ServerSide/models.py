from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

"""class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
"""


class Advisor(models.Model):
    Assigned_User = (
        ('0', 'Yes'),
        ('1', 'No')
    )
    Advisorid = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    photourl=models.TextField()
    createdon=models.DateTimeField(auto_now_add=True)
    modifyon=models.DateTimeField(auto_now_add=True)
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
    createdon=models.DateTimeField(auto_now_add=True)
    modifyon=models.DateTimeField(auto_now_add=True)
    isdelete=models.BooleanField(default=False)
    AssignAdvisor=models.CharField(max_length=1,choices=Assigned_User)
    

class booking(models.Model):
    Advisorid=models.ForeignKey(Advisor, on_delete=models.CASCADE)
    Userid=models.ForeignKey(User, on_delete=models.CASCADE)
    createdon=models.DateTimeField(auto_now_add=True)
    modifyon=models.DateTimeField(auto_now_add=True)
    isdelete=models.BooleanField(default=False)
    bookingTime=models.DateTimeField(auto_now_add=True)
    
