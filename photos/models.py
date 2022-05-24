from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to='images/', default='SOME STRING')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)


class Categories(models.Model):
    name = models.CharField(max_length=30)


class Locations(models.Model):
    city = models.CharField(max_length=30)