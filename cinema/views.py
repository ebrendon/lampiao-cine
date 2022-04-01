from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from cinema.models import Cinema, Ticket, Movie


class ListMoviesView(ListView):
    model = Movie
    template_name = 'movies.html'
    context_object_name = 'movies_list'
    http_method_names = ['get']


class DetailMovieView(ListView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie_detail'
    http_method_names = ['get']


class ListTicketView(ListView):
    model = Ticket
    template_name = 'tickets.html'
    context_object_name = 'tickets_list'
    http_method_names = ['get']


class DetailTicketView(DetailView):
    model = Ticket
    template_name = 'ticket.html'
    context_object_name = 'ticket_detail'
    http_method_names = ['get']


class BuyTicketView(UpdateView):
    http_method_names = ['post']
    pass


class ListCinemaView(ListView):
    model = Cinema
    template_name = 'cinemas.html'
    context_object_name = 'cinema_list'
    http_method_names = ['get']


class DetailCinemaView(DetailView):
    model = Cinema
    template_name = 'cinema.html'
    context_object_name = 'cinema_detail'
    http_method_names = ['get']
