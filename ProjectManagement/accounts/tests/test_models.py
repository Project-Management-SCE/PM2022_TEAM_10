from django.test import TestCase
from accounts.models import User, associationManager

class TestModels(TestCase):

    def setUp(self):
        #   Create objects
        self.UserObj = User.objects.create(
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773'
        )

        self.associationManagerObj = associationManager.objects.create(
            user = self.UserObj,
            association_number = '123456'
        )

    def test_User(self):
        # self.assertTrue(self.UserObj.is_association_manager)
        self.assertEqual(self.UserObj.first_name, 'Jim')
        self.assertEqual(self.UserObj.last_name, 'Botten')
        self.assertEqual(self.UserObj.phone_number, '0524619773')

    def test_association_manager(self):
        self.assertFalse(self.associationManagerObj.user.is_association_manager)
        self.assertEqual(self.associationManagerObj.user.first_name, 'Jim')
        self.assertEqual(self.associationManagerObj.user.last_name, 'Botten')
        self.assertEqual(self.associationManagerObj.user.phone_number, '0524619773')
        self.assertEqual(self.associationManagerObj.association_number, '123456')