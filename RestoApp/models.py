from django.db import models

# Create your models here.
class Food_Db(models.Model):
    Category_Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=500,null=True,blank=True)
    Category_Image = models.ImageField(upload_to="Categories",null=True,blank=True)
class FoodItems_DB(models.Model):
    category = models.CharField(max_length=100,null=True,blank=True)
    Food_Name = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Food_Description = models.TextField(max_length=500,null=True,blank=True)
    Food_Imagea = models.ImageField(upload_to="Food_Items",null=True,blank=True)
    Food_Imageb = models.ImageField(upload_to="Food_Items",null=True,blank=True)
    Food_Imagec = models.ImageField(upload_to="Food_Items",null=True,blank=True)