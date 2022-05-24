from django.test import TestCase
from .models import Images, Categories, Locations

# Create your tests here.

class ImagesTest(TestCase):

    def setUp(self):

        self.new_category = Categories(name='testing')
        self.new_category.save_category()
        
        self.new_location = Locations(city='Nairobi', country='Kenya')
        self.new_location.save_location()
        
        self.new_picture = Images(image_link='images/picture.jpeg', title='Image title', description='sth random', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Images(image_link='images/photo.jpg', title='Another title', description='sth else more random', category=self.new_category, location=self.new_location)
        self.another_picture.save_image()