
import imp
from operator import truediv
from urllib import response
from django.test import TestCase, Client,tag
from django.urls import reverse
from posts.models import Post
from accounts.models import User,HelpoUser,associationManager
from adminPanel.models import AdminMessage
from posts.models import Category
from django.test.client import RequestFactory
from associations.models import Association
import datetime 
from feedbacks.models import Feedback
from home.models import QuestionAnswer

class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.category = Category.objects.create(
            name='categ'
        )

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
        self.user2 = User.objects.create_user(username='username2', password='password2')

        self.associationManagerObj = associationManager.objects.create(
            user = self.user2,
            association_number = '123456'
        )
        #create helpo user
        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.user1,
            city = "BS"
        )
        
        self.user1.is_superuser=True
        self.user1.is_staff=True
        self.user1.save()
        
        #create post object
        self.post=Post.objects.create(
            user=self.HelpoUserObj,
            city= "Tel-Aviv",
            info="i am writing a new post!",
            # category=self.category,
            date=datetime.date.today()
        )
        self.post2=Post.objects.create(
            user=self.HelpoUserObj,
            city= "Tel-Aviv",
            info="i am writing a new post!",
            # category=self.category,
            date=datetime.date.today()
        )
        self.adminMsg = AdminMessage.objects.create(
            content = "ABCDEFG"
        )
        
        #create feedback object
        self.feedback = Feedback.objects.create(
            user=self.user1,
            subject="subject of feedback",
            content= "content of feedback"
        )

        self.q_a = QuestionAnswer.objects.create(
            Question = 'q',
            Answer = 'a'
        )
        
        self.adminclient = Client() # Create cliend
        self.adminclient.login(username="username",password="password")

        self.client = Client()
        
        self.AllPosts_url=reverse("posts")
        self.PostDetails_url=reverse("AdminPostDetails", kwargs={'pk':self.post.id})
        self.FakePostDetails_url=reverse("AdminPostDetails", kwargs={'pk':-1})
        self.deletePost_url = reverse('AdminDeletePost',kwargs={'pk':self.post.id})
        self.Dont_deletePost_url = reverse('AdminDeletePost',kwargs={'pk':"99"})
        self.deletePostReported_url = reverse('deletePostReported',args=(f'{self.post2.id}',))
        
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
        self.deleteFeedback_url = reverse('deleteFeedback',kwargs={'pk':self.feedback.id})
        self.deleteFeedback_fake_url = reverse('deleteFeedback',kwargs={'pk':-1})
        self.AllFeedbacks_url = reverse('AllFeedbacks')
        self.showActivityTracking_url = reverse('showActivityTracking')
        self.adminMessagesUrl = reverse('adminMessages')
        self.adminEditMessageUrl = reverse('editAdminMessage',kwargs={'pk':self.adminMsg.id})
        self.adminDeleteMessageUrl = reverse('deleteAdminMessage',kwargs={'pk':self.adminMsg.id})
        self.adminDeleteMessage_FakeUrl = reverse('deleteAdminMessage',kwargs={'pk':self.adminMsg.id})

        self.show_questions_url = reverse('show_questions')
        self.add_question_url = reverse('add_question')
        self.delete_question_url = reverse('delete_question',kwargs={'pk':self.q_a.id})
        self.adminPanel_url = reverse('adminPanel')
        self.show_questions_url = reverse('show_questions')
        self.edit_question_url = reverse('edit_question',kwargs={'pk':self.q_a.id})

        self.helpo_users_url = reverse('helpo_users')
        self.AdminUpdateHelpoUser_url = reverse('AdminUpdateHelpoUser',kwargs={'pk':self.HelpoUserObj.user.id})
        self.manager_users_url = reverse('manager_users')

        self.AdminUpdateManagerUser_url = reverse('AdminUpdateManagerUser',kwargs={'pk':self.associationManagerObj.user.id})

        self.waiting_manager_users_url = reverse('waiting_manager_users')
        self.ApproveManager_url = reverse('ApproveManager',kwargs={'pk':self.associationManagerObj.user.id})
        self.DontApproveManager_url = reverse('ApproveManager',kwargs={'pk':'99'})

        self.delete_approve_request_url = reverse('delete_approve_request',kwargs={'pk':self.associationManagerObj.user.id})
        self.Dont_delete_approve_request_url = reverse('delete_approve_request',kwargs={'pk':'99'})

        self.categories_url = reverse('categories')
        self.editCategory_url = reverse('editCategory',args=[f'{self.category.id}'])
        self.deleteCategory_url = reverse('deleteCategory',args=[f'{self.category.id}'])
        self.deleteCategoryNotExists_url = reverse('deleteCategory',args=['999'])

    @tag('UT') 
    def test_deleteCategory(self):
        response = self.client.get(self.deleteCategory_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.deleteCategory_url)
        self.assertTemplateUsed("categoryFormPage")

        response = self.adminclient.get(self.deleteCategoryNotExists_url)
        self.assertTemplateUsed("categoryFormPage")        
        
    @tag('IT')     
    def test_editCategory(self):
        response = self.client.get(self.editCategory_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.editCategory_url)
        self.assertTemplateUsed("categoryFormPage")
        
        response = self.adminclient.post(self.editCategory_url ,data ={'name':'categor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("categoryFormPage")

    @tag('IT') 
    def test_categories(self):
        response = self.client.get(self.categories_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.categories_url)
        self.assertTemplateUsed("categoryFormPage")

        response = self.adminclient.post(self.categories_url ,data ={'name':'categor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("categoryFormPage")

    @tag('UT') 
    def test_delete_approve_request(self):
        response = self.client.get(self.delete_approve_request_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.delete_approve_request_url)
        self.assertTemplateUsed("waiting_manager_users")     
        response = self.adminclient.get(self.Dont_delete_approve_request_url)
        self.assertTemplateUsed("waiting_manager_users")          

    @tag('UT') 
    def test_ApproveManager(self):
        response = self.client.get(self.ApproveManager_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.ApproveManager_url)
        self.assertTemplateUsed("waiting_manager_users")     
        response = self.adminclient.get(self.DontApproveManager_url)
        self.assertTemplateUsed("waiting_manager_users")       

    @tag('UT') 
    def test_waiting_manager_users(self):
        response = self.client.get(self.waiting_manager_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.waiting_manager_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("waiting_manager_users.html")     

    @tag('UT') 
    def test_AdminUpdateManagerUser(self):
        response = self.client.get(self.AdminUpdateManagerUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.AdminUpdateManagerUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("registration/updateAssociationManager.html")         

    @tag('UT') 
    def test_manager_users(self):
        response = self.client.get(self.manager_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.manager_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_manager_users.html")        

    @tag('UT') 
    def test_AdminUpdateHelpoUser(self):
        response = self.client.get(self.AdminUpdateHelpoUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.AdminUpdateHelpoUser_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("registration/updateHelpoUser.html")

    @tag('UT') 
    def test_helpo_users(self):
        response = self.client.get(self.helpo_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.helpo_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_helpo_users.html")

    @tag('UT') 
    def test_adminPanel(self):
        response = self.client.get(self.adminPanel_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.adminPanel_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_index.html")
    
    @tag('UT') 
    def test_show_questions(self):
        response = self.client.get(self.show_questions_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.show_questions_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_q_a.html")
    
    @tag('UT') 
    def test_delete_question(self):
        response = self.client.get(self.delete_question_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        response = self.adminclient.get(self.delete_question_url)
        self.assertTemplateUsed("/adminPanel/show_questions")

    @tag('UT') 
    def test_add_question_with_login(self):
        response = self.adminclient.get(self.add_question_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_add_q_a.html")        

    @tag('UT') 
    def test_add_question_without_login(self):
        response = self.client.get(self.add_question_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

    @tag('UT') 
    def test_show_questions_with_login(self):
        response = self.adminclient.get(self.show_questions_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_q_a.html")        

    @tag('UT') 
    def test_show_questions_without_login(self):
        response = self.client.get(self.show_questions_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")      
    
    @tag('UT') 
    def test_edit_question(self):
        response = self.client.get(self.edit_question_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")  
        response = self.adminclient.get(self.edit_question_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_add_q_a.html")  

    @tag('UT') 
    def test_adminPanel_with_loogin(self):
        response = self.adminclient.get(self.admin_panel_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_index.html")
    
    @tag('UT')     
    def test_adminPanel_without_login(self):
        response = self.client.get(self.admin_panel_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

    @tag('IT') 
    def test_adminPosts_with_loogin(self):
        response = self.adminclient.get(self.AllPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(Post.objects.get(id=self.post.id),response.context['posts'].get(id=self.post.id))
        self.assertTemplateUsed("admin_posts.html")
    
    @tag('UT') 
    def test_adminPosts_without_login(self):
        response = self.client.get(self.AllPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    @tag('UT') 
    def test_AdminPostDetails_without_login(self):
        response = self.client.get(self.PostDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    @tag('UT') 
    def test_AdminPostDetails_with_login_and_fake_post(self):
        response = self.adminclient.get(self.FakePostDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    @tag('UT') 
    def test_AdminPostDetails_with_login(self):
        response = self.adminclient.get(self.PostDetails_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("adminPostDetails.html")
        self.assertEqual(response.context['obj'].id,self.post.id)
    
    @tag('IT') 
    def test_AdminDeletePost_without_login(self):
        response = self.client.get(self.deletePost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")

        response = self.adminclient.get(self.deletePost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_posts.html")
        
        response = self.adminclient.get(self.deletePostReported_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_posts.html")
        
        response = self.adminclient.get(self.Dont_deletePost_url,follow=True)  
        self.assertTemplateUsed("admin_error.html")

    
    @tag('UT') 
    def test_AdminEditAsso_without_login(self):
        response = self.client.get(self.edit_asso_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
    
    @tag('UT')     
    def test_AdminEditAsso_with_login(self):
        response = self.adminclient.get(self.edit_asso_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_editAsso.html")

    
    @tag('UT') 
    def test_adminChangeState(self):
        response = self.client.get(self.admin_changeState)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.admin_changeState)  
        self.assertEqual(302,response.status_code)
    
    
    @tag('UT') 
    def test_adminDeleteUser(self):
        response = self.client.get(self.admin_deleteUser)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.admin_deleteUser)  
        self.assertEqual(302,response.status_code)
    
    
    @tag('UT') 
    def test_showBlockedUsers(self):
        response = self.client.get(self.admin_blockedUsers)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.admin_blockedUsers)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("blocked_users.html")
    
    @tag('UT') 
    def test_reports_posts(self):
        response = self.client.get(self.reports_posts_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.reports_posts_url,follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_reports_posts.html")
    
    @tag('UT') 
    def test_reports_users(self):
        response = self.client.get(self.reports_users_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.reports_users_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_reports_users.html")
    
    @tag('IT') 
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

    @tag('IT') 
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

    @tag('IT')  
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


    @tag('UT') 
    def test_deletePostReported_with_login(self):
        response = self.adminclient.get(self.deletePost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_posts.html")
   
    @tag('UT')      
    def test_deletePostReports_without_login(self):
        response = self.client.get(self.deletePost_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html") 

    @tag('UT') 
    def test_show_activity_tracking_without_login(self):
        response = self.client.get(self.showActivityTracking_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html") 

    @tag('IT') 
    def test_show_activity_tracking_with_login(self):
        response = self.adminclient.get(self.showActivityTracking_url)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.context['num_of_posts'],Post.objects.all().count())
        self.assertEqual(response.context['num_of_associations'],Association.objects.all().count())
        self.assertEqual(response.context['num_of_users'],User.objects.filter(is_superuser__in=[False]).count())

        self.assertTemplateUsed("activity_tracking.html") 

    @tag('IT') 
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
    
    @tag('IT') 
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

    @tag('IT') 
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
