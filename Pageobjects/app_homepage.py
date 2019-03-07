from Pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    # 展开注册按钮
    mulu=(By.ID,'com.pdswp.su.smartcalendar:id/ab_icon2')
    # 登录按钮进入注册
    jinruzhuce=(By.ID,'com.pdswp.su.smartcalendar:id/email')
    #注册按钮
    zhuceanniu=(By.ID,'com.pdswp.su.smartcalendar:id/register')
    # 注册昵称输入框
    zhucekuang=(By.ID,'com.pdswp.su.smartcalendar:id/username')
    # 注册邮箱输入框
    youxiangkuang=(By.ID,'com.pdswp.su.smartcalendar:id/email')
    # 注册密码输入框
    mimakuang=(By.ID,'com.pdswp.su.smartcalendar:id/password')
    # 提交注册
    tijiao=(By.ID,'com.pdswp.su.smartcalendar:id/reguser')
    #退出
    tuichu=(By.ID,'com.pdswp.su.smartcalendar:id/exit')
    #登录
    dengluanniu=(By.ID,'com.pdswp.su.smartcalendar:id/login')
    #账户信息
    zhanghuxinxi=(By.ID,'com.pdswp.su.smartcalendar:id/login')
    #用户名
    yonghuming=(By.ID,'com.pdswp.su.smartcalendar:id/title')
    #修改框
    xiugaikuang=(By.ID,'com.pdswp.su.smartcalendar:id/username')
    #修改对勾
    duigou=(By.ID,'com.pdswp.su.smartcalendar:id/quick_add')
    #加号添加
    jiahao=(By.ID,'com.pdswp.su.smartcalendar:id/menuAdd')
    #添加文本
    tianjiawenben=(By.ID,'com.pdswp.su.smartcalendar:id/add_input_content')
    #添加保存
    tianjiabaocun=(By.ID,'com.pdswp.su.smartcalendar:id/quick_add')
    #添加备忘
    tianjiabeiwang=(By.ID,'com.pdswp.su.smartcalendar:id/design_menu_item_text')
    #搜索
    sousuoanniu=(By.ID,'com.pdswp.su.smartcalendar:id/toolbar_search')
    #搜索文本
    sousuowenben=(By.ID,'android:id/search_src_text')
    #第一个备忘录
    firsttext=(By.ID,'com.pdswp.su.smartcalendar:id/note_title')
    #归档
    gdang=(By.ID,'com.pdswp.su.smartcalendar:id/menu_archive')
    #目录归档
    gdang1=(By.NAME,'归档')
    #还原备忘录
    hytext=(By.ID,'com.pdswp.su.smartcalendar:id/note_title')
    #恢复
    huifu=(By.ID,'com.pdswp.su.smartcalendar:id/menu')
    #删除
    schu=(By.NAME,'删除备忘')
    #回收站
    hszhan=(By.NAME,'回收站')
    #清空
    qkhsz=(By.NAME,'清空回收站')
    queding=(By.NAME,'确定')
    #排序
    pxu=(By.ID,'com.pdswp.su.smartcalendar:id/menu_sort')
    #移动箭头
    ydjiantou=(By.ID,'com.pdswp.su.smartcalendar:id/sortBtn')

    def zhuce(self,text1,text2,text3):
        self.click(*self.mulu)
        self.click(*self.jinruzhuce)
        self.click(*self.zhuceanniu)
        self.sendkeys(text1,*self.zhucekuang)
        self.sendkeys(text2,*self.youxiangkuang)
        self.sendkeys(text3,*self.mimakuang)
        self.click(*self.tijiao)
    def Tuichu(self):
        self.click(*self.mulu)
        self.click(*self.jinruzhuce)
        self.click(*self.tuichu)
    def denglu(self,text1,text2):
        self.click(*self.mulu)
        self.click(*self.jinruzhuce)
        self.clear(*self.youxiangkuang)
        self.sendkeys(text1, *self.youxiangkuang)
        self.sendkeys(text2, *self.mimakuang)
        self.click(*self.dengluanniu)
    def xiugai(self,text):
        self.click(*self.mulu)
        self.click(*self.zhanghuxinxi)
        self.click(*self.yonghuming)
        self.sendkeys(text,*self.xiugaikuang)
        self.click(*self.duigou)
        self.click(*self.mulu)
    def tianjia1(self,text):
        self.click(*self.jiahao)
        self.sendkeys(text,*self.tianjiawenben)
        self.click(*self.tianjiabaocun)
    def tianjia2(self,text):
        self.click(*self.mulu)
        self.click(*self.tianjiabeiwang)
        self.sendkeys(text, *self.tianjiawenben)
        self.click(*self.tianjiabaocun)
    def sousuo(self,text1):
        self.click(*self.sousuoanniu)
        self.sendkeys(text1,*self.sousuowenben)
        self.huiche()
        title=self.text(*self.firsttext)
        time.sleep(2)
        return title
    def guidang(self):
        self.changan(*self.firsttext)
        self.click(*self.gdang)
        self.click(*self.mulu)
        self.click(*self.gdang1)
        self.zuola(*self.hytext)
        self.click(*self.huifu)
        self.click(*self.mulu)
    def shanchu(self):
        self.changan(*self.firsttext)
        self.click(*self.schu)
        self.click(*self.mulu)
        self.click(*self.hszhan)
        self.click(*self.qkhsz)
        self.click(*self.queding)
        self.click(*self.mulu)
    def paixu(self,a,b):
        self.changan(*self.firsttext)
        self.click(*self.pxu)
        self.get_windows_img()
        self.xiala(a,b,*self.ydjiantou)







