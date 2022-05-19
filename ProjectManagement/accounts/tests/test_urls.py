from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import logout, pickType, login,helpo_porfile

class TestUrls(SimpleTestCase):
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_pickType_url_is_resolved(self):
        url = reverse('pickType')
        self.assertEqual(resolve(url).func, pickType)

    def test_helpo_profile_url_is_resolved(self):
        url = reverse('helpo_porfile',kwargs={'pk':-1})
        self.assertEqual(resolve(url).func, helpo_porfile)


        