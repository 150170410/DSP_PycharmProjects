from  testsuite.bin.entel_PageObject import *

class ValidateTDEVenta(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDEVenta, self).__init__(*args, **kwargs)

        self.opType = 'venta'
        # self.ICCID_subscriber = config['main']['iccid_subscriber']
        # self.tarPlan = config['main']['tarplan']
        # self.legacy_localzn = config['main']['legacy_localzn']
        # self.tde_localzn = config['main']['tde_localzn']

        self.ICCID_subscriber = sdata.iccid_subscriber
        self.tarPlan = sdata.tarplan
        self.legacy_localzn = sdata.legacy_localzn
        self.tde_localzn = sdata.tde_localzn


    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """
        #self.loginuser()

    def test_02optionMenu(self):
        """ test_02optionMenu: Test case for test view post using GET /posts/{id}.                          """
        global txn_id
        response = self.optionmenu(self.opType)
        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]

    def test_03localizationnetw(self):
        """ test_03localizationnetw: Test case for test view post using GET /posts/{id}.                                 """
        self.localizationnetw(txn_id,self.tde_localzn)

    def test_04verifyresourceid(self):
        """ test_04verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """
        self.verifyresourceid(txn_id, self.ICCID_subscriber)

    def test_05id_document(self):
        """ test_05id_document: Test case for test view post using GET /posts/{id}.                                 """
        try:
            self.id_document(txn_id)
        except AssertionError as e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.id_document(txn_id)

    def test_06populationcenter(self):
        """ test_06populationcenter: Test case for test view post using GET /posts/{id}.                                 """
        self.populationcenter(txn_id)

    def test_07getplantariff(self):
        """ test_07getplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.getplantariff(txn_id,self.opType)

    def test_08selectplantariff(self):
        """ test_08selectplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.selectplantariff(txn_id,self.tarPlan)

    def test_09getavailablemsisdn(self):
        """ test_09getavailablemsisdn: Test case for test view post using GET /posts/{id}.                                 """
        self.getavailablemsisdn(txn_id)

    def test_10selectnumber(self):
        """ test_10selectnumber: Test case for test view post using GET /posts/{id}.                                 """
        self.selectnumber(txn_id)

    def test_11requestcontract(self):
        """ test_11requestcontract: Test case for test view post using GET /posts/{id}.                                 """
        self.requestcontract(txn_id,self.opType)

    def test_12contractacceptance(self):
        """ test_12contractacceptance: Test case for test view post using GET /posts/{id}.                                 """
        response = self.contractacceptance(txn_id)

    # def test_13biometricws(self):
    #     """ test_13biometricws: Test case for test view post using GET /posts/{id}.                                 """
    #     try:
    #         response = self.biometricws(txn_id)
    #     except AssertionError, e:
    #         self.lg(e.message)
    #         self.lg("Re-triggering since reponse code is not as expected")
    #         response = self.biometricws(txn_id)


    def test_13checknobiocounter(self):
        """ test_13checknobiocounter: Test case for test view post using GET /posts/{id}.                                 """
        self.checknobiocounter(txn_id)

    def test_14requestnobio(self):
        """ test_14requestnobio: Test case for test view post using GET /posts/{id}.                                 """
        self.requestnobio(txn_id)

    def test_15reportnobio(self):
        """ test_15reportnobio: Test case for test view post using GET /posts/{id}.                                 """
        self.reportnobio(txn_id)

    def test_16requestorder(self):
        """ test_14requestorder: Test case for test view post using GET /posts/{id}.                                 """
        self.requestorder(txn_id)

