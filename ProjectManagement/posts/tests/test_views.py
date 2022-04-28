from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User,HelpoUser,associationManager
from home.models import Category
from posts.forms import createPostForm
from posts.models import Post



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        user1 = User.objects.create_user(username='username', password='password')  

        self.HelpoUserObj = HelpoUser.objects.create(
            user = user1,
            city = "BS"
        )   
        self.client.login(username='username', password='password')

        self.categoryObj = Category.objects.create(name="c1")
        self.create_post_url = reverse("createPost") 


    #registration -> login integration
    def test_create_post(self):   
        self.assertTrue(self.client.login(username='username', password='password')) 
        response = self.client.get(self.create_post_url)      # Get response from the url
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'createPostForm.html') # Check if the right page has returned

    def test_create_post_POST(self):
        self.client.login(username='username', password='password')
        form = createPostForm(data={'info':'i am writing a new post!','category':'0'})
        self.assertTrue(form.is_valid())
        response = self.client.post(self.create_post_url, form.data,follow=True)
        self.assertEqual(response.status_code, 200)     # Check status
        self.assertTemplateUsed(response, 'index.html') # Check if the right page has returned