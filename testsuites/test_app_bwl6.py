import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
class BeiwangluSearch(Base_testcase):
    def test_app_zy6(self):
        h=HomePage(self.driver)
        h.paixu(0,3)
if __name__=='__main__':
    unittest.main()