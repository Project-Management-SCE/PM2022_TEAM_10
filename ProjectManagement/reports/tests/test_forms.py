from django.test import TestCase
from reports.forms import reportUserForm


class TestForms(TestCase):
    #Unit test for forms without data, to check the form is getting the all the needed erros
    def test_create_reportUserForm(self):
        form = reportUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_create_reportUserForm_with_data(self):   
        form = reportUserForm(data={'reason':'i want to volunteer'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)
