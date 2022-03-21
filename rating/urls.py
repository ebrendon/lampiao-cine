# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.RatingListApiView.as_view()),
]