import logging
from logging.handlers import TimedRotatingFileHandler
import time
import os
import json
import requests
from unittest import TestCase
import cx_Oracle
import smtplib


def setup_module():
    print(__name__, ': setup_module() ~~~~~~~~~~~~~~~~~~~~~~')


def teardown_module():
    print(__name__, ': teardown_module() ~~~~~~~~~~~~~~~~~~~')


class BaseTest(TestCase):

    logger=logging.getLogger('entel_test')
    if not os.path.exists('logs/entel_test.log'):os.mkdir('logs')
    handler=TimedRotatingFileHandler('logs/entel_test.log',
                                     when="d",interval=1,backupCount=0)
    formatter=logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                                  '%d/%m/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)


    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()
        cls.con = cx_Oracle.connect('DSP_MAIN/DSP_MAIN@localhost:8009/orcl')
        print("*******---DB Connection Started----********")

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        cls.con.close()
        print("*******---DB Connection Closed----********")


    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('entel_test'),
                                             {'testid': self.shortDescription().split(':')[0] or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        # self.session = requests.Session()


    def tearDown(self):
        """
        Environment cleanup and logs collection.
        """
        # self.session.close()
        if hasattr(self, '_startTime'):
            executionTime = time.time() - self._startTime
        self.lg('Testcase %s Execution Time is %s sec.' % (self._testID, executionTime))


    def lg(self, msg):
        self._logger.info(msg)

    def get_request_response(self, uri, headers=None, payload=None):
        if headers == None:
            headers = {"Content-Type": "application/json"}
        self.lg('GET %s' % self.url + uri)
        return self.session.get(self.url + uri, params=payload, headers=headers, timeout=30, allow_redirects=False)

    def post_request_response(self, uri, data, headers=None):
        if headers == None:
            headers = {"Content-Type": "application/json"}
        self.lg('POST %s' % self.url + uri)
        return self.session.post(self.url + uri, data=json.dumps(data), headers=headers, timeout=30,
                                 allow_redirects=False)

    def send_mail(self):

        subject = 'Entel Test Results**'
        text = '''debasis.dash@hpe.com
                Subject: testin
                This is a test '''

        email_from = 'entel_test@hpe.com'
        email_to = 'debasis.dash@hpe.com'
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP('15.241.48.71')
        server.sendmail(email_from, email_to, message)
        server.quit()