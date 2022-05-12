from django.test import SimpleTestCase,TestCase
from accounts.models import User
from django.urls import reverse, resolve
from reports.views import reportUser

class TestUrls(TestCase):
    
    def setUp(self):
        self.UserObj = User.objects.create(
            id = '123',
            username = 'jimb',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = False
        )

    def test_reportUser_url(self):
        url = reverse('reportUser', kwargs={'pk':self.UserObj.id})
        self.assertEqual(resolve(url).func, reportUser)