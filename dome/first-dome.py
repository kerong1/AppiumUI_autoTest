import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
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
#测试apk包的路径
desired_caps['app']=apk_path+'/app/todolist.apk'
#不需要每次安装apk
desired_caps['noReset']=True
#应用程序的包名
desired_caps['appPackage']='com.example.todolist'
desired_caps['appActivity']='com.example.todolist.LoginActivity'

#启动app
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#登录app
driver.find_element_by_id('com.example.todolist:id/nameET').send_keys(1)
driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys(1)
driver.find_element_by_name('登入').click()
#添加新待办事项
driver.find_element_by_id('com.example.todolist:id/action_new').click()
driver.find_element_by_name('输入待办事项。。。').send_keys('jdhfhsuefks')
driver.find_element_by_id('com.example.todolist:id/saveBtn').click()

#长按
el=driver.find_element_by_id('com.example.todolist:id/toDoItemDetailTv')
TouchAction(driver).long_press(el).perform()
time.sleep(3)
#删除
driver.find_element_by_name('删除').click()
driver.find_element_by_name('确定').click()
