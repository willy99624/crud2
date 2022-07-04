import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog

class OwnerView(View):

    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name = data['name'], email = data['email'], age = data['age'])
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            dogs = owner.dog_set.all()
            dog_array = []

            for dog in dogs:
                dogs = owner.dog_set.all()
                dog_information = ({'name':dog.name, 'age':dog.age})
                dog_array.append(dog_information)

            results.append({'name':owner.name, 'email':owner.email, 'age':owner.age, 'my_dog':dog_array})

        return JsonResponse({'results':results}, status=200)

class DogView(View):

    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(name = data['name'], age = data['age'], owner = Owner.objects.get(name = data['owner']))
        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append({'name':dog.name, 'age':dog.age, 'owner':dog.owner.name})

        return JsonResponse({'results':results}, status=200)
