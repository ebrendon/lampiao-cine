from django.db import models
from users.models import User


class Movie(models.Model):
    RATING_MOVIE_CHOICES = [
        ('G', 'General Audiences'),
        ('PG', 'Parental Guidance Suggested'),
        ('PG-13', 'PG-13 – Parents Strongly Cautioned'),
        ('R', 'Restricted'),
        ('NC-17', 'Adults only')
    ]

    title = models.CharField(max_length=100, unique=True)
    poster = models.TextField()
    description = models.TextField()
    ratingAverage = models.IntegerField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
    ageGroup = models.CharField(max_length=5, choices=RATING_MOVIE_CHOICES)


class Cinema(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=500)
    location_number = models.IntegerField()
    movies = models.ManyToManyField(Movie)


class Ticket(models.Model):
    price = models.IntegerField()
    schedule = models.DateTimeField()
    chair = models.IntegerField()
    room = models.IntegerField()
    theater = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
