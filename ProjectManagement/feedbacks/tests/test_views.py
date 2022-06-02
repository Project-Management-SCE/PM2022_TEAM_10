from urllib import response
from django.test import TestCase, Client,tag
from django.urls import reverse
from accounts.models import User,HelpoUser,associationManager
from feedbacks.models import Feedback
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='username', password='password')
        self.user2 = User.objects.create_user(username='username2', password='password2')
        self.user2.is_helpo_user = True
        self.user2.save()
        self.user3 = User.objects.create_user(username='username3', password='password3')
        self.user3.is_association_manager = True
        self.user3.save()


        self.UserObj = User.objects.create(
            username = 'user',
            password = 'pass',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = True,
            is_helpo_user=True,
            is_superuser=True,
            is_staff=True
        )

        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.user2,
            city = "BS"
        )

        self.associationManagerObj = associationManager.objects.create(
            user = self.user3,
            association_number = '123456'
        )

        
        self.sendFeedback_url = reverse('sendFeedback')

    @tag('IT')
    def test_sendFeedback(self):
        #if the user is not helpo or manager he cannot send feedback
        self.client.login(username="username",password="password")
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("erro_page.html")
        
        #connect to helpo user 
        self.client.login(username="username2",password="password2")

        #GET
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")       

        #POST 
        response = self.client.post(self.sendFeedback_url,data = {'subject':'subj','content':'conthelpo'},follow=True)  
        self.assertEqual(200,response.status_code)
        f = Feedback.objects.filter(content='conthelpo').first()
        self.assertIsNotNone(f)
        self.assertTemplateUsed("sendFeedback.html") 

        #connect to helpo asso manager 
        self.client.login(username="username3",password="password3")

        #GET
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")       

        # #POST 
        response = self.client.post(self.sendFeedback_url,data = {'subject':'subj','content':'contmanager'},follow=True)  
        self.assertEqual(200,response.status_code)
        f = Feedback.objects.filter(content='contmanager').first()
        self.assertIsNotNone(f)
        self.assertTemplateUsed("sendFeedback.html")        
        
        