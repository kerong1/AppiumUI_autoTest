import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
class BeiwangluSearch(Base_testcase):
    def test_app_zy4(self):
        h=HomePage(self.driver)
        h.tianjia1('zxcvbnffgm')
        h.tianjia2('asdfghjkwwwel')
if __name__=='__main__':
    unittest.main()