from django.shortcuts import render
from django.http  import HttpResponse
from .models import Categories, Images, Locations

# Create your views here.
def gallery(request):
    images = Images.get_all()
    locations = Locations.get_all()
    return render(request, 'photos/photos.html', {'images': images, 'locations':locations})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        results = Images.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'photos/search.html', {'message':message, 'results':results})
    else:
        message = 'You have not searched any term'
        return render(request, 'photos/search.html', {'message':message})

def location(request,locale):
    images = Images.filter_by_location(locale)
    return render(request, 'location.html', {'results':images})