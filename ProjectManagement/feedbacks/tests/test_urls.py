from django.test import SimpleTestCase
from django.urls import reverse, resolve
from feedbacks.views import sendFeedback

class TestUrls(SimpleTestCase):    
    def test_sendFeedback_url_is_resolved(self):
        url = reverse('sendFeedback')
        self.assertEqual(resolve(url).func, sendFeedback)
