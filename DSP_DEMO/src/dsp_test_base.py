import unittest
import dsp_test_manager
from dsp_test_manager import SeleniumTestManager


class BaseDspTest():
    default_implicit_wait_time = 2
    default_explicit_wait_time = 10
    default_window_size = {'width': 1280, 'height': 720}
    default_window_position = {'x': 0, 'y': 0}

    @classmethod
    def setUpClass(cls):
        print("Im from setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Im from tearDownClass")

    def setUp(self):
        print("Im from setUp")
        self.driver=self.get_driver();

    def tearDown(self):
        print("Im from tearDown")

    @classmethod
    def get_driver(cls):
        print("Im from get_driver")
        return cls.dsp_test_manager.driver

    def reset_command_wait_time(self):
        print("Im from reset_command_wait_time")

    @classmethod
    def get_screenshot_dir(cls):
        print("Im from get_screenshot_dir")

    def take_screenshot(self, name=None):
        print("Im from take_screenshot")

