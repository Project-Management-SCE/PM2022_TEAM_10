
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from posts.views import updateFilters
from accounts.models import User,HelpoUser
from posts.models import Post,Category
import posts.views as p
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
        
        self.createPost_url = reverse('createPost')
        self.showMyPosts_url = reverse('showMyPosts', kwargs={'pk':self.HelpoUserObj.user.id})
        self.editPost_url = reverse('editPost', kwargs={'pk':self.post.id})
        self.showAllPost_url = reverse('showAllPosts')
        self.resertFilters_url = reverse('resetFilters')


    def test_createPost(self):
        self.client.login(username="username",password="password")
        response = self.client.get(self.createPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.user1,response.context['user_obj'])
        self.assertTemplateUsed("createPostForm.html")
        
        self.client.post(self.createPost_url)
        self.assertTemplateUsed("createPostForm.html")
        

    def test_showMyPosts(self):
        response = self.client.get(self.showMyPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("myPosts.html")
        
        # Check error page
        self.client.login(username="username",password="password")
        self.assertTemplateUsed("error_page.html")


    def test_editPost(self):
        response = self.client.get(self.editPost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("editPost.html")
        
        # Check error page
        self.client.login(username="username",password="password")
        self.assertTemplateUsed("error_page.html")
    
    def test_showAllPosts(self):
        response = self.client.get(self.showAllPost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("allPosts.html")

    def test_showAllPostsWithData(self):
        response = self.client.post(reverse('showAllPosts'), data ={})
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("allPosts.html")

    def test_updateFilters(self):
        p.updateFilters(self.category,"ofaqim",True)
        self.assertEqual(self.category,p.Cat_Filter)
        self.assertEqual("ofaqim",p.City_Filter)
        self.assertTrue(p.Asking_Filter)

    def test_resetFilters(self):
        response = self.client.get(self.resertFilters_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertIsNone(p.Cat_Filter)
        self.assertIsNone(p.City_Filter)
        self.assertIsNone(p.Asking_Filter)
        self.assertTemplateUsed("allPosts.html")
    
    
