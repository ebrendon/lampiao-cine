from django.db import models
from users.models import User


class Movie(models.Model):
    RATING_MOVIE_CHOICES = [
        ('G', 'General Audiences'),
        ('PG', 'Parental Guidance Suggested'),
        ('PG-13', 'PG-13 - Parents Strongly Cautioned'),
        ('R', 'Restricted'),
        ('NC-17', 'Adults only')
    ]

    GENRE_MOVIE_CHOICES = [
        ('Terror', 'Terror'),
        ('Aventura', 'Aventura'),
        ('Ação', 'Ação'),
        ('Ficção Científica', 'Ficção Científica'),
        ('Drama', 'Drama'),
        ('Comédia', 'Comédia'),
        ('Suspense', 'Suspense')
    ]

    title = models.CharField('título', max_length=100, unique=True)
    poster = models.TextField('pôster')
    description = models.TextField('descrição')
    ratingAverage = models.FloatField('pontuação')
    duration = models.IntegerField('duração')
    genre = models.CharField('gênero', max_length=50,
                             choices=GENRE_MOVIE_CHOICES)
    ageGroup = models.CharField(
        'classificação indicativa', max_length=5, choices=RATING_MOVIE_CHOICES)

    def __str__(self):
        return self.title

    def get_ratings(self):
        return 1000


class Cinema(models.Model):
    name = models.CharField('nome', max_length=200)
    city = models.CharField('cidade', max_length=200)
    street = models.CharField('rua', max_length=500)
    location_number = models.IntegerField('número')
    movies = models.ManyToManyField(Movie, verbose_name='filmes')

    def __str__(self):
        return self.name


class Ticket(models.Model):
    price = models.IntegerField('preço')
    schedule = models.DateTimeField('horário')
    chair = models.IntegerField('cadeira')
    room = models.IntegerField('sala')
    cinema = models.ForeignKey(
        Cinema, on_delete=models.CASCADE, verbose_name='cinema', default='')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='filme')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='usuário', null=True, blank=True)

    def __str__(self):
        return f"{self.cinema.name} - Sala {str(self.room)} - Cadeira {str(self.chair)} "
