from django.test import SimpleTestCase,tag
from django.urls import reverse, resolve
from home.views import index

class TestUrls(SimpleTestCase):
    @tag('UT')
    def test_home_page_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
        