from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index

class TestUrls(SimpleTestCase):
    
    def test_home_page_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
        