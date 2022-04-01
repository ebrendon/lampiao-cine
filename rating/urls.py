from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('listRating/', views.listRating, name='list-rating'),
    path('listReview/', views.listReview, name='list-review'),
    path('deleteReview/<pk>', views.deleteReview, name="deleteReview"),
    path('deleteRating/<pk>', views.deleteRating, name="deleteRating"),
    path('createRating/', views.createRating),
    path('createReview/', views.createReview),
    path('updateRating/', views.updateRating),
    path('updateReview/', views.updateReview),
] 