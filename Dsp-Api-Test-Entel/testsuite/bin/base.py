
#http://localhost:8008/dsp_nbi/getMessages/Test411/903323611631/9033378633300131/McRj2

import logging
import time
import os
import json
import requests
from unittest import TestCase
from testconfig import config
import cx_Oracle



class BaseTest(TestCase):

    logger=logging.getLogger('api_testsuite')
    if not os.path.exists('logs/api_testsuite.log'):os.mkdir('logs')
    handler=logging.FileHandler('logs/api_testsuite.log')
    formatter=logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                                  '%d/%m/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)



    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)



    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('api_testsuite'),
                                             {'testid': self.shortDescription().split(':')[0] or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        self.session = requests.Session()


    def tearDown(self):
        """
        Environment cleanup and logs collection.
        """
        self.session.close()
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

