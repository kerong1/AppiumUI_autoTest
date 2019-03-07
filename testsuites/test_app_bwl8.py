import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
class BeiwangluSearch(Base_testcase):
    def test_app_zy8(self):
        h=HomePage(self.driver)
        h.shanchu()
        h.Tuichu()
if __name__=='__main__':
    unittest.main()