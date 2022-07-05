import json

from django.http import JsonResponse
from django.views import View

from .models import Actor, Movie

class ActorView(View):
    def get(self, request):
        results = []
        actors = Actor.objects.all()
        for actor in actors:
            results.append({"first_name" : actor.first_name, "last_name" : actor.last_name, "movies_title" : list(actor.movie.values('title'))})
        return JsonResponse({'results' : results}, status = 200)
        
class MovieView(View):
    def get(self, request):
        results = []
        movies = Movie.objects.all()
        for movie in movies:
            actors_name = []
            actors = movie.actor_set.all()
            for actor in actors:
                actors_name.append({"actors_first_name" : actor.first_name})
            results.append({"movies_title" : movie.title, "running_time" : movie.running_time, "actors_first_name" : actors_name})
        return JsonResponse({'results' : results}, status = 200)
