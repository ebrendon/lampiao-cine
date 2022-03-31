from django.urls import path, include
from . import views

urlpatterns = [
    path('listRating/', views.listRating),
    path('listReview/', views.listReview),
    path('deleteRating/', views.deleteRating),
    path('deleteReview/', views.deleteReview),
    path('createRating/', views.createRating),
    path('createReview/', views.createReview),
] 