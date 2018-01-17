
from  testsuite.bin.entel_PageObject import *

class ValidateTDELegacyPortability(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDELegacyPortability, self).__init__(*args, **kwargs)


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
        opType = 'venta'

        txn_id = 'ACT148'   #To be removed once started testing

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

    def test_04portabilityquery(self):
        """ test_04portabilityquery: Test case for test view post using GET /posts/{id}.                                 """

        response=self.portabilityquery(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_05sendportabilityresult(self):
        """ test_05sendportabilityresult: Test case for test view post using GET /posts/{id}.                                 """

        response=self.sendportabilityresult(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_06validatemaximumLines(self):
        """ test_06validatemaximumLines: Test case for test view post using GET /posts/{id}.                                 """

        response=self.validatemaximumLines(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_07verifyresourceid(self):
        """ test_07verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """

        response=self.verifyresourceid(txn_id,ICCID_subscriber)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_08populationcenter(self):
        """ test_08populationcenter: Test case for test view post using GET /posts/{id}.                                 """

        response=self.populationcenter(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_09getplantariff(self):
        """ test_09getplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response=self.getplantariff(txn_id,opType)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_10selectplantariff(self):
        """ test_10selectplantariff: Test case for test view post using GET /posts/{id}.                                 """
        tarPlan = "PO_ADDON_BOLSA_100MB_1HR"

        response=self.selectplantariff(txn_id,tarPlan)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_11requestcontract(self):
        """ test_11requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id,opType)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_12contractacceptance(self):
        """ test_12contractacceptance: Test case for test view post using GET /posts/{id}.                                 """

        response = self.contractacceptance(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_13biometricws(self):
        """ test_13biometricws: Test case for test view post using GET /posts/{id}.                                 """

        response = self.biometricws(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_14requestorder(self):
        """ test_14requestorder: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestorder(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])