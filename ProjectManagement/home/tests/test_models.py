# Create your tests here.
from django.test import TestCase
from home.models import Category

class TestModels(TestCase):
    def setUp(self):
        self.CatagoryObj = Category.objects.create(name = 'TestCatagory' )
        # self.CatagoryObj.save()
    
    
    #test method:
    def test_catagory(self):
        self.assertEqual(self.CatagoryObj.__str__(),self.CatagoryObj.name)
        