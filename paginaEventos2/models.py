from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.
class Alumno(models.Model):
    
    fullname = models.CharField(max_length=200)
    nombre? = models.ForeignKey('nombre?', on_delete=models.SET_NULL, null=True)
    mail= models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    rut= models.int(max_length=8)
    fullname = models.CharField(max_length=200)