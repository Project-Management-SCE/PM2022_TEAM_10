from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import logout

class TestUrls(SimpleTestCase):
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)
        