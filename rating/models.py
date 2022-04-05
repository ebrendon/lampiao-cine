from django.db import models
from cinema.models import Movie
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
  
class Rating(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    review = models.TextField(default='', 
        validators=[MaxLengthValidator(300, "Número de caracteres máximo")])
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, "Certifique-se de que este valor seja maior ou igual a 1"), 
            MaxValueValidator(5, "Certifique-se de que esse valor seja menor ou igual a 5.")
        ])

    def __str__(self):
        return "Rating: {}, Review: {}".format(self.score, self.review)