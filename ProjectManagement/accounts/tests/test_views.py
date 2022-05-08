from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.pick_type_url = reverse("pickType")
    
    def test_pick_type(self):
        response = self.client.get(self.pick_type_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/PickType.html')

    def test_registration_login(self):   
        self.assertFalse(self.client.login(username='username', password='password')) #before creation
        user1 = User.objects.create_user(username='username', password='password')     
        self.assertTrue(self.client.login(username='username', password='password')) #after Creation creation

