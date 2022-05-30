# Create your tests here.
from django.test import TestCase
from adminPanel.models import AdminMessage

class TestModels(TestCase):
    def setUp(self):
        self.message = AdminMessage.objects.create(
            content = 'cont'
        )
        
    def test_QuestionAnswer(self):
        self.assertEqual(self.message.content,'cont')
        self.assertEqual(str(self.message),f'Message no. {self.message.id}')
        
        