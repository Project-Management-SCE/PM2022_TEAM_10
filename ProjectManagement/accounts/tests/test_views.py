from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User,HelpoUser,associationManager

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(username='username1', password='password1')
        self.user2 = User.objects.create_user(username='username2', password='password2')

        self.associationManagerObj = associationManager.objects.create(
            user = self.user,
            association_number = '123456'
        )

        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.user2,
            city = "BS"
        )

        self.logout_url = reverse('logout')
        self.pick_type_url = reverse("pickType")
        self.searchUsers_url= reverse('searchUsers')
        self.helpo_porfile_fake_url = reverse('helpo_porfile',kwargs={'pk':-1})
        self.helpo_porfile_url = reverse('helpo_porfile',kwargs={'pk':self.user.id})
        self.updateHelpoUser_url = reverse('updateHelpoUser',kwargs={'pk':self.HelpoUserObj.user.id})
        self.updateAssociationManager_url = reverse('updateAssociationManager',kwargs={'pk':self.associationManagerObj.user.id})


    def test_updateHelpoUser(self):
        self.client.login(username="username2",password="password2")
        response = self.client.get(self.updateHelpoUser_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/updateHelpoUser.html')



    def test_updateAssociationManager(self):
        self.client.login(username="username1",password="password1")
        response = self.client.get(self.updateAssociationManager_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/updateAssociationManager.html')



    def test_pick_type(self):
        response = self.client.get(self.pick_type_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/PickType.html')

    def test_registration_login(self):   
        self.assertFalse(self.client.login(username='username', password='password')) #before creation
        User.objects.create_user(username='username', password='password')     
        self.assertTrue(self.client.login(username='username', password='password')) #after Creation

    def test_helpo_profile(self):
        response = self.client.get(self.helpo_porfile_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("registration/helpoProfile.html")
        
        response = self.client.get(self.helpo_porfile_fake_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

    def test_searchUsers(self):
        response = self.client.get(self.searchUsers_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("searchUsers.html")
        self.assertEqual(list(HelpoUser.objects.all()),list(response.context["context"]))

    def test_logout(self):
        self.client.login(username="username1",password="password1")
        self.client.get(self.logout_url)  
        self.assertTemplateUsed("index.html")

