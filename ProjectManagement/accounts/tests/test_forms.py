from django.test import TestCase
from accounts.forms import AssociationManagerSignUpform, AssociationManagerUpdateform, UserUpdateform, HelpoUserUpdateform, HelpoUserSignUpform

class TestForms(TestCase):
    #Unit test for forms without data, to check the form is getting the all the needed erros
    def test_create_AssociationManagerSignUpform_no_data(self):
        form = AssociationManagerSignUpform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),8)

    def test_create_HelpoUserSignUpform_no_data(self):
        form = HelpoUserSignUpform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),8)

    def test_update_UserUpdateform_no_data(self):
        form = UserUpdateform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),5)

    def test_update_AssociationManagerUpdateForm_no_data(self):
        form = AssociationManagerUpdateform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_update_HelpoUserUpdateform_no_data(self):
        form = HelpoUserUpdateform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    #Unit test for forms
    def test_update_HelpoUserUpdateform_with_data(self):
        form = HelpoUserUpdateform(data={'city':'ofakim'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_update_AssociationManagerUpdateForm_with_data(self):
        form = AssociationManagerUpdateform(data={'association_number':'12345'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_update_UserUpdateform_with_data(self):
        form = UserUpdateform(data={'username':'abc','first_name':'JIM', 'last_name':'Botten', 'email':'J@b.com','phone_number':'0500500501'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_create_HelpoUserSignUpform_with_data(self):
        form = HelpoUserSignUpform(data={'username':'abc','first_name':'JIM', 'last_name':'Botten', 'email':'J@b.com'
                                    ,'phone_number':'0500500501','password1':'JjBotten1280','password2':'JjBotten1280', 'city':'lalaland'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_create_AssociationManagerSignUpform_with_data(self):
        form = AssociationManagerSignUpform(data={'username':'abc','first_name':'JIM', 'last_name':'Botten', 'email':'J@b.com'
                                    ,'phone_number':'0500500501','password1':'JjBotten1280','password2':'JjBotten1280', 'association_number':'12345'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)