from django.shortcuts import render
from APIRESTful import models
import requests


def index(request):
    r = requests.get('http://127.0.0.1:8000/api/photo')
    photo = models.Photo.objects.get(id=1)
    print(photo.image)
    context = {'ecuson': 'image'}
    return render(request, 'index.html', context)
