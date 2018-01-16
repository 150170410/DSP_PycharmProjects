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
        self.uri_dataporta= config['main']['dataporta']
        self.post_dataporta= ast.literal_eval(config['main']['post_dataporta'])
        self.uri_dataswap=config['main']['dataswap']
        self.post_dataswap=ast.literal_eval(config['main']['post_dataswap'])
        self.uri_swapreason=config['main']['swapreason']
        self.post_swapreason=ast.literal_eval(config['main']['post_swapreason'])
        self.uri_portabilityquery=config['main']['portabilityquery']
        self.post_portabilityquery=ast.literal_eval(config['main']['post_portabilityquery'])
        self.uri_sendportabilityresult=config['main']['sendportabilityresult']
        self.post_sendportabilityresult=ast.literal_eval(config['main']['post_sendportabilityresult'])
        self.uri_validatemaximumlines=config['main']['validatemaximumlines']
        self.post_validatemaximumlines = ast.literal_eval(config['main']['post_validatemaximumlines'])


    def loginuser(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_loginuser, data=self.post_loginUser)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response

    def optionmenu(self,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

        self.post_optionmenu.update({'option': opType})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_optionmenu, data=self.post_optionmenu)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])

        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]  # Returning txn_id

        self.assertEqual(self.checkOprID(txn_id), 3)
        return response

    def localizationnetw(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.        """

        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri='localizationNetw/'+txn_id+'/'+self.uri_localizationnetw)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 4)
        return response

    def verifyresourceid(self,txn_id,ICCID_subscriber):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

        self.post_verifyresourceid.update({'txn_ID': txn_id})
        self.post_verifyresourceid.update({'ICCID_subscriber': ICCID_subscriber})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_verifyresourceid, data=self.post_verifyresourceid)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id),5)
        return response

    def id_document(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """

        self.post_id_document.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_id_document, data=self.post_id_document)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 6)
        return response


    def populationcenter(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}."""

        self.post_populationcenter.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_populationcenter, data=self.post_populationcenter)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 7)
        return response

    def getplantariff(self,txn_id,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri=self.uri_getplantariff + '/'+ txn_id+ '/'+ opType)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 8)
        return response

    def selectplantariff(self,txn_id,tarPlan):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri=self.uri_selectplantariff + '/' + txn_id + '/' + tarPlan)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 9)
        return response

    def getavailablemsisdn(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_getavailablemsisdn.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_getavailablemsisdn, data=self.post_getavailablemsisdn)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 24)
        return response

    def selectnumber(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_selectnumber.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_selectnumber, data=self.post_selectnumber)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 25)
        return response

    def requestcontract(self,txn_id,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)

        response= self.get_request_response(uri=self.uri_requestcontract + '/' + txn_id + '/' + opType)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 11)
        return response

    def contractacceptance(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)

        response= self.get_request_response(uri=self.uri_contractacceptance + '/' + txn_id + '/' + '/1/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 12)
        return response

    def biometricws(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_biometricws.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_biometricws, data=self.post_biometricws)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 13)
        return response

    def requestorder(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        self.lg('%s Triggered' % self._testID)

        response= self.get_request_response(uri=self.uri_requestorder + '/' + txn_id )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 18)
        return response

    def dataporta(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_dataporta.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_dataporta, data=self.post_dataporta)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 22)
        return response

    def dataswap(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_dataswap.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_dataswap, data=self.post_dataswap)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 10)
        return response

    def swapreason(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_swapreason.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_swapreason, data=self.post_swapreason)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response

    def portabilityquery(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_portabilityquery.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_portabilityquery, data=self.post_portabilityquery)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response


    def sendportabilityresult(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_sendportabilityresult.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_sendportabilityresult, data=self.post_sendportabilityresult)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response

    def validatemaximumLines(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.post_validatemaximumLines.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=self.uri_validatemaximumLines, data=self.post_validatemaximumLines)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response

    def getmessage(self):
        """ TestCase-2: Test case for test view post using GET /posts/{id}.*        """

        self.lg('%s STARTED' % self._testID)

        response = self.get_request_response(uri=self.url_getmessage)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]
        return response

    def getPortabilityData(self):
        """ TestCase-1: Test case for test create post using POST /posts/.        """
        self.lg('%s STARTED' % self._testID)

        response = self.post_request_response(uri=self.url_getPortabilityData, data=self.post_getPortabilityData)
        self.lg(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        return response



    def checkOprID(self,txn_id):
        """ TestCase-1: Test case for test create post using POST /posts/.        """
        #txn_id = 'ACT178'

        checkQuerry="SELECT OPERATION_ID FROM DSP_TRANSACTION_DTLS where TXN_ID = '%s'" % txn_id
        self.lg("__DB connection Started__")
        con = cx_Oracle.connect('DSP_MAIN/DSP_MAIN@localhost:7779/orcl')
        cur = con.cursor()
        cur.execute(checkQuerry)
        oprID= cur.fetchall()[0][0]

        # for row in cur:    # This method is to iterate thorough the list of tuples
        #     print (row)
        #print cur.fetchall()    #fetchall()-> Fetches All rows as Array of tupples, then you can handle as an array
        # print cur.fetchone()[0]       #fetchone()->Fetches one rows as Array of tupples

        cur.close()
        con.close()
        self.lg("__DB connection closed Successfully__")
        return oprID

