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


def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        res = Images.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'results':res})
    else:
        message = 'You have not searched any term'
        return render(request, 'search.html', {'message':message})