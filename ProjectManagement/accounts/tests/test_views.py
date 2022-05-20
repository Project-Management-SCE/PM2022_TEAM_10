from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User,HelpoUser

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
       
        # self.UserObj = User.objects.create(
        #     username = 'jimb2',
        #     first_name = 'Jim',
        #     last_name = 'Botten',
        #     phone_number = '0524619773',
        #     is_active = True,
        #     is_helpo_user=True,
        #     is_superuser=True,
        #     is_staff=True
        # )
        # self.UserObj.password="123456"
        # self.UserObj.save()
        
        self.user = User.objects.create_user(username='username1', password='password1')
        
        #create helpo user
        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.user,
            city = "BS"
        )

        self.pick_type_url = reverse("pickType")
        self.helpo_porfile_url = reverse('helpo_porfile',kwargs={'pk':self.user.id})
        self.helpo_porfile_fake_url = reverse('helpo_porfile',kwargs={'pk':-1})


    def test_pick_type(self):
        response = self.client.get(self.pick_type_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/PickType.html')

    def test_registration_login(self):   
        self.assertFalse(self.client.login(username='username', password='password')) #before creation
        user1 = User.objects.create_user(username='username', password='password')     
        self.assertTrue(self.client.login(username='username', password='password')) #after Creation

    def test_helpo_profile(self):
        response = self.client.get(self.helpo_porfile_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("registration/helpoProfile.html")
        
        response = self.client.get(self.helpo_porfile_fake_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
