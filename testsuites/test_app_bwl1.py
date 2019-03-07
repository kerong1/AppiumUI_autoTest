import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
class BeiwangluSearch(Base_testcase):
    def test_app_zy1(self):
        h=HomePage(self.driver)
        h.zhuce("9oegwnj6","kdgk1@qq.com","asdfghjk")
        h.Tuichu()
        h.zhuce("zkr","19970705@qq.com","19970705")
if __name__=='__main__':
    unittest.main()
