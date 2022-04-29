from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve
from associations.views import All,profile,showRequest,volunteersRequests,editAssociation,submitVolunteeringRequest,deleteVolRequest
from accounts.models import User,HelpoUser,associationManager
from associations.models import Association,volunteeringRequest


class TestUrls(TestCase):
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



    
    def test_all_associations_page_url_is_resolved(self):
        url = reverse('All')
        self.assertEqual(resolve(url).func, All)

    def test_all_profile_url_is_resolved(self):
        url = reverse('profile', kwargs={'pk':self.assoObj.id})
        self.assertEqual(resolve(url).func, profile)
    
    def test_all_editAssociation_url_is_resolved(self):
        url = reverse('editAssociation', kwargs={'pk':self.assoObj.id})
        self.assertEqual(resolve(url).func, editAssociation)
    
    def test_all_volunteersRequest_url_is_resolved(self):
        url = reverse('submitVolunteeringRequest', kwargs={'pk':self.assoObj.id})
        self.assertEqual(resolve(url).func, submitVolunteeringRequest)

    def test_all_volunteersRequests_url_is_resolved(self):
        url = reverse('volunteersRequests', kwargs={'pk':self.assoObj.id})
        self.assertEqual(resolve(url).func, volunteersRequests)

    def test_all_showRequest_url_is_resolved(self):
        url = reverse('showRequest', kwargs={'pk':self.assoObj.id, 'r_pk':self.reqObj.id})
        self.assertEqual(resolve(url).func, showRequest)

    def test_all_deleteVolRequest_url_is_resolved(self):
        url = reverse('deleteVolRequest', kwargs={'pk':self.reqObj.id})
        self.assertEqual(resolve(url).func, deleteVolRequest)