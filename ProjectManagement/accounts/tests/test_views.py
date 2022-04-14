from urllib import response
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.pick_type_url = reverse("pickType")
    
    def test_pick_type(self):
        response = self.client.get(self.pick_type_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/PickType.html')

