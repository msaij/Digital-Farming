from django.db import models

# Create your models here.
class profilepic1(models.Model):
    userid= models.CharField(max_length=5)
    img = models.ImageField(upload_to='profile')
class landtype(models.Model):
    userid= models.CharField(max_length=20)
    land_type= models.CharField(max_length=35, default='clay soil')
    land_area= models.FloatField(max_length=8)
    cropselected= models.CharField(max_length=35, default='rice')