#coding=utf-8


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time,datetime
from ..pageobject.basePage import BasePage as BP

class BasePageAction():

    def __init__(self,driver):
        self.driver = driver


    def waitElePresents(self,loc,seconds=10,poll_frequency=0.5):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False

    def waitElesPresents(self,loc,seconds=10,poll_frequency=0.5): ##返回所有elements
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_all_elements_located(loc))
            return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False


    def waitEleClick(self,loc,seconds=10,poll_frequency=0.5):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.element_to_be_clickable(loc))
            ele.click()
            return ele
        except TimeoutException as e:
            print(e)
            # print(loc)
            return False

    def switchPage(self,loc,seconds=10,poll_frequency=0.5):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            if ele.is_selected():
                return ele
            else:
                ele.click()
                return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False


    def savePNG(self,name,printPng=True):
        _name = os.path.abspath(os.path.join(os.path.curdir, "screenshots", name+".png"))
        self.driver.get_screenshot_as_file(_name)
        src = "..\screenshots\%s" % name+".png"
        if printPng:
            print(r'''<img src="%(src)s"  alt="%(filename)s"  title="%(filename)s" height="100" width="100" class="pimg"  onclick="javascript:window.open(this.src);"/>%(filename)s''' % {'filename':name,"src":src})

    def waitStaleness(self,ele,seconds=5,poll_frequency=0.5):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.staleness_of(ele))
            return True
        except TimeoutException as e:
            print(e)
            return False

    ## 开屏跳过
    def passJump(self,seconds=30,poll_frequency=0.1):
        _jump = self.waitPresents(BP.JUMP,seconds=seconds,poll_frequency=poll_frequency)
        if _jump:
            self.savePNG("跳过出现")
            self.waitStaleness(_jump)
            self.savePNG("跳过消失")
        return True

    ## 检查开屏splash
    def checkSplash(self,bachInit,seconds=20,poll_frequency=0.1):
        _jump = self.waitPresents(BP.JUMP,seconds=seconds,poll_frequency=poll_frequency)
        if _jump:
            _splash = self.waitClick(BP.JUMPPAGE,seconds=seconds,poll_frequency=poll_frequency)
            self.savePNG("开屏页截屏")
            if bachInit:
                wc = self.waitPresents(BP.WEBVIEWCLOSE)
                time.sleep(5)
                self.savePNG("开屏页跳转页面展示")
                wc.click()
                self.waitStaleness(wc)
                self.savePNG("开屏页跳转页面关闭")
                return True
            return True
        else:
            print("未发现开屏页")
            return False #


    ## all=True时，将所有的value返回；all=False时，只返回今天周几
    def getWeekday(self,all=True):
        week_day_dict = {
                    0 : '周一',
                    1 : '周二',
                    2 : '周三',
                    3 : '周四',
                    4 : '周五',
                    5 : '周六',
                    6 : '周日',
                    7 : '完结',
                    }
        cur_time = datetime.datetime.now()
        day = cur_time.weekday()
        if all:
            week_day_dict[day]="今天"
            return week_day_dict.values()
        else:
            return week_day_dict[day]


    def startAppCloseAlert(self):
        self.waitEleClick(BP.SYSALLOW,seconds=5)
        self.waitEleClick(BP.SYSCONFIRM,seconds=5)
        self.waitEleClick(BP.H5CLOSE,seconds=5)

    def waitTextInPage(self,text,seconds=10,poll_frequency=0.5):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(lambda x:text in x.page_source)
            return True
        except TimeoutException as e:
            print(e)
            print(text)
            return False

    def pickerWheel(self,element):
        self.driver.execute_script('mobile: selectPickerWheelValue', {'order': 'next', 'offset': 0.15, 'element': element});



    def getBack(self):
        self.waitEleClick(BP.BTNBACK)


    def getInMyPage(self,):
        mybtn = self.waitElePresents(BP.MY)
        mybtn.click()
        # if self.waitElePresents(MP.APPINFO,seconds=3):
        #     pass
        # else:
        #     self.getInMyPage()
        # self.waitEleClick(BP.MY)
        # ele = self.waitElePresents(BP.MY)
        # if ele:
        #     self.tapElement(ele)

    def getInMyToon(self):
        mybtn = self.waitElePresents(BP.MYCARTOON)
        mybtn.click()
        # if self.waitElePresents(MCP.RECENTLY,seconds=3):
        #     pass
        # else:
        #     self.getInMyToon()



    def getInFoundPage(self):
        mybtn = self.waitElePresents(BP.DISCOVERY)
        mybtn.click()

        # if self.waitElePresents(DP.RECOMMEND,seconds=3):
        #     pass
        # else:
        #     self.getInFoundPage()
        # self.waitEleClick(BP.DISCOVERY)
        # ele = self.waitElePresents(BP.DISCOVERY)
        # if ele:
        #     self.tapElement(ele)

    def getInUpdatePage(self):
        mybtn = self.waitElePresents(BP.UPDATE)
        mybtn.click()
        # if flag:
        #     mybtn.click()
        # else:
        #     mybtn.double_click()
        # if self.waitElePresents(UP.END):
        #     pass
        # else:
        #     self.getInUpdatePage(not flag)
        # self.waitEleClick(BP.UPDATE)
        # ele = self.waitElePresents(BP.UPDATE)
        # if ele:
        #     self.tapElement(ele)


    def swipeUp(self):
        self.driver.execute_script("mobile: swipe", {"direction": "up"})

    def swipeDown(self):
        self.driver.execute_script("mobile: swipe", {"direction": "down"})

    def swipeLeft(self):
        self.driver.execute_script("mobile: swipe", {"direction": "left"})

    def swipeRight(self):
        self.driver.execute_script("mobile: swipe", {"direction": "right"})

    def scrollUp(self):
        self.driver.execute_script("mobile: scroll", {"direction": "up"})

    def scrollDown(self):
        self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def scrollLeft(self):
        self.driver.execute_script("mobile: scroll", {"direction": "left"})

    def scrollRight(self):
        self.driver.execute_script("mobile: scroll", {"direction": "right"})


    def tapElement(self,element):
        # actions = TouchAction(self.driver)
        # actions.tap(element)
        # actions.perform()
        self.driver.execute_script('mobile: tap', {'element': element.get_attribute("name"),'x':0.1,'y':0.1});

    def terminalAPP(self,name="QQ"):
        lowername = name.lower()
        if lowername == "qq":
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.tencent.mqq'})
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.tencent.mqq'})
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.naver.linewebtoon.cn'})

        elif lowername == "weibo":
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.sina.weibo'})
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.sina.weibo'})
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.naver.linewebtoon.cn'})

        elif lowername == "wechat":
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.tencent.xin'})
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.tencent.xin'})
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.naver.linewebtoon.cn'})

        else:
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.naver.linewebtoon.cn'})


    def Scroll2Tail(self):
        moon = self.waitElePresents(BP.MOONICON)
        self.waitStaleness(moon)
        # sv = self.waitElePresents(BP.SCROLLVIEWER)
        topEle = self.waitElePresents(BP.TOTOP)
        self.driver.execute_script('mobile: scroll', {'element': topEle.get_attribute("name"),'toVisible':True})
        self.savePNG("SCROLLTO TOP")

    def Scroll2Subscribe(self):
        moon = self.waitElePresents(BP.MOONICON)
        self.waitStaleness(moon)
        # sv = self.waitElePresents(BP.SCROLLVIEWER)
        subEle = self.waitElePresents(BP.VIEWERSUBSCRIBE)
        self.driver.execute_script('mobile: scroll', {'element': subEle.get_attribute("name"),'toVisible':True})
        self.savePNG("SCROLLTO 关注")

    def clickScrollviewer(self):
        self.waitEleClick(BP.SCROLLVIEWER)


    def clickViewerList(self):
        self.waitEleClick(BP.TOLIST)

    def clickViewerShareTop(self):
        self.waitEleClick(BP.SHARE)

    def getBackRe(self):
        self.waitEleClick(BP.BACKRE)

    def subscribeA(self):
        ##点击 viwer下方【关注】
        self.waitEleClick("关注")


