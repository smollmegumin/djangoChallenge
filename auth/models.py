from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200, unique=True)
