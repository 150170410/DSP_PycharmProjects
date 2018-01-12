
from  testsuite.bin.test_entel_PageObject import *

class ValidateLegacyVenta(TestPosts):
    def __init__(self,*args, **kwargs):
        super(ValidateLegacyVenta, self).__init__(*args, **kwargs)


    def loginUser(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                          """

        response=self.loginuser()

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])

    def test_01optionMenu(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                          """

        response=self.optionmenu()

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        global txn_id
        txn_id= response.text.split(',')[2].split(':')[1].split('"')[1]    #Returning txn_id

    def test_02localizationnetw(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                                 """

        #txn_id = self.test_01optionMenu().

        response=self.localizationnetw(txn_id)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])

    def test_03verifyresourceid(self):
        """ EntelRegressionSuite: Test case for test view post using GET /posts/{id}.                                 """

        ICCID_subscriber=89560100000792428976

        response=self.verifyresourceid(txn_id,ICCID_subscriber)

        self.lg(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.text.split(',')[0].split(':')[1],'0',response.text.split(',')[1])
        self.lg(response.text.split(',')[2].split(':')[1].split('"')[1])