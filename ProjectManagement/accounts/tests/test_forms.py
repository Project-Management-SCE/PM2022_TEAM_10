from django.test import TestCase
from accounts.forms import AssociationManagerSignUpform, AssociationManagerUpdateform, UserUpdateform

class TestForms(TestCase):
    def test_create_AssociationManagerSignUpform_no_data(self):
        form = AssociationManagerSignUpform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),8)

    def test_update_AssociationManagerSignUpform_no_data(self):
        form = AssociationManagerUpdateform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_update_UserUpdateform_no_data(self):
        form = UserUpdateform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),5)