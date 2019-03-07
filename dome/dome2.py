import os
from appium import webdriver
import yaml
import time
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
#获取根目录
apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
#设备系统
desired_caps['platformName']='Android'
#设备版本
desired_caps['platformVersion']='6.2.7.0'
#设备名称
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['sessionOverride']=True

desired_caps['app']=apk_path+'/app/znbwl.apk'
#不需要每次安装apk
desired_caps['noReset']=True
desired_caps['appPackage']='com.pdswp.su.smartcalendar'
desired_caps['appActivity']='com.pdswp.su.smartcalendar.WelcomeNote'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(10)

#注册
# driver.find_element_by_class_name('android.widget.ImageView').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/username').click()
# driver.find_element_by_name('注册一个吧!').click()
# driver.find_element_by_name('昵称').send_keys(1)
# driver.find_element_by_name('注册邮箱(这将是您的账号)').send_keys('125466@qq.com')
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/password').send_keys(11111111)
# time.sleep(5)
# driver.find_element_by_name('注册').click()

#登录
# driver.find_element_by_class_name('android.widget.ImageView').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/username').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/email').send_keys('125466@qq.com')
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/password').send_keys(11111111)
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/login').click()
#退出
# time.sleep(3)
# driver.find_element_by_class_name('android.widget.ImageView').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/login').click()
# driver.find_element_by_name('退出当前账号').click()
# #注册
# driver.find_element_by_class_name('android.widget.ImageView').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/username').click()
# driver.find_element_by_name('注册一个吧!').click()
# driver.find_element_by_name('昵称').send_keys(1)
# driver.find_element_by_name('注册邮箱(这将是您的账号)').send_keys('125466@qq.com')
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/password').send_keys(11111111)
# time.sleep(5)
# driver.find_element_by_name('注册').click()
# print('注册失败')

#修改用户名
# driver.find_element_by_class_name('android.widget.ImageView').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/login').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/title').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/username').send_keys('zkr')
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/quick_add').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/ab_icon2').click()

#添加备忘录+
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/menuAdd').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/add_input_content').send_keys('aaaaaaa')
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/quick_add').click()

# driver.find_element_by_class_name('android.widget.ImageView').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/design_menu_item_text').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/add_input_content').send_keys('bbbbbb')
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/quick_add').click()

# #搜索
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/toolbar_search').click()
# driver.find_element_by_id('android:id/search_src_text').send_keys('aaa')
# driver.keyevent(66)
# 排序
px=driver.find_element_by_id('com.pdswp.su.smartcalendar:id/note_title')
TouchAction(driver).long_press(px).perform()
time.sleep(3)
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/menu_sort').click()
time.sleep(3)
e1=driver.find_elements_by_id('com.pdswp.su.smartcalendar:id/sortBtn')
TouchAction(driver).press(e1[0]).wait(1000).move_to(e1[3]).release().perform()

#归档
# px=driver.find_element_by_id('com.pdswp.su.smartcalendar:id/note_title')
# TouchAction(driver).long_press(px).perform()
# time.sleep(3)
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/menu_archive').click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/ab_icon2').click()
# #gui
# driver.find_element_by_name('归档').click()
# el=driver.find_element_by_id('com.pdswp.su.smartcalendar:id/note_title')
# TouchAction(driver).press(el,x=100,y=50).wait(1000).move_to(el,x=-50,y=0).release().perform()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/menu').click()