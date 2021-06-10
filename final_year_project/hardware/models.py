from django.db import models

# Create your models here.
class hdata(models.Model):
    Did=models.CharField(max_length=20)
    temp=models.FloatField(default=0.0)
    moisture=models.FloatField(default=0.0)
    ph=models.FloatField(default=0.0)