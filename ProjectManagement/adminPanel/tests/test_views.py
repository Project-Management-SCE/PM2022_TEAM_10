
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from posts.models import Post
from accounts.models import User,HelpoUser
from home.models import Category
from django.test.client import RequestFactory
import datetime 

class TestViews(TestCase):
    def setUp(self):

        self.UserObj = User.objects.create(
            username = 'jimb2',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = True,
            is_helpo_user=True,
            is_superuser=True,
            is_staff=True
        )
        self.UserObj.password="123456"
        self.UserObj.save()
        
        user1 = User.objects.create_user(username='username', password='password')
        
        #create helpo user
        self.HelpoUserObj = HelpoUser.objects.create(
            user = user1,
            city = "BS"
        )
        
        user1.is_superuser=True
        user1.is_staff=True
        user1.save()
        
        #create Category
        self.category=Category.objects.create(
            name="my new category"
        )
        
        #create post object
        self.post=Post.objects.create(
            user=self.HelpoUserObj,
            city= "Tel-Aviv",
            info="i am writing a new post!",
            category=self.category,
            date=datetime.date.today()
        )
        
        self.adminclient = Client() # Create cliend
        self.adminclient.login(username="username",password="password")

        self.client = Client()
        
        self.AllPosts_url=reverse("posts")
        self.PostDetails_url=reverse("AdminPostDetails", kwargs={'pk':self.post.id})
        self.FakePostDetails_url=reverse("AdminPostDetails", kwargs={'pk':-1})
        self.deletePost_url = reverse('AdminDeletePost',kwargs={'pk':self.post.id})
     
    def test_adminPosts_with_loogin(self):
        response = self.adminclient.get(self.AllPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(Post.objects.get(id=self.post.id),response.context['posts'].get(id=self.post.id))
        self.assertTemplateUsed("admin_posts.html")
    
    def test_adminPosts(self):
        response = self.client.get(self.AllPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    def test_AdminPostDetails_without_login(self):
        response = self.client.get(self.PostDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    def test_AdminPostDetails_with_login_and_fake_post(self):
        response = self.adminclient.get(self.FakePostDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    def test_AdminPostDetails_with_login(self):
        response = self.adminclient.get(self.PostDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("adminPostDetails.html")
        self.assertEqual(response.context['obj'].id,self.post.id)
    
    def test_AdminDeletePost_without_login(self):
        response = self.client.get(self.deletePost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    
    def test_AdminDeletePost_without_login(self):
        response = self.adminclient.get(self.deletePost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_posts.html")
