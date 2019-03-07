from appium import webdriver
import warnings
from framework.browser_engine import phone
import unittest
from ddt import data,ddt,unpack
@ddt
class Base_testcase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.browser=phone()
        self.driver=self.browser.appium_desired()

    def tearDown(self):
        self.browser.close_App()
        print("结束")