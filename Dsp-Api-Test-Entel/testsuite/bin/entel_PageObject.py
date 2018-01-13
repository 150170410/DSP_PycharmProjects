from  testsuite.bin.base import *
from testconfig import config
import types
import ast


response_headers = {'Content-Type': 'application/json;charset=UTF-8'}


class TestPosts(BaseTest):

    def __init__(self, *args, **kwargs):
        super(TestPosts, self).__init__(*args, **kwargs)
        self.url = config['main']['url']
        self.url_getmessage = config['main']['url_getmessage']
        self.url_getPortabilityData = config['main']['getportabilitydata']
        self.post_getPortabilityData = ast.literal_eval(config['main']['post_getportabilitydata'])
        self.uri_loginuser = config['main']['loginuser']
        self.post_loginUser = ast.literal_eval(config['main']['post_loginuser'])
        self.uri_optionmenu = config['main']['optionmenu']
        self.post_optionmenu = ast.literal_eval(config['main']['post_optionmenu'])
        self.uri_localizationnetw = config['main']['localizationnetw']
        self.uri_verifyresourceid = config['main']['verifyresourceid']
        self.post_verifyresourceid = ast.literal_eval(config['main']['post_verifyresourceid'])
        self.uri_id_document = config['main']['id_document']
        self.post_id_document = ast.literal_eval(config['main']['post_id_document'])
        self.uri_populationcenter = config['main']['populationcenter']
        self.post_populationcenter = ast.literal_eval(config['main']['post_populationcenter'])
        self.uri_getplantariff = config['main']['getplantariff']
        self.uri_selectplantariff = config['main']['selectplantariff']
        self.uri_getavailablemsisdn = config['main']['getavailablemsisdn']
        self.post_getavailablemsisdn = ast.literal_eval(config['main']['post_getavailablemsisdn'])
        self.uri_selectnumber = config['main']['selectnumber']
        self.post_selectnumber = ast.literal_eval(config['main']['post_selectnumber'])
        self.uri_requestcontract = config['main']['requestcontract']
        self.uri_contractacceptance = config['main']['contractacceptance']
        self.uri_biometricws = config['main']['biometricws']
        self.post_biometricws = ast.literal_eval(config['main']['post_biometricws'])
        self.uri_requestorder = config['main']['requestorder']
        self.uri_dataPorta= config['main']['dataporta']
        self.post_dataPorta= config['main']['post_dataporta']




    def loginuser(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_loginuser, data=self.post_loginUser)

    def optionmenu(self,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

        self.post_optionmenu.update({'option': opType})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_optionmenu, data=self.post_optionmenu)

    def localizationnetw(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.        """

        self.lg('%s Triggered' % self._testID)
        return self.get_request_response(uri='localizationNetw/'+txn_id+'/'+self.uri_localizationnetw)

    def verifyresourceid(self,txn_id,ICCID_subscriber):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

        self.post_verifyresourceid.update({'txn_ID': txn_id})
        self.post_verifyresourceid.update({'ICCID_subscriber': ICCID_subscriber})

        self.lg('%s Triggered' % self._testID)
        self.lg(self.post_verifyresourceid)
        return self.post_request_response(uri=self.uri_verifyresourceid, data=self.post_verifyresourceid)

    def id_document(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """

        self.post_id_document.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_id_document, data=self.post_id_document)


    def populationcenter(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}."""

        self.post_populationcenter.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_populationcenter, data=self.post_populationcenter)

    def getplantariff(self,txn_id,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        return self.get_request_response(uri=self.uri_getplantariff + '/'+ txn_id+ '/'+ opType)

    def selectplantariff(self,txn_id,tarPlan):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        return self.get_request_response(uri=self.uri_selectplantariff + '/' + txn_id + '/' + tarPlan)

    def getavailablemsisdn(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_getavailablemsisdn.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_getavailablemsisdn, data=self.post_getavailablemsisdn)

    def selectnumber(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_selectnumber.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_selectnumber, data=self.post_selectnumber)

    def requestcontract(self,txn_id,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)

        return self.get_request_response(uri=self.uri_requestcontract + '/' + txn_id + '/' + opType)

    def contractacceptance(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)

        return self.get_request_response(uri=self.uri_contractacceptance + '/' + txn_id + '/' + '/1/1')

    def biometricws(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_biometricws.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_biometricws, data=self.post_biometricws)

    def requestorder(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        self.lg('%s Triggered' % self._testID)

        return self.get_request_response(uri=self.uri_requestorder + '/' + txn_id )

    def dataporta(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_dataPorta.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_dataPorta, data=self.post_dataPorta)


    def getmessage(self):
        """ TestCase-2: Test case for test view post using GET /posts/{id}.*        """

        self.lg('%s STARTED' % self._testID)

        response = self.get_request_response(uri=self.url_getmessage)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]

        self.lg('%s ENDED' % self._testID)

    def getPortabilityData(self):
        """ TestCase-1: Test case for test create post using POST /posts/.        """
        self.lg('%s STARTED' % self._testID)

        response = self.post_request_response(uri=self.url_getPortabilityData, data=self.post_getPortabilityData)

        self.lg(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        self.lg('%s ENDED' % self._testID)