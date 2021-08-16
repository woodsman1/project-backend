from django.urls import path
from .views import *


urlpatterns = [
    path("platfroms/", PlatfromView.as_view()),
    path('tags/', TagView.as_view()),
    path('solved-count/', CountProblemsView.as_view()),
    path('solved-problems/', SolvedProblemsView.as_view()),
    path('unsolved-problems/', UnSolvedProblemView.as_view()),
    path('problem/', ProblemView.as_view()),
    path('problem-update/<int:pk>/', ProblemView.as_view()),
]