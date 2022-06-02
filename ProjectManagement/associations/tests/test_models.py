# Create your tests here.
from django.test import TestCase,tag
from associations.models import Association,volunteeringRequest,Rank
from accounts.models import User, associationManager,HelpoUser

class TestModels(TestCase):
    def setUp(self):
        
        #create manager
        self.UserObj = User.objects.create(
            username = 'jimb2',
            first_name = 'Jim',
            last_name = 'Botten',
            phone_number = '0524619773',
            is_active = True,
            is_helpo_user=True
        )

        self.associationManagerObj = associationManager.objects.create(
            user = self.UserObj,
            association_number = '123123123'
        )
        
        #create helpo user
        self.HelpoUserObj = HelpoUser.objects.create(
            user = self.UserObj,
            city = "BS"
        )
        

        #create association object
        self.assoObj = Association.objects.create(
            id = '123123123',
            manager= self.associationManagerObj,
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
        
        #create volunteer Request
        self.vol_request = volunteeringRequest.objects.create(
            association=self.assoObj,
            user=self.HelpoUserObj,
            info="i want to volunteer!"
        )

        self.rankObj = Rank.objects.create(
            user = self.HelpoUserObj,
            association = self.assoObj,
            rank = 5
        )

    @tag('UT')
    def test_rank(self):
        self.assertEqual(self.rankObj.user.city,'BS')
        self.assertEqual(self.rankObj.rank,5)

    #test method:
    @tag('UT')
    def test_association(self):               
        self.assertEqual(self.assoObj.name,'asso1')
        self.assertEqual(self.assoObj.id,'123123123')
        self.assertEqual(self.assoObj.category,'category1')
        self.assertEqual(self.assoObj.vol_num,'10')
        self.assertEqual(self.assoObj.city,'Tel Aviv')
        self.assertEqual(self.assoObj.street,'Dizengoff')
        self.assertEqual(self.assoObj.apartment,'54')
        self.assertEqual(self.assoObj.phone,'0501231231')
        self.assertEqual(self.assoObj.info,'')
        self.assertEqual(self.assoObj.email,'asso1@associations.com')
        self.assertEqual(self.assoObj.manager.user.username,self.associationManagerObj.user.username)
        self.assertEqual(self.assoObj.__str__(),self.assoObj.name)
        
    @tag('UT')
    def test_volunteeringRequest(self):
        self.assertEqual(self.vol_request.info,"i want to volunteer!")
        self.assertEqual(self.vol_request.association.id,"123123123")
        self.assertTrue(self.vol_request.user.user.is_helpo_user)
        self.assertEqual(self.vol_request.user.user.username,"jimb2")

        
        
        
        
        

        
        
        
        
        