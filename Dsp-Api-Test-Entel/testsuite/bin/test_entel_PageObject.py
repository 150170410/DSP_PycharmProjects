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
        self.post_requestorder = ast.literal_eval(config['main']['post_requestorder'])



    def loginuser(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        return self.post_request_response(uri=self.uri_loginuser, data=self.post_loginUser)

    def optionmenu(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

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
        return self.post_request_response(uri=self.uri_populationcenter, data=self.post_id_document)

    def getplantariff(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        pass

    def selectplantariff(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        pass

    def getavailablemsisdn(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        pass

    def selectnumber(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        pass

    def requestcontract(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        pass

    def biometricws(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        pass

    def requestorder(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        pass



    def getmessage(self):
        """ TestCase-2: Test case for test view post using GET /posts/{id}.*
        **Test Scenario:**
        #. View post using GET /posts/{id}, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """

        self.lg('%s STARTED' % self._testID)

        self.lg('#. View post using GET /posts/{id}, should succeed')
        # ***    response = self.get_request_response(uri='/posts/%d' % post["id"])
        response = self.get_request_response(uri=self.url_getmessage)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        # print (response.json())
        # print(response.headers.keys())
        # print(response.headers)

        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]

        # self.lg('#. Check response body, should succeed')
        # self.assertEqual(type(response.json()), types.DictType)
        # [self.assertEqual(response.json()[key], post[key]) for key in response.json().keys()]

        self.lg('%s ENDED' % self._testID)
        # ----------------------------------------------------------

    def getPortabilityData(self):
        """ TestCase-1: Test case for test create post using POST /posts/.*
        **Test Scenario:**
        #. Create post using POST /posts/, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """
        self.lg('%s STARTED' % self._testID)

        self.lg('#. Create post using POST /posts/, should succeed')
        # ***    response = self.post_request_response(uri='/posts', data=post)
        response = self.post_request_response(uri=self.url_getPortabilityData, data=self.post_getPortabilityData)

        self.lg(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        # print (response.json())
        # print('***************************')
        # print(response.headers)


        # self.lg('#. Check response headers, should succeed')
        # [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        # [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]
        #
        # self.lg('#. Check response body, should succeed')
        # self.assertEqual(type(response.json()), types.DictType)
        # self.assertEqual(response.json(), posturi)

        self.lg('%s ENDED' % self._testID)