from  testsuite.bin.entel_PageObject import TestPosts,sdata

class ValidateTDEPortability(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateTDEPortability, self).__init__(*args, **kwargs)

        self.url = sdata.tde_url
        self.opType = 'Portability'
        self.substype = 'POSTPAID'

    def test_01loginUser(self):
        """ test_01loginUser: Test case for test view post using GET /posts/{id}.                          """
        # response=self.loginuser()


    def test_02transactionquery(self):
        """ test_02transactionquery: Test case for test view post using GET /posts/{id}.                                 """
        self.transactionquery(self.portedMsisdn)

    def test_03optionMenu(self):
        """ test_03optionMenu: Test case for test view post using GET /posts/{id}.                          """
        global txn_id
        response = self.optionmenu(self.opType)
        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]

    def test_04localizationnetw(self):
        """ test_04localizationnetw: Test case for test view post using GET /posts/{id}.                                 """
        self.localizationnetw(txn_id,self.tde_localzn)

    def test_05portabilityquery(self):
        """ test_05portabilityquery: Test case for test view post using GET /posts/{id}.                                 """
        self.portabilityquery(txn_id,self.portedMsisdn,self.substype)


    def test_06portaqueryresult(self):
        """ test_06portaqueryresult: Test case for test view post using GET /posts/{id}.                                 """
        self.portaqueryresult(self.portedMsisdn, self.portStatus, txn_id)

    def test_07verifycustomerdata(self):
        """ test_07verifycustomerdata: Test case for test view post using GET /posts/{id}.                                 """
        self.verifycustomerdata(txn_id)

    def test_08verifyresourceid(self):
        """ test_08verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """
        self.verifyresourceid(txn_id, self.ICCID_subscriber)

    def test_09id_document(self):
        """ test_09id_document: Test case for test view post using GET /posts/{id}.                                 """
        try:
          self.id_document(txn_id)

        except AssertionError, e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.id_document(txn_id)

    def test_10populationcenter(self):
        """ test_10populationcenter: Test case for test view post using GET /posts/{id}.                                 """
        self.populationcenter(txn_id)

    def test_11getplantariff(self):
        """ test_11getplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.getplantariff(txn_id,self.opType)

    def test_12selectplantariff(self):
        """ test_13selectplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.selectplantariff(txn_id,self.tarPlan)

    def test_13requestcontract(self):
        """ test_13requestcontract: Test case for test view post using GET /posts/{id}.                                 """
        self.requestcontract(txn_id,self.opType)

    def test_14contractacceptance(self):
        """ test_14contractacceptance: Test case for test view post using GET /posts/{id}.                                 """
        self.contractacceptance(txn_id)

    def test_15biometricws(self):
        """ test_15biometricws: Test case for test view post using GET /posts/{id}.                                 """

        try:
            self.biometricws(txn_id)

        except AssertionError, e:
            self.lg(e.message)
            self.lg("Re-triggering since reponse code is not as expected")
            self.biometricws(txn_id)

    def test_16requestorder(self):
        """ test_16requestorder: Test case for test view post using GET /posts/{id}.                                 """
        self.requestorder(txn_id)


