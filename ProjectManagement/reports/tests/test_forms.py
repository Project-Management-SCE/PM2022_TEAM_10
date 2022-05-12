from django.test import TestCase
from reports.forms import reportPostForm

class TestForms(TestCase):
    def setUp(self):
        pass
            
    def test_create_createReportPostForm_with_data(self):   
        form = reportPostForm(data={'info':'report'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)


    def test_create_createReportPostForm(self):
        form = reportPostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
        

