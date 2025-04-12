from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=155)
    author = models.CharField(max_length=155)
    age = models.IntegerField()
    genre = models.CharField(max_length=155)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    


