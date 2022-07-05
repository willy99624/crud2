from django.urls import path
from movies.views import ActorView, MovieView

urlpatterns = [
    path('/actors', ActorView.as_view()),
    path('/movies', MovieView.as_view()),
]
