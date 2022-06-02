
from urllib import response
from django.test import TestCase, Client,tag
from django.urls import reverse
from posts.views import updateFilters
from accounts.models import User,HelpoUser
from posts.models import Post,Category
import posts.views as p
import datetime


class TestViews(TestCase):
    #prepate db and objects for the tests
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
        self.showAllPost_url = reverse('showAllPosts')
        self.resertFilters_url = reverse('resetFilters')

    @tag('IT')
    def test_createPost(self):
        #if user not logged in, he can't create a post
        #check GET
        response = self.client.get(self.createPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("login.html")

        #check POST
        response = self.client.post(self.createPost_url,data ={'info':'postdbchek1','city':'BS','is_asking':True,'category':self.category},follow=True)
        self.assertEqual(200,response.status_code)
        p = Post.objects.filter(info='postdbchek1').first()
        self.assertIsNone(p)    #object didnot exists!

        #preform login to a user
        self.client.login(username="username",password="password")

        #create post
        #check GET
        response = self.client.get(self.createPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.user1,response.context['user_obj'])
        self.assertTrue(response.context['user_obj'].is_authenticated)
        self.assertTemplateUsed("createPostForm.html")
        
        #check POST
        self.client.post(self.createPost_url)
        self.assertTemplateUsed("createPostForm.html")
        response = self.client.post(self.createPost_url,data ={'info':'postdbchek1','city':'BS','is_asking':True,'category':self.category.id}, follow=True)
        p = Post.objects.filter(info='postdbchek1').first()
        self.assertIsNotNone(p)    #object exists after user is authenticated!
        
    @tag('IT')
    def test_showMyPosts(self):
        #set the url with param of HelpoUserObj id
        self.showMyPosts_url = reverse('showMyPosts', kwargs={'pk':self.HelpoUserObj.user.id})

        #if the user requested the site page is not the user id in url param
        response = self.client.get(self.showMyPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        
        # Check error page
        self.client.login(username="username",password="password")
        response = self.client.get(self.showMyPosts_url)

        #check if the data that send is the correct data
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.HelpoUserObj.user.id,response.context['user'].id)
        posts = Post.objects.filter(user_id=self.HelpoUserObj.user.id)
        self.assertEqual(list(posts),list(response.context['posts']))
        self.assertTemplateUsed("myPosts.html")

    @tag('IT')
    def test_editPost(self):
        #set the url with param of HelpoUserObj id
        self.editPost_url = reverse('editPost', kwargs={'pk':self.post.id})

        #check GET
        response = self.client.get(self.editPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        #check POST
        response = self.client.post(self.editPost_url,data ={'info':'i am writing a new post!','city':'BS','is_asking':False,'category':self.category},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        p = Post.objects.filter(info='i am writing a new post!').first()
        self.assertNotEqual('BS',p.city)    #object changed his attribute

        #preform login to a user
        self.client.login(username="username",password="password")

        #create post
        #check GET - Get the correct page only if logged in to the correct user
        response = self.client.get(self.editPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.user1,response.context['obj'].user)
        self.assertTrue(response.context['obj'].user.is_authenticated)
        self.assertTemplateUsed("editPost.html")
        
        #check POST - update FORM
        response = self.client.post(self.editPost_url,data ={'info':'i am writing a new post!','city':'BS','is_asking':False,'category':self.category.id}, follow=True)
        self.assertTemplateUsed("editPost.html")
        p = Post.objects.filter(info='i am writing a new post!').first()
        self.assertEqual('BS',p.city)    #object changed his attribute
    
    @tag('UT')
    def test_showAllPosts(self):
        response = self.client.get(self.showAllPost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("allPosts.html")

    @tag('UT')
    def test_showAllPostsWithData(self):
        response = self.client.post(reverse('showAllPosts'), data ={})
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("allPosts.html")

    @tag('UT') 
    def test_updateFilters(self):
        p.updateFilters(self.category,"ofaqim",True)
        self.assertEqual(self.category,p.Cat_Filter)
        self.assertEqual("ofaqim",p.City_Filter)
        self.assertTrue(p.Asking_Filter)

    @tag('UT')
    def test_resetFilters(self):
        response = self.client.get(self.resertFilters_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertIsNone(p.Cat_Filter)
        self.assertIsNone(p.City_Filter)
        self.assertIsNone(p.Asking_Filter)
        self.assertTemplateUsed("allPosts.html")
    
    
