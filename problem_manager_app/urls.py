from django.urls import path
from .views import *


urlpatterns = [
    path("platfroms/", PlatfromView.as_view()),
    path('tags/', TagView.as_view()),
    path('solved-count/', CountProblemsView.as_view()),
    path('solved-problems/', SolvedProblemsView.as_view()),
]