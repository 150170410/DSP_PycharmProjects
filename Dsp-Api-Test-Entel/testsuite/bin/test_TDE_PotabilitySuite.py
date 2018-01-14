
from  testsuite.bin.entel_PageObject import *

class ValidateTDEPortability(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDEPortability, self).__init__(*args, **kwargs)


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
        opType = 'portability'

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

    def test_05id_document(self):
        """ test_05id_document: Test case for test view post using GET /posts/{id}.                                 """

        response=self.id_document(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_06populationcenter(self):
        """ test_06populationcenter: Test case for test view post using GET /posts/{id}.                                 """

        response=self.populationcenter(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_07dataporta(self):
        """ test_07dataporta: Test case for test view post using GET /posts/{id}.                                 """

        response = self.dataporta(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_08getplantariff(self):
        """ test_08getplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response=self.getplantariff(txn_id,opType)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_09selectplantariff(self):
        """ test_09selectplantariff: Test case for test view post using GET /posts/{id}.                                 """
        tarPlan = "PO_ADDON_BOLSA_100MB_1HR"

        response=self.selectplantariff(txn_id,tarPlan)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_10requestcontract(self):
        """ test_10requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id,opType)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_11contractacceptance(self):
        """ test_11contractacceptance: Test case for test view post using GET /posts/{id}.                                 """

        response = self.contractacceptance(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_12biometricws(self):
        """ test_12biometricws: Test case for test view post using GET /posts/{id}.                                 """

        response = self.biometricws(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_13requestorder(self):
        """ test_13requestorder: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestorder(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])