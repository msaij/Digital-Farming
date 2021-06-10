from django.db import models

# Create your models here.
class crop(models.Model):
    name = models.CharField(max_length=100)
    climatic_condition=models.CharField(max_length=100)
    water_quantity=models.CharField(max_length=100)
    moisture=models.CharField(max_length=100)
    pesticides=models.CharField(max_length=200)
    ph_level=models.FloatField(default=0)
    min_temp=models.FloatField(default=0)
    max_temp=models.FloatField(default=100)
    land_type=models.CharField(max_length=50, choices=(
        ('chalk soil','chalk soil'),
        ('clay soil','clay soil'),
        ('loam soil','loam soil'),
        ('peat soil','peat soil'),
        ('sandy soil','sandy soil'),
        ('silt soil','silt soil')
    ))
    description=models.TextField(max_length=1000)
    img = models.ImageField(upload_to='crops')
class land(models.Model):
    name= models.CharField(max_length=100)

    img = models.ImageField(upload_to='land')
    # Create your models here.
