from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User,HelpoUser,associationManager

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
    

    #registration -> login integration
    def test_pick_type(self):   
        self.assertFalse(self.client.login(username='username', password='password')) #before creation
        user1 = User.objects.create_user(username='username', password='password')     
        self.assertTrue(self.client.login(username='username', password='password')) #after Creation creation


