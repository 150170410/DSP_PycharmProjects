from  testsuite.bin.base import *
import staticDdata as sdata


response_headers = {'Content-Type': 'application/json;charset=UTF-8'}


class TestPosts(BaseTest):

    def __init__(self, *args, **kwargs):
        super(TestPosts, self).__init__(*args, **kwargs)

        self.ICCID_subscriber = sdata.iccid_subscriber
        self.portedMsisdn = sdata.portedmsisdn
        self.portStatus = sdata.portstatus
        self.tarPlan = sdata.tarplan
        self.legacy_localzn = sdata.legacy_localzn
        self.tde_localzn = sdata.tde_localzn

    def loginuser(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.loginuser, data=sdata.post_loginuser)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response

    def optionmenu(self,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

        sdata.post_optionmenu.update({'option': opType})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.optionmenu, data=sdata.post_optionmenu)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])

        txn_id = response.text.split(',')[2].split(':')[1].split('"')[1]  # Returning txn_id

        self.assertEqual(self.checkOprID(txn_id), 3)
        return response

    def localizationnetw(self,txn_id,inparams):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.        """

        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri=sdata.localizationnetw+'/'+txn_id+inparams)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 4)
        return response

    def verifyresourceid(self,txn_id,ICCID_subscriber):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.      """

        sdata.post_verifyresourceid.update({'txn_ID': txn_id})
        sdata.post_verifyresourceid.update({'ICCID_subscriber': ICCID_subscriber})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.verifyresourceid, data=sdata.post_verifyresourceid)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id),5)
        return response

    def id_document(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """

        sdata.post_id_document.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.id_document, data=sdata.post_id_document)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 6)
        return response

    def populationcenter(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}."""

        sdata.post_populationcenter.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.populationcenter, data=sdata.post_populationcenter)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 7)
        return response

    def getplantariff(self,txn_id,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri=sdata.getplantariff + '/'+ txn_id+ '/'+ opType)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 8)
        return response

    def selectplantariff(self,txn_id,tarPlan):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri=sdata.selectplantariff + '/' + txn_id + '/' + tarPlan)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 9)
        return response

    def getavailablemsisdn(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_getavailablemsisdn.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.getavailablemsisdn, data=sdata.post_getavailablemsisdn)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 24)
        return response

    def selectnumber(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_selectnumber.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.selectnumber, data=sdata.post_selectnumber)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 25)
        return response

    def requestcontract(self,txn_id,opType):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)
        response= self.get_request_response(uri=sdata.requestcontract + '/' + txn_id + '/' + opType)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 11)
        return response

    def contractacceptance(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)
        tempContract = sdata.contractacceptance %txn_id

        response= self.get_request_response(uri=tempContract)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 12)
        return response

    def biometricws(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_biometricws.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.biometricws, data=sdata.post_biometricws)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 13)
        return response

    def checknobiocounter(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)
        tempbio_uri = sdata.checknobiocounter % txn_id

        response = self.get_request_response(uri=tempbio_uri)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 14)
        return response

    def requestnobio(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)
        tempbio_uri = sdata.requestnobio % txn_id

        response = self.get_request_response(uri=tempbio_uri)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 15)
        return response

    def reportnobio(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.*                """
        self.lg('%s Triggered' % self._testID)
        sdata.post_reportnobio.update({'txn_ID': txn_id})

        response = self.post_request_response(uri=sdata.reportnobio, data=sdata.post_reportnobio)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 16)
        return response

    def requestorder(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """
        self.lg('%s Triggered' % self._testID)

        response= self.get_request_response(uri=sdata.requestorder + '/' + txn_id )
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 18)
        return response

    def dataporta(self,txn_id,portedMsisdn):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_dataporta.update({'txn_ID': txn_id})
        sdata.post_dataporta.update({'telNumber': portedMsisdn})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.dataporta, data=sdata.post_dataporta)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 22)
        return response

    def dataswap(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_dataswap.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.dataswap, data=sdata.post_dataswap)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 10)
        return response

    def swapreason(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_swapreason.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.swapreason, data=sdata.post_swapreason)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 26)
        return response

    def transactionquery(self,msisdn):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_tde_transactionQuery.update({'MSISDNPorted': msisdn})

        self.lg('%s Triggered' % self._testID)
        response = self.post_request_response(uri=sdata.tde_transactionquery, data=sdata.post_tde_transactionQuery)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        # self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        return response

    def portabilityquery(self,txn_id,portedMsisdn,substype):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_portabilityquery.update({'txn_ID': txn_id})
        sdata.post_portabilityquery.update({'telNumber': portedMsisdn})
        sdata.post_portabilityquery.update({'subsType': substype})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.portabilityquery, data=sdata.post_portabilityquery)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 30)
        return response

    def sendportabilityresult(self,txn_id,portedMsisdn,portStatus):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_sendportabilityresult.update({'portedMsisdn': portedMsisdn})
        sdata.post_sendportabilityresult.update({'msisdn': portedMsisdn})
        sdata.post_portaqueryresult['portabilityUpdate'].update({'PortabilityIdMessage': portStatus})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.sendportabilityresult, data=sdata.post_sendportabilityresult)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 23)
        return response

    def portaqueryresult(self,portedMsisdn,portStatus,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_portaqueryresult['portabilityUpdate'].update({'PortabilityNumber': txn_id})
        sdata.post_portaqueryresult['portabilityUpdate'].update({'PortabilityMSISDN': portedMsisdn})
        sdata.post_portaqueryresult['portabilityUpdate'].update({'PortabilityIdMessage': portStatus})

        self.lg('%s Triggered' % self._testID)
        response = self.post_request_response(uri=sdata.portaqueryresult, data=sdata.post_portaqueryresult)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[2], '"0"', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 23)
        return response


    def validatemaximumLines(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_validatemaximumlines.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response= self.post_request_response(uri=sdata.validatemaximumlines, data=sdata.post_validatemaximumlines)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '0', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 31)
        return response

    def verifycustomerdata(self,txn_id):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                """

        sdata.post_verifycustomerdata.update({'txn_ID': txn_id})

        self.lg('%s Triggered' % self._testID)
        response = self.post_request_response(uri=sdata.verifycustomerdata, data=sdata.post_verifycustomerdata)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1], '"0"', response.text.split(',')[1])
        self.assertEqual(self.checkOprID(txn_id), 31)
        return response

    def getmessage(self):
        """ TestCase-2: Test case for test view post using GET /posts/{id}.*        """

        self.lg('%s STARTED' % self._testID)

        response = self.get_request_response(uri=sdata.url_getmessage)
        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]
        return response

    def getPortabilityData(self):
        """ TestCase-1: Test case for test create post using POST /posts/.        """
        self.lg('%s STARTED' % self._testID)

        response = self.post_request_response(uri=sdata.getportabilitydata, data=sdata.post_getportabilitydata)
        self.lg(response.text)
        self.lg(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        return response

    def checkOprID(self,txn_id):
        """ TestCase-1: Test case for test create post using POST /posts/.        """
        #txn_id = 'ACT178'

        checkQuerry="SELECT OPERATION_ID FROM DSP_TRANSACTION_DTLS where TXN_ID = '%s'" % txn_id

        cur = self.con.cursor()
        cur.execute(checkQuerry)
        oprID= cur.fetchall()[0][0]

        cur.close()
        return oprID

