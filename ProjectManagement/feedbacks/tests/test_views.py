from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='username', password='password')
        self.sendFeedback_url = reverse('sendFeedback')

        
    def test_sendFeedback(self):
        self.client.login(username="username",password="password")
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")
        
        
        