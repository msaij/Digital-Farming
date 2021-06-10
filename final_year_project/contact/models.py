from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email=models.EmailField()
    workStatus = (
        ('Teacher','Teacher'),
        ('Student','Student')
    )
    category = models.CharField(max_length=50, choices=workStatus)
    img = models.ImageField(upload_to='Contact')
