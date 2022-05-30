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

    def tearDown(self):
        Categories.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete()

    def test_instances(self):
        self.assertTrue(isinstance(self.new_picture,Images))
        self.assertTrue(isinstance(self.new_category, Categories))
        self.assertTrue(isinstance(self.new_location, Locations))

    def test_save_image(self):
        self.assertTrue(len(Images.objects.all()) == 2)

    def test_delete_image(self):
        self.new_picture.delete_image()
        self.assertTrue(len(Images.objects.all()) == 1)

    def test_update_image(self):
        update_test = self.new_picture.update_image('images/updated.png')
        self.assertEqual(update_test.image_link, 'images/updated.png')

    def test_get_all(self):
        pictures = Images.get_all()
        # print(pictures)

    def test_get_image_by_id(self):
        obtained_image = Images.get_image_by_id(self.another_picture.id)
        # print(obtained_image.title)

        obtained_image = Images.search_image(self.new_picture.category)
        print(obtained_image) 

    def test_filter_by_location(self):
        obtained_image = Images.filter_by_location(self.another_picture.location)
        print(obtained_image)



class CategoryTest(TestCase):
    def setUp(self):
        self.new_category = Categories(name='categoryA')
        self.new_category.save_category()

    def tearDown(self):
        Categories.objects.all().delete()

    def test_save_category(self):
        self.assertTrue(len(Categories.objects.all()) == 1)     

    def test_delete_category(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Categories.objects.all()) == 0)    

    def test_update_category(self):
        update_cat = Categories.update_category('categoryA', 'CategoryB')
        self.assertEqual(update_cat.name, 'CategoryB')




class LocationTest(TestCase):
    def setUp(self):
        self.new_location = Locations(city='lost city', country='unknown')
        self.new_location.save_location()

    def test_save_location(self):
        self.assertTrue(len(Locations.objects.all()) == 1)     

    def test_delete_location(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Locations.objects.all()) == 0)

    def test_update_location(self):
        update_locale = Locations.update_location('unknown', 'paperTown')
        self.assertEqual(update_locale.city, 'paperTown')

    def test_get_all(self):
        locations = Locations.get_all()
        print(locations)