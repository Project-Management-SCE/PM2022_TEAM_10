from django.test import SimpleTestCase,TestCase,tag
from accounts.models import User
from django.urls import reverse, resolve
from reports.views import reportUser, createReportPost

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

    @tag('UT')
    def test_reportUser_url(self):
        url = reverse('reportUser', kwargs={'pk':self.UserObj.id})
        self.assertEqual(resolve(url).func, reportUser)

    @tag('UT')    
    def test_all_associations_page_url_is_resolved(self):
        url = reverse('createReportPost',kwargs={'pk':1})
        self.assertEqual(resolve(url).func, createReportPost)

