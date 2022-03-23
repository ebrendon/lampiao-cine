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

    title = models.CharField('título', max_length=100, unique=True)
    poster = models.TextField('pôster')
    description = models.TextField('descrição')
    ratingAverage = models.IntegerField('pontuação')
    duration = models.IntegerField('duração')
    genre = models.CharField('gênero', max_length=100)
    ageGroup = models.CharField(
        'classificação indicativa', max_length=5, choices=RATING_MOVIE_CHOICES)


class Cinema(models.Model):
    name = models.CharField('nome', max_length=200)
    city = models.CharField('cidade', max_length=200)
    street = models.CharField('rua', max_length=500)
    location_number = models.IntegerField('número')
    movies = models.ManyToManyField(Movie, verbose_name='filmes')


class Ticket(models.Model):
    price = models.IntegerField('preço')
    schedule = models.DateTimeField('horário')
    chair = models.IntegerField('cadeira')
    room = models.IntegerField('sala')
    theater = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, verbose_name='teatro')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='cinema')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='usuário')
