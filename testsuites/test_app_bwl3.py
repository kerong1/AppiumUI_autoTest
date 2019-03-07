import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
class BeiwangluSearch(Base_testcase):
    def test_app_zy3(self):
        h=HomePage(self.driver)
        h.denglu("125466@qq.com", "11111111")
        h.xiugai('llvvlllvvv')
if __name__=='__main__':
    unittest.main()
