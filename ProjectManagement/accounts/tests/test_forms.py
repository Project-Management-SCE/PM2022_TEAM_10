from django.test import TestCase
from accounts.forms import AssociationManagerSignUpform

class TestForms(TestCase):
    def test_create_AssociationManagerSignUpform_no_data(self):
        form = AssociationManagerSignUpform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),8)
