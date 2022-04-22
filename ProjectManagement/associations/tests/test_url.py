from django.test import SimpleTestCase
from django.urls import reverse, resolve
from associations.views import All

class TestUrls(SimpleTestCase):
    
    def test_all_associations_page_url_is_resolved(self):
        url = reverse('All')
        self.assertEqual(resolve(url).func, All)
    
#add test for the dynamic url