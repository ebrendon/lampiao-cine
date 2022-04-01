from django.shortcuts import render, redirect
from rating.models import Rating
from .forms import RatingForm
from django.http import HttpResponse, HttpResponseRedirect

def listRating(request): 

    ratings = Rating.objects.all()
    ratings_dict = {'ratings': ratings}

    return render(request, 'listRatings.html', ratings_dict)

# def listReview(request): 

#     reviews = Review.objects.all()
#     reviews_dict = {'reviews': reviews}

#     return render(request, 'listReview.html', reviews_dict)

def deleteRating(request, pk):
    r = Rating.objects.get(pk=pk)
    r.delete()
    return redirect('list-rating')  
 

# def deleteReview(request, pk):
#     r = Review.objects.get(pk=pk)
#     r.delete()
#     return redirect('list-review')

def createRating(request):
    if request.method == 'POST': 
        form = RatingForm(request.POST)
         
        if form.is_valid():
            score = form.cleaned_data.get('score')
            review = form.cleaned_data.get('review')
            print("-----------")
            print(review)
            print("-----------")
            # Alterar este Construtor  
            r = Rating(score=score, review=review)   
            r.save() 
            return redirect('list-rating')  
    else:
        form = RatingForm()

    return render(request, 'createRating.html', {'form': form})

# def createReview(request): 
#     if request.method == 'POST': 
#         form = ReviewForm(request.POST)
         
#         if form.is_valid():
#             review = form.cleaned_data.get('review')
#             r = Review(review=review)       # alterar este construtor 
#             r.save() 
#             return redirect('list-review') 
 
#     else:
#         form = ReviewForm()

#     return render(request, 'createReview.html', {'form': form})

def updateRating(request):
    pass
 