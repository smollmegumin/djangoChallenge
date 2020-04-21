from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    placas = models.CharField(max_length=200,unique=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    lat = models.FloatField()
    lon = models.FloatField()