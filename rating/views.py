from django.shortcuts import render, redirect, get_object_or_404
from rating.models import Rating
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

def createRating(request):
    if request.method == 'POST': 
        form = RatingForm(request.POST)
         
        if form.is_valid():
            score = form.cleaned_data.get('score')
            review = form.cleaned_data.get('review')

            # Alterar este Construtor  
            r = Rating(score=score, review=review)   
            r.save() 

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