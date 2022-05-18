from django.test import SimpleTestCase
from django.urls import reverse, resolve
from adminPanel.views import searchAsso,AllFeedbacks

class TestUrls(SimpleTestCase):
    def test_searchAsso_url_is_resolved(self):
        url = reverse('searchAsso')
        self.assertEqual(resolve(url).func, searchAsso)
        
        
    def test_AllFeedbacks_url_is_resolved(self):
        url = reverse('AllFeedbacks')
        self.assertEqual(resolve(url).func, AllFeedbacks)


        