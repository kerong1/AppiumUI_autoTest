import unittest
from testsuites.base_testcase import Base_testcase
from Pageobjects.app_homepage import HomePage
from ddt import data,ddt,unpack
from framework.util import Util
testdata="E:/Appium/data/data.xlsx"
sheetname="Sheet1"
@ddt
class BeiwangluSearch(Base_testcase):
    def test_app_zy2(self):
        u = Util()
        users = u.read_excel(testdata, sheetname)
        data = users[0]
        email = data["username"]
        pwd = data["userpassword"]
        data1 = users[1]
        email1 = data1["username"]
        pwd1 = data1["userpassword"]
        print(email,pwd)
        h=HomePage(self.driver)
        h.denglu(email,pwd)
        h.Tuichu()
        h.denglu(email1,pwd1)
if __name__=='__main__':
    unittest.main()
