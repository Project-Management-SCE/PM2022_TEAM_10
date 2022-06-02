from django.test import TestCase,tag
from reports.forms import reportUserForm, reportPostForm

class TestForms(TestCase):
    #Unit test for forms without data, to check the form is getting the all the needed erros
    @tag('UT')
    def test_create_reportUserForm(self):
        form = reportUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    @tag('UT')
    def test_create_reportUserForm_with_data(self):   
        form = reportUserForm(data={'reason':'i want to volunteer'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    @tag('UT')    
    def test_create_createReportPostForm_with_data(self):   
        form = reportPostForm(data={'info':'report'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    @tag('UT')
    def test_create_createReportPostForm(self):
        form = reportPostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

