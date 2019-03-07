from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import os
from framework.logger import Logger
import time
logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
    def get(self,url):
        self.driver.get(url)
        logger.info("进入网址")
    def text(self, *loc):
        el = self.find_element(*loc)
        logger.info("获取内容成功")
        return el.text
    def find_element(self,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        logger.info("成功找到元素")
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        logger.info("成功找到元素")
        return self.driver.find_elements(*loc)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.send_keys(text)
        logger.info("输入信息成功")
    def click(self,*loc):
        el=self.find_element(*loc)
        el.click()
        logger.info("点击操作成功")
    def changan(self,*loc):
        el=self.find_element(*loc)
        TouchAction(self.driver).long_press(el).wait(1000).perform()
        logger.info('长按')
    def shuijiao(self,n):
        time.sleep(n)
        logger.info("睡觉")
    def switch_to(self,*loc):
        el = self.find_element(*loc)
        self.driver.switch_to.frame(el)
        logger.info("切换frame")
        # dangqian = dir.current_window_handle
        # dir.switch_to.window(dangqian)
    def qieyemian(self,a):
        self.driver.switch_to.window(self.driver.window_handles[a])
        logger.info("切到另一个页面啦")
    def clear(self,*loc):
        el=self.find_element(*loc)
        el.clear()
        logger.info("清除")
    def hqtext(self,*loc):
        el=self.find_element(*loc)
        logger.info("获取文本值成功。")
        return el.text

    def huiche(self):
        self.driver.keyevent(66)
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime(" %Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder：/screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.info("Failed to take screenshot! %s"%e)
        logger.info("截图成功。")

    def zuola(self,*loc):
        el=self.find_element(*loc)
        TouchAction(self.driver).press(el,x=100,y=50).wait(1000).move_to(el,x=-50,y=0).release().perform()
        logger.info("向左拖拽成功")
    def xiala(self,a,b,*loc):
        el = self.find_elements(*loc)
        TouchAction(self.driver).press(el[a]).wait(1000).move_to(el[b]).release().perform()
        logger.info("向下拖拽成功")



