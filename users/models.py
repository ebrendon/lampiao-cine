from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=250, null=True)
    birthDate = models.DateField(null=True)
    phone = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class WatchList(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    movies = models.ManyToManyField('cinema.Movie')

class Account(models.Model):
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=200)
