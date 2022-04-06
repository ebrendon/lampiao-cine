
from django.urls import path
from cinema.views import DetailCinemaView, DetailMovieView, HomeView, ListCinemaView, ListTicketsFromMovie


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/<int:pk>', DetailMovieView.as_view(), name='movie_detail'),
    path('cinemas/<int:pk>', DetailCinemaView.as_view(), name='cinema_detail'),
    path('tickets/<int:cinema_id>/<int:movie_id>',
         ListTicketsFromMovie.as_view(), name="list_tickets_movie")
]
