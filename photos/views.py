from django.shortcuts import render
from django.http  import HttpResponse
from .models import Categories, Images, Locations

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def gallery(request):
    images = Images.get_all()
    locations = Locations.get_all()
    return render(request, 'photos.html', {'images': images, 'locations':locations})