from django.urls import path
from MovieRater.views import *

urlpatterns = [
    path('',MovieList,name="home"),
    path('movies/<name>',MovieDetails),
]
