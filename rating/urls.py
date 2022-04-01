from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('listRating/', views.listRating, name='list-rating'),
    path('deleteRating/<pk>', views.deleteRating, name="deleteRating"),
    path('createRating/', views.createRating),
    path('updateRating/', views.updateRating),
    # path('listReview/', views.listReview, name='list-review'),
    # path('deleteReview/<pk>', views.deleteReview, name="deleteReview"),
    # path('createReview/', views.createReview),
    # path('updateReview/', views.updateReview),
] 