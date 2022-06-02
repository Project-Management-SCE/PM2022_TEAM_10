from django.test import SimpleTestCase,TestCase,tag
from django.urls import reverse, resolve
from posts.views import showAllPosts

#inregration tests

class TestUrls(TestCase):
    def setUp(self):
        pass
    
    @tag('UT')    #maybe change it to IT
    def test_all_associations_page_url_is_resolved(self):
        url = reverse('showAllPosts')
        self.assertEqual(resolve(url).func, showAllPosts)
