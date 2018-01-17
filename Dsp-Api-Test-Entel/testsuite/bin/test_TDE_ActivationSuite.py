from  testsuite.bin.entel_PageObject import *

class ValidateTDEVenta(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDEVenta, self).__init__(*args, **kwargs)


    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """

        # response=self.loginuser()
        # self.lg(response.text)

    def test_02optionMenu(self):
        """ test_02optionMenu: Test case for test view post using GET /posts/{id}.                          """

        global txn_id
        global opType
        global ICCID_subscriber
        global tarPlan
        global legacy_localzn
        global tde_localzn

        txn_id = 'ACT188'
        opType = 'venta'
        ICCID_subscriber = '89560100000792428909'
        tarPlan = 'PO_ADDON_BOLSA_100MB_1HR'
        legacy_localzn = '/YHT/BGF/3G'
        tde_localzn = '/23/56/Apple/SW2/4G'

        response = self.optionmenu(opType)
        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]
        self.lg(response.text)

    def test_03localizationnetw(self):
        """ test_03localizationnetw: Test case for test view post using GET /posts/{id}.                                 """

        response=self.localizationnetw(txn_id,tde_localzn)
        self.lg(response.text)

    def test_04verifyresourceid(self):
        """ test_04verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """

        response = self.verifyresourceid(txn_id, ICCID_subscriber)
        self.lg(response.text)

    def test_05id_document(self):
        """ test_05id_document: Test case for test view post using GET /posts/{id}.                                 """
        try:
            response = self.id_document(txn_id)
            self.lg(response.text)

        except AssertionError, e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            response = self.id_document(txn_id)
            self.lg(response.text)

    def test_06populationcenter(self):
        """ test_06populationcenter: Test case for test view post using GET /posts/{id}.                                 """

        response=self.populationcenter(txn_id)
        self.lg(response.text)

    def test_07getplantariff(self):
        """ test_07getplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response=self.getplantariff(txn_id,opType)
        self.lg(response.text)

    def test_08selectplantariff(self):
        """ test_08selectplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response=self.selectplantariff(txn_id,tarPlan)
        self.lg(response.text)

    def test_09getavailablemsisdn(self):
        """ test_09getavailablemsisdn: Test case for test view post using GET /posts/{id}.                                 """

        response=self.getavailablemsisdn(txn_id)
        self.lg(response.text)

    def test_10selectnumber(self):
        """ test_10selectnumber: Test case for test view post using GET /posts/{id}.                                 """

        response = self.selectnumber(txn_id)
        self.lg(response.text)

    def test_11requestcontract(self):
        """ test_11requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id,opType)
        self.lg(response.text)

    def test_12contractacceptance(self):
        """ test_12contractacceptance: Test case for test view post using GET /posts/{id}.                                 """

        response = self.contractacceptance(txn_id)
        self.lg(response.text)

    def test_13biometricws(self):
        """ test_13biometricws: Test case for test view post using GET /posts/{id}.                                 """
        try:
            response = self.biometricws(txn_id)
            self.lg(response.text)

        except AssertionError, e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            response = self.biometricws(txn_id)
            self.lg(response.text)

    def test_14requestorder(self):
        """ test_14requestorder: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestorder(txn_id)
        self.lg(response.text)

