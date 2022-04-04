from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from cinema.models import Cinema, Ticket, Movie
from django.core import serializers


class HomeView(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movies'
    http_method_names = ['get']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cinemas = Cinema.objects.all()
        context['cinemas'] = cinemas
        return context


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
    context_object_name = 'cinema'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cinema_id = context['cinema'].id
        context['tickets'] = serializers.serialize(
            "json", Ticket.objects.filter(cinema=cinema_id))
        return context
