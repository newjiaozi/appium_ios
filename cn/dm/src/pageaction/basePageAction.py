#coding=utf-8


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time,datetime
from cn.dm.src.pageobject.basePage import BasePage as BP
from cn.dm.src.interface import appGetHotWordNew
from  urllib.parse import quote

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


    def getChildEle(self,ele,loc):
        try:
            subele = ele.find_element(loc)
            return subele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False

    def getChildEleClick(self,ele,loc):
        try:
            # print(type(loc),loc)
            subele = ele.find_element(*loc)
            subele.click()
            return subele
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
            print(r'''<img src="%(src)s"  alt="%(filename)s"  title="%(filename)s" height="400" width="250" class="pimg"  onclick="javascript:window.open(this.src);"/>%(filename)s''' % {'filename':name,"src":src})

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
                    0 : ['周一','MONDAY'],
                    1 : ['周二','TUESDAY'],
                    2 : ['周三','WEDNESDAY'],
                    3 : ['周四','THURSDAY'],
                    4 : ['周五','FRIDAY'],
                    5 : ['周六','SATURDAY'],
                    6 : ['周日','SUNDAY'],
                    7 : ['完结','COMPLETE'],
                    }
        cur_time = datetime.datetime.now()
        day = cur_time.weekday()
        if all:
            week_day_dict[day][0]="今天"
            return week_day_dict.values()
        else:
            week_day_dict[day][0]="今天"
            return week_day_dict[day]


    def startAppCloseAlert(self):
        self.waitEleClick(BP.SYSALLOW,seconds=5)
        self.waitEleClick(BP.SYSCONFIRM,seconds=5)
        self.waitEleClick(BP.UPDATENEXT, seconds=10)
        ele = self.waitElePresents(BP.FIRSTCLOSE,seconds=5)
        if ele:
            self.tapXY(ele)
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
        self.driver.execute_script('mobile: scroll', {'element': topEle.get_attribute("name").e,'toVisible':True})
        self.savePNG("SCROLLTO TOP")

    def scroll2Subscribe(self):
        moon = self.waitElePresents(BP.MOONICON)
        self.waitStaleness(moon)
        # sv = self.waitElePresents(BP.SCROLLVIEWER)
        subEle = self.waitElePresents(BP.VIEWERSUBSCRIBE)
        self.driver.execute_script('mobile: scroll', {'element': subEle.get_attribute("name"),'toVisible':True})
        self.savePNG("SCROLLTO 关注")

    def scroll2Visible(self,ele):
        self.driver.execute_script('mobile: scroll', {'element': ele,'toVisible':True})

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

    def getXY(self,ele,center=True):
        location = ele.rect
        # print(location)
        if center:
            return location["x"]+location['width']/2,location['y']+location['height']/2
        else:
            return location

    def tapXY(self,ele):
        x,y = self.getXY(ele)
        self.driver.execute_script('mobile: tap', {'x':x,'y':y})

    ##确认viewer
    def checkViewer(self,titleName,episodeName):
        if self.waitElePresents((BP.IDTOBE[0],BP.IDTOBE[1] % episodeName)):
            self.savePNG(titleName+episodeName)
        else:
            self.waitEleClick(BP.SCROLLVIEWER)
            self.waitElePresents((BP.IDTOBE[0],BP.IDTOBE[1] % episodeName))
            self.savePNG(titleName+episodeName)
        # self.waitElePresents(BP.SCROLLVIEWER)
        top = self.waitElePresents(BP.VIEWERTOTOP)
        if top:
            self.scroll2Visible(top)
            self.savePNG("TOP"+titleName+episodeName)
    def clickViewer(self):
        self.waitEleClick(BP.SCROLLVIEWER)

    def ifHasNavigator(self):
        return self.waitElePresents(BP.MOONICON,seconds=2)

    def clickViewerList(self):
        self.waitEleClick(BP.TOLIST)

    def clickViewerTopShare(self):
        self.waitEleClick(BP.SHARE)

    def clickViewerBottomShare(self):
        self.waitEleClick(BP.VIEWERSHAREBUTTON)

    def clickViewerBottomLike(self):
        self.waitEleClick(BP.VIEWERLIKEBUTTON)

    def clickViewerBottomFavourite(self):
        self.waitEleClick(BP.VIEWERFAVOURITEBUTTON)

    def clickShangYiHua(self):
        self.waitEleClick(BP.SHANGYIHUA)

    def clickXiaYiHua(self):
        self.waitEleClick(BP.XIAYIHUA)

    def clickToTopViewer(self):
        self.waitEleClick(BP.VIEWERTOTOP)

    def clickToMoreComment(self):
        self.waitEleClick(BP.COMMENTMORE)

    def sendCommentInViewer(self,text):
        commentInput = self.waitEleClick(BP.INPUTCOMMENT)
        commentInput.send_keys(text)
        self.waitEleClick(BP.COMMENTSUBMIT)

    ##确认预览
    def checkPreview(self):
        pass

    ##确认最新话弹窗
    def checkPopup(self):
        pass

    def hideKeyboard(self):
        self.driver.hide_keyboard()

    ##小于1000展示赏我个赞吧！，>=100万展示为汉字万
    def handleLikeCount(self,count):
        if count<1000:
            return "赏我个赞吧！"
        elif count<1000000:
            return '{:,d}'.format(count)
        else:
            return '{:.1f}'.format(count/10000)+"万"

    def getHotWord(self):
        return appGetHotWordNew()

    def sleep(self,seconds=2):
        time.sleep(seconds)

    def getBackFromViewer(self):
        self.waitEleClick(BP.VIEWERBACK)

if __name__ == "__main__":
    bpa = BasePageAction(1)
    print(bpa.handleLikeCount(999))
    print(bpa.handleLikeCount(123123))
    print(bpa.handleLikeCount(2214523))