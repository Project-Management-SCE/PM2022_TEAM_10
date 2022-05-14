from django.test import TestCase
from feedbacks.models import Feedback
from accounts.models import User
from feedbacks.forms import FeedbackFrom


class TestForms(TestCase):

    def test_FeedbackFrom(self):
        form = FeedbackFrom(data={'subject':"sub",'content':'con'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)