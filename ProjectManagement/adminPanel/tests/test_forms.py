from django.test import TestCase
from adminPanel.forms import Categoryform,AdminMessageForm
from posts.models import Category


class TestForms(TestCase):
    def setUp(self):
        self.categoryObj = Category.objects.create(
            name='Cat'
        )

    def test_create_createPostForm_with_data(self):   
        form = Categoryform(data={'name':'helpy'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

        form = Categoryform(data={'name':'Cat'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)


    def test_create_createPostForm(self):   
        form = Categoryform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        
    
    def test_AdminMessageForm(self):   
        #no data
        form = AdminMessageForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

        #with data
        form = AdminMessageForm(data={'content':'abcdefu'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)