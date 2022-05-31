from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User,HelpoUser
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='username', password='password')

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
            user = self.UserObj,
            city = "BS"
        )
        
        self.sendFeedback_url = reverse('sendFeedback')
        
    def test_sendFeedback(self):
        self.client.login(username="username",password="password")
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")
        
        self.client.login(username="user",password="pass")
        response = self.client.post(self.sendFeedback_url,data = {'subject':'subj','content':'cont'},follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")        
        
        