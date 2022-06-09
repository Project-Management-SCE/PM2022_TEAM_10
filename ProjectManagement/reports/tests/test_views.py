from django.test import TestCase, Client,tag
from django.urls import reverse
from accounts.models import User,HelpoUser
from posts.models import Post,Category
from reports.models import PostReport
import datetime

class TestViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='username', password='password')     

        self.UserObj = User.objects.create(
            id = '123',
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
        
        self.HelpoUserObj2 = HelpoUser.objects.create(
            user = self.UserObj,
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
        self.reportUser_url = reverse('reportUser', kwargs={'pk':self.UserObj.id})
        self.createPost_url = reverse('createPost')

    @tag('UT')
    def reportUser(self):
        response = self.client.get(self.reportUser_url)  # Get response from the url
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.UserObj , response.context['reported_obj'])
        self.assertTemplateUsed("userReportPage.html")
    
    @tag('IT')    
    def test_createReportPost_with_login(self):
        #create post instance
        #without login will send him to login page
        response = self.client.get(self.createReportPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("login.html")

        #login to user
        self.client.login(username="username",password="password")

        #error page  -  post not found
        response = self.client.get(self.createReportPost_postError_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        
        #creating a new post
        self.client.post(self.createPost_url)
        self.assertTemplateUsed("createPostForm.html")
        response = self.client.post(self.createPost_url,data ={'info':'postreport','city':'BS','is_asking':True,'category':self.category.id}, follow=True)
        p = Post.objects.filter(info='postreport').first()
        self.assertIsNotNone(p)    #object exists after user is authenticated!

        self.createReportPost_url = reverse('createReportPost', kwargs={'pk':p.id})

        #post found
        #GET the page
        response = self.client.get(self.createReportPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("postReportPage.html")
        
        #POST - creating a new report 
        self.client.post(self.createReportPost_url,{'info':'abc'})
        pr = PostReport.objects.filter(info='abc')
        self.assertIsNotNone(pr)
        self.assertTemplateUsed("index.html")

        #Try to report again on the same post will now be allowed
        self.client.post(self.createReportPost_url,{'info':'abcd'})
        pr = PostReport.objects.filter(info='abcd')
        self.assertEqual([],list(pr))
        self.assertTemplateUsed("error_page.html")