from testsuite.bin.entel_PageObject import *


class ValidateLegacySimSwap(TestPosts):
    def __init__(self, *args, **kwargs):
        super(ValidateLegacySimSwap, self).__init__(*args, **kwargs)

        self.opType = 'Sim Swap'
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

        response = self.localizationnetw(txn_id, self.legacy_localzn)
        self.lg(response.text)

    def test_04verifyresourceid(self):
        """ test_04verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """

        response = self.verifyresourceid(txn_id, self.ICCID_subscriber)
        self.lg(response.text)

    def test_05dataswap(self):
        """ test_05dataswap: Test case for test view post using GET /posts/{id}.                                 """

        response = self.dataswap(txn_id)
        self.lg(response.text)

    def test_07requestcontract(self):
        """ test_07requestcontract: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestcontract(txn_id, self.opType)
        self.lg(response.text)

    def test_08contractacceptance(self):
        """ test_08contractacceptance: Test case for test view post using GET /posts/{id}.                                 """

        response = self.contractacceptance(txn_id)
        self.lg(response.text)

    def test_09biometricws(self):
        """ test_09biometricws: Test case for test view post using GET /posts/{id}.                                 """

        try:
            response = self.biometricws(txn_id)
            self.lg(response.text)

        except AssertionError, e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            response = self.biometricws(txn_id)
            self.lg(response.text)

    def test_10requestorder(self):
        """ test_10requestorder: Test case for test view post using GET /posts/{id}.                                 """

        response = self.requestorder(txn_id)
        self.lg(response.text)
