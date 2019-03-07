import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
class BeiwangluSearch(Base_testcase):
    def test_app_zy7(self):
        h=HomePage(self.driver)
        h.guidang()
if __name__=='__main__':
    unittest.main()