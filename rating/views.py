from unicodedata import name
from django.shortcuts import render, redirect
from cinema.models import Movie
from rating.models import Rating
from users.models import User
from .forms import RatingForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def listRating(request):

    ratings = Rating.objects.all()
    ratings_dict = {'ratings': ratings}

    return render(request, 'listRatings.html', ratings_dict)


def deleteRating(request, pk):
    r = Rating.objects.get(pk=pk)
    r.delete()

    # Framework de Mensagens
    messages.success(request, 'Removido com Sucesso')
    return redirect('list-rating')


def createRating(request, pk): 

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            user = request.user
            print('user-------------')
            print(user)
            print(user.id)
            print('user-------------')

            movie = Movie.objects.get(id=pk)
            user = User.objects.get(pk=user.id)

            new_rating = form.save(commit=False)
            new_rating.movie = movie
            new_rating.user = user
            new_rating.score = form.cleaned_data.get('score')
            new_rating.review = form.cleaned_data.get('review')
            new_rating.save()
 

            messages.success(request, 'Adicionado com Sucesso')
            return redirect('list-rating')
    else:
        form = RatingForm()

    return render(request, 'createRating.html', {'form': form})


def updateRating(request, pk):
    r = Rating.objects.get(pk=pk)

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            return redirect('list-rating')
    else:
        form = RatingForm(instance=r)

    return render(request, 'createRating.html', {'form': form})
