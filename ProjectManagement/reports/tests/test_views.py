from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client() # Create cliend
        self.UserObj = User.objects.create(
            id = '123',
            username = 'jimb',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = False
        )
        self.reportUser_url = reverse('reportUser', kwargs={'pk':self.UserObj.id})

    def reportUser(self):
        response = self.client.get(self.reportUser_url)  # Get response from the url
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.UserObj , response.context['reported_obj'])
        self.assertTemplateUsed("userReportPage.html")
        
        