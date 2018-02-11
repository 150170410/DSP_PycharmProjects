from  testsuite.bin.entel_PageObject import TestPosts,sdata

class ValidateTDESimSwap(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDESimSwap, self).__init__(*args, **kwargs)

        self.url = sdata.tde_url
        self.opType = 'Sim Swap'

    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """
        # self.loginuser()

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

    def test_05dataswap(self):
        """ test_05dataswap: Test case for test view post using GET /posts/{id}.                                 """
        try:
            self.dataswap(txn_id)
        except AssertionError as e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.dataswap(txn_id)

    def test_06swapreason(self):
        """ test_06swapreason: Test case for test view post using GET /posts/{id}.                                 """
        try:
            self.swapreason(txn_id)
        except AssertionError as e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.swapreason(txn_id)

    def test_07requestcontract(self):
        """ test_07requestcontract: Test case for test view post using GET /posts/{id}.                                 """
        self.requestcontract(txn_id,self.opType)

    def test_08contractacceptance(self):
        """ test_08contractacceptance: Test case for test view post using GET /posts/{id}.                                 """
        self.contractacceptance(txn_id)

    def test_09biometricws(self):
        """ test_09biometricws: Test case for test view post using GET /posts/{id}.                                 """
        try:
            self.biometricws(txn_id)
        except AssertionError as e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.biometricws(txn_id)

    def test_10requestorder(self):
        """ test_10requestorder: Test case for test view post using GET /posts/{id}.                                 """
        self.requestorder(txn_id)
