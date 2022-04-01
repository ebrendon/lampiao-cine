from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=250)
    birthDate = models.DateField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)


class WatchList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField('cinema.Movie')
