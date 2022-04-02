# from django.conf.urls import url
from django.shortcuts import redirect
from django.urls import path
from cinema.views import DetailCinemaView, DetailMovieView, ListCinemaView, ListMoviesView


urlpatterns = [
    path('movies/', ListMoviesView.as_view(), name='movie_list'),
    path('movies/<int:pk>', DetailMovieView.as_view(), name='movie_detail'),
    path('cinemas', ListCinemaView.as_view(), name='cinema_list'),
    path('cinemas/<int:pk>', DetailCinemaView.as_view(), name='cinema_detail'),
    path('', lambda _: redirect('movies/')),
]
