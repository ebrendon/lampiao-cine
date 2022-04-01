# from django.conf.urls import url
from django.urls import path, include
from cinema.views import DetailCinemaView, DetailMovieView, ListCinemaView, ListMoviesView


urlpatterns = [
    path('', ListMoviesView.as_view(), name='movies'),
    path('movies/<int:id>', DetailMovieView.as_view(), name='movie detail'),
    path('cinemas', ListCinemaView.as_view(), name='cinemas'),
    path('cinemas/<int:id>', DetailCinemaView.as_view(), name='cinema detail'),
]
