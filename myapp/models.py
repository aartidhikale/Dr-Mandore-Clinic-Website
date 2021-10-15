from django.db import models
import datetime
import os

class Register(models.Model):
    firstname=models.TextField(max_length=254)
    lastname=models.TextField(max_length=254)
    Email=models.EmailField(max_length=254)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Birthdate=models.TextField(max_length=254)
    City=models.TextField(max_length=254)
    imageuser = models.ImageField('images/', null=True, blank=True)

    
# Create your models here.
class Consult1(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    phone=models.TextField(max_length=254)
    address=models.TextField(max_length=254)
    Birthdate=models.TextField(max_length=254)
    Birthmonth=models.TextField(max_length=254)
    Birthyear=models.TextField(max_length=254)
    Hobbies=models.TextField(max_length=254)
    Diagnosis=models.TextField(max_length=254)
    Work=models.TextField(max_length=254)
    Diet=models.TextField(max_length=254)

class Contact(models.Model):
    name= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    comment=models.TextField(max_length=254)


class Item1(models.Model):
    name = models.TextField(max_length=191)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField('images/', null=True, blank=True)

class FAQ(models.Model):
    question = models.TextField(max_length=191)
    answer = models.TextField(max_length=500, null=True)
    