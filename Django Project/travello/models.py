from msilib.schema import Class
from operator import mod
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Destination(models.Model):    #Models and Migration
    
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

