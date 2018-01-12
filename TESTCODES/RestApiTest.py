
#http://localhost:8008/dsp_nbi/getMessages/Test411/903323611631/9033378633300131/McRj2

import logging
import time
import os

import requests
from unittest import TestCase

from testconfig import config

import json

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
 #****       self.url = config['main']['url']
        self.url='http://localhost:8008/dsp_nbi/'

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
#----------------------------------------------------------------------------------------


import types
response_headers = {'Content-Type': 'application/json;charset=UTF-8'}

'''post = {"id": 1,
        "userId": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
'''
geturi ='getMessages/Test411/903323611631/9033378633300131/McRj2'
posturi='getPortabilityData'

postdata={
	"docValue":"DNIABC88",
	"portedMsisdn":""
}

class TestPosts(BaseTest):

    def test_view(self):
        """ TestCase-2: Test case for test view post using GET /posts/{id}.*
        **Test Scenario:**
        #. View post using GET /posts/{id}, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """
        self.lg('%s STARTED' % self._testID)

        self.lg('#. View post using GET /posts/{id}, should succeed')
#***    response = self.get_request_response(uri='/posts/%d' % post["id"])
        response=self.get_request_response(uri=geturi)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        # print (response.json())
        # print('***************************')
        # print(response.headers.keys())
        # print('***************************')
        # print(response.headers)

        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]

        # self.lg('#. Check response body, should succeed')
        # self.assertEqual(type(response.json()), types.DictType)
        # [self.assertEqual(response.json()[key], post[key]) for key in response.json().keys()]

        self.lg('%s ENDED' % self._testID)
#----------------------------------------------------------

    def test_create(self):
        """ TestCase-1: Test case for test create post using POST /posts/.*
        **Test Scenario:**
        #. Create post using POST /posts/, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """
        self.lg('%s STARTED' % self._testID)

        self.lg('#. Create post using POST /posts/, should succeed')
#***    response = self.post_request_response(uri='/posts', data=post)
        response = self.post_request_response(uri=posturi,data=postdata)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        print (response.json())
        print('***************************')
        print(response.headers)


        # self.lg('#. Check response headers, should succeed')
        # [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        # [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]
        #
        # self.lg('#. Check response body, should succeed')
        # self.assertEqual(type(response.json()), types.DictType)
        # self.assertEqual(response.json(), posturi)

        self.lg('%s ENDED' % self._testID)