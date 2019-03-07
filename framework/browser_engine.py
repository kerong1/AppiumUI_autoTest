import os.path
import yaml
from appium import webdriver
from framework.logger import Logger
logger=Logger(logger="phone").getlog()
class phone(object):
    apk_path = os.path.dirname(os.path.abspath('.'))
    def appium_desired(self):
        with open(os.path.dirname(os.path.abspath('.'))+ '/config/config.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)
        print(file)
        desired_caps = {}
        desired_caps['platformName'] =data['platformName']
        logger.info("读取手机信息,手机型:%s" % desired_caps['platformName'])
        desired_caps['deviceName'] = data['deviceName']
        logger.info("找到模拟机:%s" % desired_caps['deviceName'])
        desired_caps['platformVersion'] = data['platformVersion']
        logger.info("找到模拟机版本:%s" % desired_caps['platformVersion'])
        desired_caps['sessionOverride'] = True
        desired_caps['app'] =self.apk_path+'/app/znbwl.apk'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return self.driver
    def close_App(self):
        logger.info("关闭app")
        self.driver.quit()
