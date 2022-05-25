from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.gallery, name ='gallery'),
    url(r'^category/', views.category, name='category'),
    url(r'^location/', views.location, name='location'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)