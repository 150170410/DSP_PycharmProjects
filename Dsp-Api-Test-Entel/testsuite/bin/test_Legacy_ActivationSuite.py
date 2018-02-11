
from  testsuite.bin.entel_PageObject import TestPosts,sdata

class ValidateLegacyVenta(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateLegacyVenta, self).__init__(*args, **kwargs)

        self.url = sdata.legacy_url
        self.opType = 'venta'

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

    def test_04verifyresourceid(self):
        """ test_04verifyresourceid: Test case for test view post using GET /posts/{id}.                                 """
        self.verifyresourceid(txn_id, self.ICCID_subscriber)

    def test_05id_document(self):
        """ test_05id_document: Test case for test view post using GET /posts/{id}.                                 """
        self.id_document(txn_id)

    def test_06populationcenter(self):
        """ test_06populationcenter: Test case for test view post using GET /posts/{id}.                                 """
        self.populationcenter(txn_id)

    def test_07getplantariff(self):
        """ test_07getplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.getplantariff(txn_id, self.opType)

    def test_08selectplantariff(self):
        """ test_08selectplantariff: Test case for test view post using GET /posts/{id}.                                 """
        self.selectplantariff(txn_id, self.tarPlan)

    def test_09requestcontract(self):
        """ test_09requestcontract: Test case for test view post using GET /posts/{id}.                                 """
        self.requestcontract(txn_id, self.opType)

    def test_10contractacceptance(self):
        """ test_10contractacceptance: Test case for test view post using GET /posts/{id}.                                 """
        self.contractacceptance(txn_id)

    def test_11checknobiocounter(self):
        """ test_11checknobiocounter: Test case for test view post using GET /posts/{id}.                                 """
        self.checknobiocounter(txn_id)

    def test_12requestnobio(self):
        """ test_12requestnobio: Test case for test view post using GET /posts/{id}.                                 """
        self.requestnobio(txn_id)

    def test_13reportnobio(self):
        """ test_13reportnobio: Test case for test view post using GET /posts/{id}.                                 """
        self.reportnobio(txn_id)

    def test_14requestorder(self):
        """ test_14requestorder: Test case for test view post using GET /posts/{id}.                                 """
        self.requestorder(txn_id)
