
from django.urls import path
from cinema.views import DetailCinemaView, DetailMovieView, HomeView, ListCinemaView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/<int:pk>', DetailMovieView.as_view(), name='movie_detail'),
    path('cinemas/<int:pk>', DetailCinemaView.as_view(), name='cinema_detail'),
]
