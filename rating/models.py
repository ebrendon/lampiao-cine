from django.db import models
from cinema.models import Movie
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Rating(models.Model):

    user = models.CharField(max_length=300)
    movie = models.CharField(max_length=300)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # review = models.TextField(max_length=300)
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # score = models.IntegerField(
    #     validators=[MinValueValidator(1), MaxValueValidator(5)]
    # )
    # review = models.TextField(max_length=300)

    def __str__(self):
        return str(self.score)
 

class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField(max_length=300)

    def __str__(self):
        return self.review