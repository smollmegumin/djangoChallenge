from django.db import models


class User(models.model):
    username = models.String
    email = models.String
    password = models.String
