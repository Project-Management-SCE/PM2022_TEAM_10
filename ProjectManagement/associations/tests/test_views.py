
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from associations.models import Association,volunteeringRequest,Rank
from accounts.models import User,HelpoUser,associationManager
from django.contrib.auth import login
from django.test.client import RequestFactory
from associations.views import updateAssociationRank,getRating
from home.models import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile


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
        user1 = User.objects.create_user(username='username', password='password')     

        self.UserObj = User.objects.create(
            username = 'jimb',
            password = 'A!123456',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = False
        )

        self.associationManagerObj = associationManager.objects.create(
            user = user1,
            association_number = '123456'
        )


        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.UserObj,
            city = "BS"
        )

        self.assoObj2 = Association.objects.create(
            id = '123456',
            manager= self.associationManagerObj,
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
        
        self.reqObj = volunteeringRequest.objects.create(
            id='222',
            association = self.assoObj,
            user = self.HelpoUserObj,
            info ="sdfsdfs"
        )

        self.rankObj = Rank.objects.create(
            user = self.HelpoUserObj,
            association = self.assoObj,
            rank = 5
        )

        self.image = Image.objects.create(
            asso = self.assoObj2,
            img = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        self.client = Client() # Create cliend

        self.user_client = Client() # Create cliend
        self.user_client.login(username = 'jimb', password = 'A!123456')

        self.association_manager_client = Client()
        self.association_manager_client.login(username='username', password='password')

        self.profile_url=reverse('profile', kwargs={'pk':self.assoObj.id})
        self.all_url = reverse("All") 
        self.volunteer_url=reverse("submitVolunteeringRequest", kwargs={'pk':self.assoObj.id})
        self.requests_url = reverse('volunteersRequests',kwargs={'pk':self.assoObj.id})
        self.show_request_url = reverse('showRequest',kwargs={'pk':self.assoObj.id, 'r_pk':self.reqObj.id})
        self.deleteVolRequest_url = reverse('deleteVolRequest',kwargs={'pk':self.reqObj.id})
        self.edit_association_url = reverse('editAssociation',kwargs={'pk':self.assoObj2.id})
        self.rankAssociation_url = reverse('rankAssociation',kwargs={'pk':self.assoObj.id})
        self.associationPhotos_url = reverse('associationPhotos',kwargs={'pk':self.assoObj2.id})
        self.deletePhoto_url = reverse('deletePhoto',kwargs={'asso_pk':self.assoObj2.id,'photo_pk': self.image.id})
        self.deletePhoto_url_error = reverse('deletePhoto',kwargs={'asso_pk':self.assoObj2.id,'photo_pk': -1 })


    def test_rankAssociation(self):
        response = self.association_manager_client.post(self.rankAssociation_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        response = self.client.post(self.rankAssociation_url,follow=True) 
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("profile.html")

    def test_updateAssociationRank(self):
        updateAssociationRank(self.assoObj.id)

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

    def test_edit_association(self):
        self.client.login(username="username",password="password")
        response = self.client.get(self.edit_association_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.assoObj2,response.context['obj'])
        self.assertTemplateUsed("updateAssoDetails.html")

    def test_edit_association_error(self):
        response = self.client.get(self.edit_association_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

#upload photos tests    
    def test_associationPhotos(self):
        response = self.client.get(self.associationPhotos_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        self.client.login(username="username",password="password")
        response = self.client.get(self.associationPhotos_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("assoPhotos.html")

        response = self.client.post(self.associationPhotos_url, data ={'img':tempfile.NamedTemporaryFile(suffix=".jpg")})  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("assoPhotos.html")

    def test_deletePhoto(self):
        response = self.client.get(self.deletePhoto_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        self.client.login(username="username",password="password")
        response = self.client.get(self.deletePhoto_url_error,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        
        self.client.login(username="username",password="password")
        response = self.client.get(self.deletePhoto_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("assoPhotos.html")


    # def test_deleteVolRequest_url(self):
    #     response = self.client.get(self.deleteVolRequest_url)  
    #     self.assertEqual(200,response.status_code)
    #     self.assertTemplateUsed("volunteersRequests.html")

    # def test_submit_request_url(self):
    #     self.client.login(username='username', password='password')
    #     response = self.client.get(self.submit_request_url)      
    #     self.assertEqual(response.status_code, 200)   
    #     self.assertTemplateUsed(response, 'volunteerForm.html')