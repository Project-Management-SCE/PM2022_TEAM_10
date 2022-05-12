
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User,HelpoUser
from posts.models import Post,Category
import datetime

class TestViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='username', password='password')     

        self.UserObj = User.objects.create(
            username = 'jimb',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = False
        )

        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.user1,
            city = "BS"
        )
        
        self.category=Category.objects.create(
            id='1',
            name="my new category"
        )
        
        self.post=Post.objects.create(
            user=self.HelpoUserObj,
            city= "Tel-Aviv",
            info="i am writing a new post!",
            category=self.category,
            date=datetime.datetime.now()
        )
        
        self.client = Client() 
        
        self.createReportPost_url = reverse('createReportPost', kwargs={'pk':self.post.id})
        self.createReportPost_postError_url = reverse('createReportPost',kwargs={'pk':'345'})



    def test_createReportPost_with_login(self):
        #error page  -  post not found
        self.client.login(username="username",password="password")
        response = self.client.get(self.createReportPost_postError_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        #post found - GET
        response = self.client.get(self.createReportPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("postReportPage.html")
        
        #post found - POST
        self.client.post(self.createReportPost_url,{'info':'abc'})
        self.assertTemplateUsed("index.html")
        
    def test_createReportPost_without_login(self):
        response = self.client.get(self.createReportPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("postReportPage.html")
