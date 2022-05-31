from django.test import TestCase
from accounts.models import User, associationManager, HelpoUser

class TestModels(TestCase):

    def setUp(self):
        #   Create objects
        self.UserObj = User.objects.create(
            username = 'jimb',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = False
        )

        self.associationManagerObj = associationManager.objects.create(
            user = self.UserObj,
            association_number = '123456'
        )
        
        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.UserObj,
            city = "BS"
        )

    def test_User(self):
        # Test basic user
        self.assertEqual(self.UserObj.username, 'jimb')
        self.assertEqual(self.UserObj.first_name, 'Jim')
        self.assertEqual(self.UserObj.last_name, 'Botten')
        self.assertEqual(self.UserObj.phone_number, '0524619773')
        self.assertFalse(self.UserObj.is_active)
        self.assertEqual(self.UserObj.__str__(), 'jimb')        
        

    def test_association_manager(self):
        self.assertFalse(self.associationManagerObj.user.is_association_manager)
        self.assertEqual(self.UserObj.username, 'jimb')
        self.assertEqual(self.associationManagerObj.user.first_name, 'Jim')
        self.assertEqual(self.associationManagerObj.user.last_name, 'Botten')
        self.assertEqual(self.associationManagerObj.user.phone_number, '0524619773')
        self.assertEqual(self.associationManagerObj.association_number, '123456')
        #admin page approval
        self.assertFalse(self.associationManagerObj.user.is_active)
        self.assertEqual(self.associationManagerObj.__str__(), 'jimb : Wait-for-activate')
        
        self.associationManagerObj.user.is_active = True
        self.assertTrue(self.associationManagerObj.user.is_active)
        self.assertEqual(self.associationManagerObj.__str__(), 'jimb : active')
        self.assertTrue(self.associationManagerObj.user_is_active())
        
        
    def test_helpo_user(self):
        self.assertFalse(self.HelpoUserObj.user.is_association_manager)
        self.assertEqual(self.HelpoUserObj.user.username, 'jimb')
        self.assertEqual(self.HelpoUserObj.user.first_name, 'Jim')
        self.assertEqual(self.HelpoUserObj.user.last_name, 'Botten')
        self.assertEqual(self.HelpoUserObj.user.phone_number, '0524619773')
        self.assertEqual(self.HelpoUserObj.city, 'BS')
        #admin page approval
        self.assertFalse(self.HelpoUserObj.user.is_active)
        self.assertEqual(self.HelpoUserObj.__str__(), 'jimb')
        
        self.HelpoUserObj.user.is_active = True
        self.assertTrue(self.HelpoUserObj.user.is_active)
        
        
        
