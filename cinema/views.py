from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from cinema.models import Cinema, Ticket, Movie

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer

class MovieListAPIView(APIView): 
 
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListMoviesView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies_list'
    http_method_names = ['get']


class DetailMovieView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie_detail'
    http_method_names = ['get']


class BuyTicketView(UpdateView):
    http_method_names = ['post']
    pass


class ListCinemaView(ListView):
    model = Cinema
    template_name = 'cinema_list.html'
    context_object_name = 'cinema_list'
    http_method_names = ['get']


class DetailCinemaView(DetailView):
    model = Cinema
    template_name = 'cinema_detail.html'
    context_object_name = 'cinema_detail'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cinema_id = context['cinema_detail'].id
        context['tickets'] = Ticket.objects.filter(cinema=cinema_id)
        return context
