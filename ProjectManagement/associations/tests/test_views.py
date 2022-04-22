import imp
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client() # Create cliend
    
        self.all_url = reverse("All") # Get url with name "index"
    
    def test_index(self):
        response = self.client.get(self.all_url)      # Get response from the url
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'table.html') # Check if the right page has returned
        
        
    def test_profile(self):
        response = self.client.get(self.all_url)      # Get response from the url
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'table.html') # Check if the right page has returned
        