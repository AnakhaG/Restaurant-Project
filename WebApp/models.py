from django.db import models

# Create your models here.
class Contact_DB(models.Model):
    Name =models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Subject = models.CharField(max_length=200,null=True,blank=True)
    Message = models.TextField(max_length=500,null=True,blank=True)
class Signup_DB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Mobile_Number = models.IntegerField(null=True,blank=True)
    Pass_word=models.CharField(max_length=15,null=True,blank=True)
    Re_pass=models.CharField(max_length=15,null=True,blank=True)
class Cartdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    FudName = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
class OrderDb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=80,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.TextField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Message = models.TextField(max_length=300,null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)