import imp
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client() # Create cliend
    
        self.index_url = reverse("index") # Get url with name "index"
    
    def test_index(self):
        response = self.client.get(self.index_url)      # Get response from the url
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'index.html') # Check if the right page has returned