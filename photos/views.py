from django.shortcuts import render
from django.http  import HttpResponse
from .models import Categories, Images, Locations

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def gallery(request):
    images = Images.get_all()
    return render(request, 'photos/photos.html', {'images': images})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        results = Images.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'photos/search.html', {'message':message, 'results':results})
    else:
        message = 'You have not searched any term'
        return render(request, 'photos/search.html', {'message':message})

