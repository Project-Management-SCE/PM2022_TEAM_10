from django.test import TestCase,tag
from accounts.forms import AssociationManagerSignUpform, AssociationManagerUpdateform, UserUpdateform, HelpoUserUpdateform, HelpoUserSignUpform,UserBlockForm
from associations.models import Association
from accounts.models import User,associationManager

@tag('UT')
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

    def test_update_UserBlockForm_no_data(self):
        form = UserBlockForm(data={})
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
        self.assoObj = Association.objects.create(
            id = '123123',
            manager= None,
            name='asso1',
            category='category1',
            vol_num='10',
            city = 'Tel Aviv',
            street= 'Dizengoff',
            apartment='54',
            phone='0501231231',
            info='',
            email='asso1@associations.com'
        )
        form = AssociationManagerSignUpform(data={'username':'abc','first_name':'JIM', 'last_name':'Botten', 'email':'J@b.com'
                                    ,'phone_number':'0500500501','password1':'JjBotten1280','password2':'JjBotten1280', 'association_number':'123123'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)

    def test_update_UserBlockForm_with_data(self):
        form = UserBlockForm(data={'blocked_reason':'stam'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)