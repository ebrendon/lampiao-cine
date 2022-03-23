from django.http import HttpResponse
from models import Movie


def list():
    movies = Movie.objects.all()
    return HttpResponse(movies, status_code=200)


def detail(request, movie_id):
    if(movie_id):
        movie = Movie.objects.filter(id=movie_id)
        return HttpResponse(movie, status_code=200)
    return HttpResponse('O id do filme não foi informado!', status_code=400)


def create(request, movie):
    name = movie
    if(movie):
        movie = Movie(movie)
        movie.save()
        return HttpResponse('Filme criado com sucesso!', status_code=200)
    return HttpResponse('Filme com informações incompletas', status_code=400)


def delete(request, movie_id):
    if(movie_id):
        movie = Movie.objects.filter(id=movie_id)
        movie.delete()
        return HttpResponse('Filme deletado com sucesso!', status_code=200)
    return HttpResponse('O id do filme não foi informado!', status_code=400)


def update(request, movie_id, update_fields):
    if(movie_id):
        movie = Movie.objects.filter(id=movie_id).update(update_fields)
        return HttpResponse('Filme atualizado com sucesso!', status_code=200)
    return HttpResponse('O id do filme não foi informado!', status_code=400)
