from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve
from reports.views import createReportPost

#inregration tests

class TestUrls(TestCase):
    def setUp(self):
        pass

    def test_all_associations_page_url_is_resolved(self):
        url = reverse('createReportPost',kwargs={'pk':1})
        self.assertEqual(resolve(url).func, createReportPost)
