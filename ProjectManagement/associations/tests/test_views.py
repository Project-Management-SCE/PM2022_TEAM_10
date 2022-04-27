
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from associations.models import Association,volunteeringRequest
from accounts.models import User,HelpoUser,associationManager
from django.contrib.auth import login
from django.test.client import RequestFactory

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

        self.UserObj = User.objects.create(
            username = 'jimb',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = False
        )

        self.associationManagerObj = associationManager.objects.create(
            user = self.UserObj,
            association_number = '123456'
        )

        # user1 = User.objects.create_user(username='username', password='password')     

        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.UserObj,
            city = "BS"
        )
        
        self.reqObj = volunteeringRequest.objects.create(
            id='222',
            association = self.assoObj,
            user = self.HelpoUserObj,
            info ="sdfsdfs"
        )


        self.client = Client() # Create cliend

        self.profile_url=reverse('profile', kwargs={'pk':self.assoObj.id})
        self.all_url = reverse("All") 
        self.volunteer_url=reverse("submitVolunteeringRequest", kwargs={'pk':self.assoObj.id})
        self.requests_url = reverse('volunteersRequests',kwargs={'pk':self.assoObj.id})
        self.show_request_url = reverse('showRequest',kwargs={'pk':self.assoObj.id, 'r_pk':self.reqObj.id})
        # self.submit_request_url = reverse('submitVolunteeringRequest',kwargs={'pk':self.assoObj.id})
        self.deleteVolRequest_url = reverse('deleteVolRequest',kwargs={'pk':self.reqObj.id})


    def test_index(self):
        response = self.client.get(self.all_url)      # Get response from the url
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'table.html') # Check if the right page has returned
        
        
    def test_profile(self):
        response = self.client.get(self.profile_url)  # Get response from the url
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.assoObj.name,response.context['obj'].name)
        self.assertTemplateUsed("profile.html")
        
    def test_vol_requests(self):
        response = self.client.get(self.requests_url)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.assoObj,response.context['asso_obj'])
        self.assertTemplateUsed("volunteerRequests.html")

    def test_show_vol_request(self):
        response = self.client.get(self.show_request_url)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.HelpoUserObj,response.context['helpo_user'])
        self.assertEqual(self.assoObj,response.context['asso_obj'])
        self.assertEqual(self.reqObj,response.context['request'])
        self.assertTemplateUsed("showRequest.html")
    
    # def test_deleteVolRequest_url(self):
    #     response = self.client.get(self.deleteVolRequest_url)  
    #     self.assertEqual(200,response.status_code)
    #     self.assertTemplateUsed("volunteersRequests.html")

    # def test_submit_request_url(self):
    #     self.client.login(username='username', password='password')
    #     response = self.client.get(self.submit_request_url)      
    #     self.assertEqual(response.status_code, 200)   
    #     self.assertTemplateUsed(response, 'volunteerForm.html')