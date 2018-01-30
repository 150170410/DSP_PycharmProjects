
from  testsuite.bin.entel_PageObject import *

class ValidateLegacyPortability(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateLegacyPortability, self).__init__(*args, **kwargs)

        self.opType = 'Portability'
        self.ICCID_subscriber = config['main']['iccid_subscriber']
        self.portedMsisdn = config['main']['portedmsisdn']
        self.portStatus = config['main']['portstatus']
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

        response=self.localizationnetw(txn_id,self.legacy_localzn)
        self.lg(response.text)

    def test_04portabilityquery(self):
        """ test_04portabilityquery: Test case for test view post using GET /posts/{id}.                                 """

        response=self.portabilityquery(txn_id,self.portedMsisdn)
        self.lg(response.text)

    def test_05sendportabilityresult(self):
        """ test_05sendportabilityresult: Test case for test view post using GET /posts/{id}.                                 """

        response=self.sendportabilityresult(txn_id,self.portedMsisdn,self.portStatus)
        self.lg(response.text)


    def test_06validatemaximumLines(self):
        """ test_06validatemaximumLines: Test case for test view post using GET /posts/{id}.                                 """

        response=self.validatemaximumLines(txn_id)
        self.lg(response.text)

    def test_07verifyresourceid(self):
        """ test_07verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """

        response=self.verifyresourceid(txn_id,self.ICCID_subscriber)
        self.lg(response.text)

    def test_08populationcenter(self):
        """ test_08populationcenter: Test case for test view post using GET /posts/{id}.                                 """

        response=self.populationcenter(txn_id)
        self.lg(response.text)


    def test_09getplantariff(self):
        """ test_09getplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response=self.getplantariff(txn_id,self.opType)
        self.lg(response.text)

    def test_10selectplantariff(self):
        """ test_10selectplantariff: Test case for test view post using GET /posts/{id}.                                 """

        response=self.selectplantariff(txn_id,self.tarPlan)
        self.lg(response.text)

    def test_11requestcontract(self):
        """ test_11requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id,self.opType)
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
