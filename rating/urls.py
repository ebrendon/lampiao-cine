from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('listRating/', views.listRating, name='list-rating'),
    path('deleteRating/<pk>', views.deleteRating, name="delete-rating"),
    path('createRating/<pk>', views.createRating, name='create-rating' ),
    path('updateRating/<pk>', views.updateRating, name='update-rating'),
] 