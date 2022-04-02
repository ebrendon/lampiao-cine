from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

from rating.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'review']

    # score = forms.IntegerField(label='Rating',
    #     validators=[
    #         MinValueValidator(1, "Certifique-se de que este valor seja maior ou igual a 1"), 
    #         MaxValueValidator(5, "Certifique-se de que esse valor seja menor ou igual a 5.")
    #     ]) 
    # review = forms.CharField(label='Review',validators=[MaxLengthValidator(300, "Número de caracteres máximo")])