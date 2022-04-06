from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('listMovieRating/<pk>', views.listMovieRating, name='list-movie-rating'),
    path('listUserRating/', views.listUserRating, name='list-user-rating'),
    path('deleteRating/<pk>', views.deleteRating, name="delete-rating"),
    path('createRating/<pk>', views.createRating, name='create-rating' ),
    path('updateRating/<pk>', views.updateRating, name='update-rating'),
] 