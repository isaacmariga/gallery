from django.shortcuts import render
from django.http  import HttpResponse
from .models import Categories, Images, Locations

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def gallery(request):
    pictures = Images.get_all()
    locations = Locations.get_all()
    categories = Categories.get_all()
    return render(request, 'photos.html', {'pictures': pictures, 'locations':locations, 'categories':categories})