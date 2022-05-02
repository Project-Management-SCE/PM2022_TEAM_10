from django.test import TestCase
from posts.forms import createPostForm, editPostForm
from posts.models import Category


class TestForms(TestCase):
    def setUp(self):

        #create Category
        self.category=Category.objects.create(
            id='1',
            name='helpy'
        )
        
    def test_create_createPostForm_with_data(self):   
        form = createPostForm(data={'info':'i am writing a new post!','category':self.category.id})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

        form = createPostForm(data={'info':'i am writing a new post!'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_create_createPostForm(self):   
        form = createPostForm(data={'category':self.category.id})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        
        form = createPostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        
    def test_editPostForm_with_data(self):
        form = editPostForm(data={'info':'i am updating my post!','city':'New city', 'is_asking':True, 'category':self.category.id})
        self.assertTrue(form.is_valid())
        print(len(form.errors))
        self.assertEqual(len(form.errors),0)
        
