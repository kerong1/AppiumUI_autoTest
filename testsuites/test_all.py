import unittest
import HTMLTestRunner
import os
import sys

sys.path.append("E:\\Appium\\")
dir='./'
c_path=os.path.dirname(os.path.abspath('.'))
report_path=os.path.join(c_path,'report')
if not os.path.exists(report_path): os.mkdir(report_path)
suite=unittest.TestLoader().discover(dir,pattern='test_app_bwl*')

if __name__=="__main__":
    html_report=report_path+r'\result.html'
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="智能备忘录测试报告",description="用例执行情况")
    runner.run(suite)