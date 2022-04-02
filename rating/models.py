from email import message
from django.db import models
from cinema.models import Movie
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
  
class Rating(models.Model):

    user = models.CharField(max_length=100)
    movie = models.CharField(max_length=200)
    review = models.CharField(max_length=300, default='')
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, "Certifique-se de que este valor seja maior ou igual a 1"), 
            MaxValueValidator(5, "Certifique-se de que esse valor seja menor ou igual a 5.")
        ])

    def __str__(self):
        return "Rating: {}, Review: {}".format(self.score, self.review)
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # score = models.IntegerField(
    #     validators=[MinValueValidator(1), MaxValueValidator(5)]
    # )
    # review = models.TextField(max_length=300)
  

# class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # review = models.TextField(max_length=300)

    # def __str__(self):
    #     return str(self.review)