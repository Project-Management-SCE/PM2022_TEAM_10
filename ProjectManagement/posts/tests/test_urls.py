from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve
from posts.views import showAllPosts



class TestUrls(TestCase):
    def setUp(self):
        pass

    def test_all_associations_page_url_is_resolved(self):
        url = reverse('showAllPosts')
        self.assertEqual(resolve(url).func, showAllPosts)
