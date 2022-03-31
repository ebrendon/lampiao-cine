import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import render

from .serializers import RatingSerializer
from rating.models import Rating, Review
from .forms import ReviewForm
from django.http import HttpResponse
from .models import Review

# # 1. List all
def listRating(request): 

    ratings = Rating.objects.all()
    ratings_dict = {'ratings': ratings}

    return render(request, 'listRatings.html', ratings_dict)

def listReview(request): 

    reviews = Review.objects.all()
    reviews_dict = {'reviews': reviews}

    return render(request, 'listReview.html', reviews_dict)

def deleteRating(request):
    pass

def deleteReview(request):
    pass

def createRating(request):
    pass

def createReview(request): 
    if request.method == 'POST': 
        form = ReviewForm(request.POST)
         
        if form.is_valid():
            review = form.cleaned_data.get('review')
            r = Review(review=review)
            r.save() 
            return HttpResponse()
 
    else:
        form = ReviewForm()

    return render(request, 'createReview.html', {'form': form})