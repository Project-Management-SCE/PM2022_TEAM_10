from django.test import TestCase
from posts.forms import createPostForm


class TestForms(TestCase):
        
    def test_create_createPostForm_with_data(self):   
        form = createPostForm(data={'info':'i am writing a new post!','category':'0'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_create_createPostForm(self):   
        form = createPostForm(data={'info':'i am writing a new post!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        
        form = createPostForm(data={'category':'0'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        
        
        form = createPostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)
        