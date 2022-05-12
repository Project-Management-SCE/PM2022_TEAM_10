# Create your tests here.
from django.test import TestCase
from reports.models import UserReport
from accounts.models import User

class TestModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username = 'jimb1',
            first_name = 'Jim1',
            last_name = 'Botten1',
            phone_number = '0524619773',
            is_active = True,
            is_helpo_user=True
        )
        
        self.user2 = User.objects.create(
            username = 'jimb2',
            first_name = 'Jim2',
            last_name = 'Botten2',
            phone_number = '0524619773',
            is_active = True,
            is_helpo_user=True
        )
                
        self.user_report = UserReport.objects.create(
            reporter = self.user1,
            reported = self.user2,
            reason = "becaus"
        )
        
    def test_UserReport(self): 
        self.assertEqual(self.user_report.reporter,self.user1)
        self.assertEqual(self.user_report.reported,self.user2)
        self.assertEqual(self.user_report.reason,"becaus")
