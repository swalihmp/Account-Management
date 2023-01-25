from django.db import models

# Create your models here.

class user_data(models.Model): 
    firstname = models.CharField(max_length=50,default=0)
    lastname = models.CharField(max_length=50,default=0)
    username = models.CharField(max_length=100) 
    email = models.EmailField()
    password = models.CharField(max_length=15)
    
class imgdata(models.Model):
    img_data = models.FileField()
    desc = models.CharField(max_length=30)
    
