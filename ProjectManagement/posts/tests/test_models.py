from django.test import TestCase,tag
from posts.models import Post,Category
from accounts.models import User,HelpoUser
import datetime

class TestModels(TestCase):
    def setUp(self):
        
        self.UserObj = User.objects.create(
            username = 'jimb2',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = True,
            is_helpo_user=True
        )
        
        #create helpo user
        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.UserObj,
            city = "BS"
        )
        
        #create Category
        self.category=Category.objects.create(
            name="my new category"
        )
        self.date = datetime.datetime.now()
        #create post object
        self.post=Post.objects.create(
            user=self.HelpoUserObj,
            city= "Tel-Aviv",
            info="i am writing a new post!",
            category=self.category,
            date=self.date
        )
        
    
    #test methods:
    @tag('UT')    
    def test_catagory(self):
        self.assertEqual(self.category.name, "my new category")
        self.assertEqual(self.category.__str__(),self.category.name)

    @tag('UT')    
    def test_post(self):
        self.assertFalse(self.post.is_asking)
        self.assertEqual(self.post.category.name,"my new category")
        self.assertEqual(self.post.date,self.date)
        self.assertTrue(self.post.user.user.is_helpo_user)
        self.assertEqual(self.post.info,"i am writing a new post!")
        self.assertEqual(self.post.city,"Tel-Aviv")
          
    
