import unittest




def get_function_args(func_ref):
    print("Im from get_function_args")


def store_class_fields(class_ref, args_passed):
    print("Im from get_function_args")


class StartWebDriverError(Exception): pass



class SeleniumTestManager():

    def __init__(self,
                 browser_name,
                 browser_version,
                 webdriver_path,
                 base_url,
                 start_webdriver_num_tries=3):
        print("Im from get_function_args")

        
    def setup(self):
        print("Im from setup")

    def teardown(self):
        print("Im from teardown")

    def _start_driver(self):
        print("Im from _start_driver")
        self.driver = "Im driver"

    def _stop_driver(self):
        print("Im from _stop_driver")

