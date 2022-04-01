from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class RatingForm(forms.Form):
    score = forms.IntegerField(label='Rating',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    ) 
    review = forms.CharField(label='Review', max_length=300)