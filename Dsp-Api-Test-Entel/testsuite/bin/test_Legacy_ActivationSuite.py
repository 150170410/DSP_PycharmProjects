
from  testsuite.bin.entel_PageObject import *

class ValidateLegacyVenta(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateLegacyVenta, self).__init__(*args, **kwargs)

        self.opType = 'venta'
        self.ICCID_subscriber = config['main']['iccid_subscriber']
        self.tarPlan = config['main']['tarplan']
        self.legacy_localzn = config['main']['legacy_localzn']
        self.tde_localzn = config['main']['tde_localzn']

    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """

        # response=self.loginuser()
        # self.lg(response.text)

    def test_02optionMenu(self):
        """ test_02optionMenu: Test case for test view post using GET /posts/{id}.                          """

        global txn_id
        response = self.optionmenu(self.opType)
        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]
        self.lg(response.text)

    def test_03localizationnetw(self):
        """ test_03localizationnetw: Test case for test view post using GET /posts/{id}.                                 """

        response = self.localizationnetw(txn_id,self.legacy_localzn)
        self.lg(response.text)

    def test_04verifyresourceid(self):
        """ test_04verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """

        response = self.verifyresourceid(txn_id, self.ICCID_subscriber)
        self.lg(response.text)

    def test_05id_document(self):
        """ test_05id_document: Test case for test view post using GET /posts/{id}.                                 """

        response = self.id_document(txn_id)
        self.lg(response.text)

    def test_06populationcenter(self):
        """ test_06populationcenter: Test case for test view post using GET /posts/{id}.                                 """

        response = self.populationcenter(txn_id)
        self.lg(response.text)

    def test_07getplantariff(self):
        """ test_07getplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response = self.getplantariff(txn_id, self.opType)
        self.lg(response.text)

    def test_08selectplantariff(self):
        """ test_08selectplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response = self.selectplantariff(txn_id, self.tarPlan)
        self.lg(response.text)

    def test_09requestcontract(self):
        """ test_09requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id, self.opType)
        self.lg(response.text)

    def test_10contractacceptance(self):
        """ test_10contractacceptance: Test case for test view post using GET /posts/{id}.                                 """

        response = self.contractacceptance(txn_id)
        self.lg(response.text)

    def test_11biometricws(self):
        """ test_11biometricws: Test case for test view post using GET /posts/{id}.                                 """
        try:
            response = self.biometricws(txn_id)
            self.lg(response.text)

        except AssertionError, e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            response = self.biometricws(txn_id)
            self.lg(response.text)

    def test_12requestorder(self):
        """ test_12requestorder: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestorder(txn_id)
        self.lg(response.text)


