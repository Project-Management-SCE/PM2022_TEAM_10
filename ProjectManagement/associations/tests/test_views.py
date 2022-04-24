import imp
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from associations.models import Association


class TestViews(TestCase):
    def setUp(self):
        self.assoObj = Association.objects.create(
            id = '123123123',
            manager= None,
            name='asso1',
            category='category1',
            vol_num='10',
            city = 'Tel Aviv',
            street= 'Dizengoff',
            apartment='54',
            phone='0501231231',
            info='',
            email='asso1@associations.com'
        )
        
        self.client = Client() # Create cliend
        self.profile_url=reverse('profile', kwargs={'pk':self.assoObj.id})
        self.all_url = reverse("All") # Get url with name "index"
        self.volunteer_url=reverse("submitVolunteeringRequest", kwargs={'pk':self.assoObj.id})
    
    def test_index(self):
        response = self.client.get(self.all_url)      # Get response from the url
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'table.html') # Check if the right page has returned
        
        
    def test_profile(self):
        response = self.client.get(self.profile_url)  # Get response from the url
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.assoObj.name,response.context['obj'].name)
        self.assertTemplateUsed("profile.html")
        
    
        