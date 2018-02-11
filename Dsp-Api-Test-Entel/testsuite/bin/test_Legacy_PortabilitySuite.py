from  testsuite.bin.entel_PageObject import TestPosts,sdata

class ValidateLegacyPortability(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateLegacyPortability, self).__init__(*args, **kwargs)

        self.url = sdata.legacy_url
        self.opType = 'Portability'
        self.substype = '0'

    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """
        # response=self.loginuser()

    def test_02optionMenu(self):
        """ test_02optionMenu: Test case for test view post using GET /posts/{id}.                          """
        global txn_id
        response = self.optionmenu(self.opType)
        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]

    def test_03localizationnetw(self):
        """ test_03localizationnetw: Test case for test view post using GET /posts/{id}.                                 """
        self.localizationnetw(txn_id,self.legacy_localzn)

    def test_04portabilityquery(self):
        """ test_04portabilityquery: Test case for test view post using GET /posts/{id}.                                 """
        self.portabilityquery(txn_id,self.portedMsisdn,self.substype)

    def test_05sendportabilityresult(self):
        """ test_05sendportabilityresult: Test case for test view post using GET /posts/{id}.                                 """
        self.sendportabilityresult(txn_id,self.portedMsisdn,self.portStatus)

    def test_06validatemaximumLines(self):
        """ test_06validatemaximumLines: Test case for test view post using GET /posts/{id}.                                 """
        self.validatemaximumLines(txn_id)

    def test_07verifyresourceid(self):
        """ test_07verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """
        self.verifyresourceid(txn_id,self.ICCID_subscriber)

    def test_08populationcenter(self):
        """ test_08populationcenter: Test case for test view post using GET /posts/{id}.                                 """
        self.populationcenter(txn_id)

    def test_09getplantariff(self):
        """ test_09getplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.getplantariff(txn_id,self.opType)

    def test_10selectplantariff(self):
        """ test_10selectplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.selectplantariff(txn_id,self.tarPlan)

    def test_11requestcontract(self):
        """ test_11requestcontract: Test case for test view post using GET /posts/{id}.                                 """
        self.requestcontract(txn_id,self.opType)

    def test_12contractacceptance(self):
        """ test_12contractacceptance: Test case for test view post using GET /posts/{id}.                                 """
        self.contractacceptance(txn_id)

    def test_13biometricws(self):
        """ test_13biometricws: Test case for test view post using GET /posts/{id}.                                 """

        try:
            self.biometricws(txn_id)
        except AssertionError as e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.biometricws(txn_id)

    def test_14requestorder(self):
        """ test_14requestorder: Test case for test view post using GET /posts/{id}.                                 """
        self.requestorder(txn_id)
