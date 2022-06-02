from django.test import SimpleTestCase,tag
from django.urls import reverse, resolve
from feedbacks.views import sendFeedback

class TestUrls(SimpleTestCase):    
    @tag('UT')
    def test_sendFeedback_url_is_resolved(self):
        url = reverse('sendFeedback')
        self.assertEqual(resolve(url).func, sendFeedback)
