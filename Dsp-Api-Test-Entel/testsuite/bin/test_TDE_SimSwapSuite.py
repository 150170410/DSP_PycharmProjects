
from  testsuite.bin.entel_PageObject import *

class ValidateTDESimSwap(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDESimSwap, self).__init__(*args, **kwargs)


    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """

        # response=self.loginuser()
        #
        # self.lg(response.text)
        # self.assertEqual(response.status_code, 200)
        # self.assertTrue(response.ok)
        # self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])

    def test_02optionMenu(self):
        """ test_02optionMenu: Test case for test view post using GET /posts/{id}.                          """

        global opType
        global txn_id
        global ICCID_subscriber

        ICCID_subscriber = '89560100000792428977'
        opType = 'Sim Swap'

        txn_id = 'ACT148'

        # response=self.optionmenu(opType)
        #
        # self.lg(response.text)
        # self.assertEqual(response.status_code, 200)
        # self.assertTrue(response.ok)
        # self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])

        #txn_id= response.text.split(',')[2].split(':')[1].split('"')[1]    #Returning txn_id

    def test_03localizationnetw(self):
        """ test_03localizationnetw: Test case for test view post using GET /posts/{id}.                                 """

        # response=self.localizationnetw(txn_id)
        #
        # self.lg(response.text)
        # self.assertEqual(response.status_code, 200)
        # self.assertTrue(response.ok)
        # self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        # self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_04verifyresourceid(self):
        """ test_04verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """

        response=self.verifyresourceid(txn_id,ICCID_subscriber)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])


    def test_05dataswap(self):
        """ test_05dataswap: Test case for test view post using GET /posts/{id}.                                 """

        response=self.dataswap(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_06swapreason(self):
        """ test_06swapreason: Test case for test view post using GET /posts/{id}.                                 """

        response=self.swapreason(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_07requestcontract(self):
        """ test_07requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id,opType)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_08contractacceptance(self):
        """ test_08contractacceptance: Test case for test view post using GET /posts/{id}.                                 """

        response = self.contractacceptance(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_09biometricws(self):
        """ test_09biometricws: Test case for test view post using GET /posts/{id}.                                 """

        response = self.biometricws(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_10requestorder(self):
        """ test_10requestorder: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestorder(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])