
import imp
from operator import truediv
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from posts.models import Post
from accounts.models import User,HelpoUser
from adminPanel.models import AdminMessage
#from home.models import Category
from django.test.client import RequestFactory
import datetime 

class TestViews(TestCase):
    def setUp(self):

        self.factory = RequestFactory()

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
        
        self.user1 = User.objects.create_user(username='username', password='password')
        
        #create helpo user
        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.user1,
            city = "BS"
        )
        
        self.user1.is_superuser=True
        self.user1.is_staff=True
        self.user1.save()
        
        #create Category
        # self.category=Category.objects.create(
        #     name="my new category"
        # )
        
        #create post object
        self.post=Post.objects.create(
            user=self.HelpoUserObj,
            city= "Tel-Aviv",
            info="i am writing a new post!",
           # category=self.category,
            date=datetime.date.today()
        )

        self.adminMsg = AdminMessage.objects.create(
            content = "ABCDEFG"
        )
        
        self.adminclient = Client() # Create cliend
        self.adminclient.login(username="username",password="password")

        self.client = Client()
        
        self.AllPosts_url=reverse("posts")
        self.PostDetails_url=reverse("AdminPostDetails", kwargs={'pk':self.post.id})
        self.FakePostDetails_url=reverse("AdminPostDetails", kwargs={'pk':-1})
        self.deletePost_url = reverse('AdminDeletePost',kwargs={'pk':self.post.id})
        self.edit_asso_url = reverse('searchAsso')
        self.admin_panel_url = reverse('adminPanel')
        self.admin_blockedUsers= reverse('blockedUsers')
        self.admin_changeState = reverse('changeActiveState',kwargs={'pk':self.UserObj.id})
        self.admin_deleteUser = reverse('deleteUser',kwargs={'pk':self.UserObj.id})
        self.reports_posts_url = reverse('reports_posts')
        self.reports_users_url = reverse('reports_users')
        self.reportsUserDetails_url = reverse('reportsUserDetails',kwargs={'pk':self.user1.id})
        self.reportsUserDetails_fakeUser_url = reverse('reportsUserDetails',kwargs={'pk':-1})
        self.deleteUserReports_url = reverse('deleteUserReports',kwargs={'pk':self.user1.id})
        self.deleteUserReports_fakeUser_url = reverse('deleteUserReports',kwargs={'pk':-1})
        self.blockUser_url = reverse('blockUser',kwargs={'pk':self.user1.id})
        self.blockUser_fakeUser_url = reverse('blockUser',kwargs={'pk':-1})
        self.adminMessagesUrl = reverse('adminMessages')
        self.adminEditMessageUrl = reverse('editAdminMessage',kwargs={'pk':self.adminMsg.id})
        self.adminDeleteMessageUrl = reverse('deleteAdminMessage',kwargs={'pk':self.adminMsg.id})
        self.adminDeleteMessage_FakeUrl = reverse('deleteAdminMessage',kwargs={'pk':self.adminMsg.id})


        
    
    def test_adminPanel_with_loogin(self):
        response = self.adminclient.get(self.admin_panel_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_index.html")
        
    def test_adminPanel_without_login(self):
        response = self.client.get(self.admin_panel_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
     
    def test_adminPosts_with_loogin(self):
        response = self.adminclient.get(self.AllPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(Post.objects.get(id=self.post.id),response.context['posts'].get(id=self.post.id))
        self.assertTemplateUsed("admin_posts.html")
    
    def test_adminPosts_without_login(self):
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
    
    def test_AdminDeletePost_with_login(self):
        response = self.adminclient.get(self.deletePost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_posts.html")
    
    def test_AdminEditAsso_without_login(self):
        response = self.client.get(self.edit_asso_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    def test_AdminEditAsso_with_login(self):
        response = self.adminclient.get(self.edit_asso_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_editAsso.html")


    def test_adminChangeState(self):
        response = self.client.get(self.admin_changeState)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.admin_changeState)  
        self.assertEqual(302,response.status_code)
    

    def test_adminDeleteUser(self):
        response = self.client.get(self.admin_deleteUser)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.admin_deleteUser)  
        self.assertEqual(302,response.status_code)
    

    def test_showBlockedUsers(self):
        response = self.client.get(self.admin_blockedUsers)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.admin_blockedUsers)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("blocked_users.html")
    
    def test_reports_posts(self):
        response = self.client.get(self.reports_posts_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.reports_posts_url,follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_reports_posts.html")
    
    def test_reports_users(self):
        response = self.client.get(self.reports_users_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.reports_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_reports_users.html")

    def test_reportsUserDetails(self):
        response = self.client.get(self.reportsUserDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        response = self.adminclient.get(self.reportsUserDetails_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_users_reports_details.html")

        response = self.adminclient.get(self.reportsUserDetails_fakeUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

    def test_deleteUserReports(self):
        response = self.client.get(self.deleteUserReports_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        response = self.adminclient.get(self.deleteUserReports_url,follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_reports_users.html")

        response = self.adminclient.get(self.deleteUserReports_fakeUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

    def test_blockUser(self):
        response = self.client.get(self.blockUser_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
        response = self.adminclient.get(self.blockUser_fakeUser_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        self.user1.is_active=False
        self.user1.save()
        response = self.adminclient.get(self.blockUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        self.user1.is_active=True
        self.user1.save()
        
        response = self.adminclient.get(self.blockUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("blockingForm.html")

        response = self.adminclient.post(self.blockUser_url, data ={'blocked_reason':'impostor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_index.html")

        response = self.adminclient.post(self.blockUser_url, data ={})
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("blockingForm.html")


    def test_deletePostReported_with_login(self):
        response = self.adminclient.get(self.deletePost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_posts.html")
        
    def test_deletePostReports_without_login(self):
        response = self.client.get(self.deletePost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html") 


    def test_adminMessages(self):
        response = self.client.get(self.adminMessagesUrl)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        response = self.adminclient.get(self.adminMessagesUrl)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_messages.html")

        response = self.adminclient.post(self.adminMessagesUrl, data ={'content':'impostor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_messages.html")
    
    def test_adminEditMessages(self):
        response = self.client.get(self.adminEditMessageUrl)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        response = self.adminclient.get(self.adminEditMessageUrl)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_messages.html")

        response = self.adminclient.post(self.adminEditMessageUrl, data ={'content':'impostor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_messages.html")

    def test_adminDeleteMessages(self):
        response = self.client.get(self.adminDeleteMessageUrl)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        response = self.adminclient.get(self.adminDeleteMessageUrl,follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_messages.html")

        response = self.adminclient.get(self.adminDeleteMessageUrl,follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_messages.html")
