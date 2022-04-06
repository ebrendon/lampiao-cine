from django.shortcuts import render, redirect

from cinema.models import Movie
from rating.models import Rating
from users.models import User

from .forms import RatingForm
from django.contrib import messages
from django.core.paginator import Paginator


def listMovieRating(request, pk):

    ratings = Rating.objects.filter(movie=pk)
    paginator = Paginator(ratings, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listMovieRatings.html', {'page_obj': page_obj})


def listUserRating(request):
    user = User.objects.get(pk=request.user.id)
    ratings = Rating.objects.filter(user=user)

    paginator = Paginator(ratings, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'listUserRatings.html', {'page_obj': page_obj})


def deleteRating(request, pk):
    r = Rating.objects.get(pk=pk)
    r.delete()

    messages.success(request, 'Removido com Sucesso')
    return redirect('list-user-rating')


def createRating(request, pk):

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            user = request.user
            movie = Movie.objects.get(id=pk)
            user = User.objects.get(pk=user.id)

            new_rating = form.save(commit=False)
            new_rating.movie = movie
            new_rating.user = user
            new_rating.score = form.cleaned_data.get('score')
            new_rating.review = form.cleaned_data.get('review')
            new_rating.save()

            return redirect('list-movie-rating', pk=pk)
    else:
        form = RatingForm()

    return render(request, 'createRating.html', {'form': form})


def updateRating(request, pk):
    r = Rating.objects.get(pk=pk)

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=r)
        if form.is_valid():
            form.save()

            messages.success(request, 'Modificado com Sucesso!')
            return redirect('list-user-rating')
    else:
        form = RatingForm(instance=r)

    return render(request, 'createRating.html', {'form': form})

# def calculateAverageRating(request, pk):
#     movie_rating = Rating.objects.filter(movie=pk)
#     movie_rating.aggregate(Avg('score'))

#     render(request, 'averageRating.html', movie_rating)
