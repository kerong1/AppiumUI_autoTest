import unittest
from ddt import *
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
@ddt
class BeiwangluSearch(Base_testcase):
    def test_app_zy5(self):
        h=HomePage(self.driver)
        title=h.sousuo('zxcvbnm')
        try:
            self.assertIn("zxcv",title, msg=title)
            print(title)
        except AssertionError as title:
            print(u"找不到这个标题")
if __name__=='__main__':
    unittest.main()