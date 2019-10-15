#coding=utf-8


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from cn.dm.src.pageobject.basePage import BasePage as BP
from selenium.common.exceptions import ElementNotVisibleException,WebDriverException
from cn.dm.src.interface import *
from appium.webdriver.common.touch_action import TouchAction
import os
import time,datetime
import random
from urllib import parse
from cn.dm.src.logger import logger
from cn.dm.src.interface import appEpisodeListV3,appFavoriteTotalRemoveAll,v1CommentOwnAllOnlyIds,deleteComment


class BasePageAction():

    def __init__(self,driver,defaultPage,data,saveData,cache,width,height,home,menus,menusDetail):
        self.driver = driver
        self.defaultPage = defaultPage
        self.data = data
        self.saveData = saveData
        self.cache = cache
        self.width = width
        self.height = height
        self.home = home
        self.menus = menus
        self.menusDetail = menusDetail


    def toDefaultPage(self, page="MY"):
        if not self.defaultPage:
            if page == "MY":
                self.getInMyPage()
            elif page == "MYTOON":
                self.getInMyToon()
                self.closeFirstMengCeng()
            elif page == "FOUND":
                self.getInFoundPage()
            elif page == "UPDATE":
                self.getInUpdatePage()
            self.defaultPage = True

    def waitElePresents(self,loc,seconds=10,poll_frequency=1):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            logger.info("waitElePresents元素存在 %s" % str(loc))
            return ele
        except TimeoutException:
            logger.error("执行waitElePresents异常,%s" % str(loc))
            return False

    def waitEleNotPresents(self,loc,seconds=2,poll_frequency=1):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            logger.error("waitEleNotPresents元素存在 %s" % str(loc))
            return False
        except TimeoutException:
            logger.info("waitEleNotPresents元素不存在 %s" % str(loc))
            return True

    def findSubElement(self,ele,loc):
        try:
            sub_ele = ele.find_element(*loc)
            logger.info("获取子元素成功%s" % str(loc))
            return sub_ele
        except Exception:
            logger.error("获取子元素失败%s" % str(loc))
            return False




    def eleExists(self,loc,seconds=10,poll_frequency=1):
        if self.waitElePresents(loc,seconds,poll_frequency):
            return True
        else:
            return False

    def eleVisiable(self,loc,seconds=10,poll_frequency=1):
        if self.waitEleVisiable(loc,seconds,poll_frequency):
            logger.info("eleVisiable元素可见 %s" % str(loc))
            return True
        else:
            logger.error("eleVisiable元素不可见 %s" % str(loc))
            return False


    def waitEleVisiable(self,loc,seconds=10,poll_frequency=1):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.visibility_of_element_located(loc))
            logger.info("waitEleVisiable元素可见,%s" % str(loc))
            return ele
        except TimeoutException:
            logger.error("waitEleVisiable元素不可见,%s" % str(loc))
            return False

    def waitElesPresents(self,loc,seconds=10,poll_frequency=1): ##返回所有elements
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_all_elements_located(loc))
            logger.info("waitElesPresents元素存在,%s" % str(loc))
            return ele
        except TimeoutException:
            logger.info("waitElesPresents元素不存在,%s" % str(loc))
            return False


    def getChildEle(self,fatherloc,loc):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(loc)))
        ele = self.waitElePresents(fatherloc)
        if ele:
            try:
                subele = self.findSubElement(ele,loc)
                logger.info("获取父级元素成功 %s,子元素成功 %s" % (str(fatherloc),str(loc)))
                return subele
            except TimeoutException:
                logger.error("获取子元素异常 %s" % str(loc))
                return False
        else:
            logger.error("获取父级元素失败 %s,子元素失败 %s" % (str(fatherloc),str(loc)))
            return False



    def getChildEleDisplay(self,fatherloc,loc):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(loc)))
        ele = self.waitElePresents(fatherloc)
        if ele:
            try:
                subele = ele.find_element(*loc)
                if subele.is_displayed():
                    logger.info("获取父级元素成功 %s,子元素可见 %s" % (str(fatherloc), str(loc)))
                    return True
                else:
                    logger.error("获取父级元素成功 %s,子元素不可见 %s" % (str(fatherloc), str(loc)))
                    return False
            except TimeoutException:
                logger.error("获取子元素异常 %s" % str(loc))
                return False
        else:
            logger.error("获取父级元素失败 %s,子元素失败 %s" % (str(fatherloc),str(loc)))
            return False


    def getChildElesDisplay(self,fatherloc,locs):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(locs)))
        ele = self.waitElePresents(fatherloc)
        if ele:
            try:
                locs_count = 0
                for loc in locs:
                    subele = self.findSubElement(ele,loc)
                    if subele.is_displayed():
                        logger.info("获取父级元素成功 %s,子元素可见 %s" % (str(fatherloc), str(loc)))
                        locs_count+=1
                    else:
                        logger.info("获取父级元素成功 %s,子元素不可见 %s" % (str(fatherloc), str(loc)))
                if locs_count == len(locs):
                    return True
                else:
                    return False
            except TimeoutException:
                logger.error("获取子元素异常")
                return False
        else:
            logger.error("获取父级元素失败 %s" % str(fatherloc))
            return False


    def clickChildEle(self,fatherloc,loc,seconds=5,poll_frequency=1):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(loc)))
        ele = self.waitElePresents(fatherloc,seconds,poll_frequency)
        if ele:
            if self.swipeUpUntilDisplayByEle(ele,loc,maxTimes=5):
                subele = self.findSubElement(ele,loc)
                if subele:
                    logger.info("获取父级元素成功,子元素可见,click子元素 %s" % str(loc))
                    subele.click()
                    return True
                else:
                    return False
            else:
                logger.error("获取父级元素成功,子元素不可见 %s" % str(loc))
                return False

        else:
            logger.error("获取父级元素失败 %s" % str(fatherloc))
            return False


    def checkChildElePresent(self,fatherloc,loc,maxTimes):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(loc)))
        ele = self.swipeUpUntilDisplayFast(fatherloc,maxTimes=maxTimes)
        if ele:
            if self.findSubElement(ele,loc):
                logger.info("获取父级元素成功,子元素找到 %s" % str(loc))
                return True
            else:
                logger.error("获取父级元素成功,子元素未找到 %s" % str(loc))
                return False
        else:
            logger.error("获取父级元素失败 %s" % str(fatherloc))
            return False


    def checkChildElesPresent(self,fatherloc,locs,maxTimes):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(locs)))
        if self.swipeUpUntilDisplayFast(fatherloc,maxTimes=maxTimes):
            ele = self.waitElePresents(fatherloc)
            count = 0
            for loc in locs:
                if self.findSubElement(ele,loc):
                    logger.info("获取父级元素成功,子元素找到 %s" % str(loc))
                    count+=1
                else:
                    logger.error("获取父级元素成功,子元素未找到 %s" % str(loc))
            if count == len(locs):
                return True
            else:
                return False
        else:
            logger.error("获取父级元素失败 %s" % str(fatherloc))
            return False



    def checkChildEleDisplay(self,fatherloc,loc,seconds=5,poll_frequency=1):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(loc)))
        try:
            ele = self.waitElePresents(fatherloc,seconds,poll_frequency)
            if ele:
                # subele = ele.find_element(*loc)
                # if subele.is_displayed():
                if self.swipeUpUntilDisplayByEle(ele,loc):
                    logger.info("获取父级元素成功,子元素可见 %s" % str(fatherloc))
                    return True
                else:
                    logger.error("获取父级元素成功,子元素不可见 %s" % str(fatherloc))
                    return False
            else:
                logger.error("获取父级元素失败 %s" % str(fatherloc))
                return False
        except TimeoutException:
            logger.error("获取子元素异常")
            return False


    def swipeUpUntilSubElesDisplay(self,fatherloc,locs,maxTimes=5,seconds=5,poll_frequency=1):
        logger.info("获取%s的子元素%s" % (str(fatherloc),str(locs)))
        if self.swipeUpUntilDisplayFast(fatherloc):
            ele = self.waitElePresents(fatherloc, seconds, poll_frequency)
            locs_count = 0
            for loc in locs:
                logger.info("等待元素可见：%s" % str(loc))
                if self.swipeUpUntilDisplayByEle(ele,loc,maxTimes=maxTimes):
                    logger.info("获取父级元素成功%s,子元素可见 %s" % (str(fatherloc),str(loc)))
                    locs_count+=1
                else:
                    logger.error("获取父级元素成功%s,子元素不可见 %s" % (str(fatherloc),str(loc)))
                    return False
            if locs_count == len(locs):
                logger.info("checkChildElesDisplay成功")
                return True
            else:
                logger.error("checkChildElesDisplay失败")
                return False
        else:
            logger.error("获取父级元素失败 %s" % str(fatherloc))
            return False


    def waitEleClick(self,loc,seconds=10,poll_frequency=1):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.element_to_be_clickable(loc))
            ele.click()
            # self.tapXY(ele)
            logger.info("执行waitEleClick成功,%s" % str(loc))
            return True
        except TimeoutException:
            logger.error("waitEleClick执行TimeoutException,%s" % str(loc))
            return False


    def switchPage(self,loc,seconds=10,poll_frequency=1):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            if ele.is_selected():
                return ele
            else:
                ele.click()
                return ele
        except TimeoutException as e:
            # print(e)
            # print(loc)
            return False


    def savePNG(self,*args):
        args_list = []
        for i in args:
            if not isinstance(i,str):
                i = str(i)
            args_list.append(i)
        name = "_".join(args_list)
        _name = os.path.abspath(os.path.join(os.path.curdir,"results","screenshots", name+".png"))
        self.driver.get_screenshot_as_file(_name)
        src = "screenshots\%s" % name+".png"
        print(r'''<br>''')
        print(r'''<img src="%(src)s"  alt="%(filename)s"  title="%(filename)s" height="%(height)s" width="%(width)s" class="pimg"  onclick="javascript:window.open(this.src);"/>%(filename)s''' % {'filename':name,"src":src,"height":self.height/2,"width":self.width/2})
        print(r'''<br>''')

    def waitStaleness(self,ele,seconds=5,poll_frequency=1):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.staleness_of(ele))
            logger.info("等待%s消失" % str(ele))
            return True
        except TimeoutException:
            logger.error("等待%s消失_失败" % str(ele))
            logger.exception("waitStaleness异常")
            return False

    ## 开屏跳过
    def passJump(self,seconds=30,poll_frequency=1):
        _jump = self.waitPresents(BP.JUMP,seconds=seconds,poll_frequency=poll_frequency)
        if _jump:
            self.savePNG("跳过出现")
            self.waitStaleness(_jump)
            self.savePNG("跳过消失")
        return True

    ## 检查开屏splash
    def checkSplash(self,bachInit,seconds=20,poll_frequency=1):
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
    def getWeekday(self,all=False,whichDay=0):
        week_day_dict = {
                    1 : ['周一','MONDAY'],
                    2 : ['周二','TUESDAY'],
                    3 : ['周三','WEDNESDAY'],
                    4 : ['周四','THURSDAY'],
                    5 : ['周五','FRIDAY'],
                    6 : ['周六','SATURDAY'],
                    7 : ['周日','SUNDAY'],
                    8 : ['完结','COMPLETE'],
                    }
        cur_time = datetime.datetime.now()
        day = cur_time.weekday()
        week_day_dict[day+1][0] = "今天"
        if whichDay:
            result =  week_day_dict[whichDay]
        elif all:
            result = week_day_dict.values()
        else:
            result = week_day_dict[day]
        logger.info(result)
        return result

    def handleUserPreference(self):
        if self.waitEleVisiable(BP.USERPREFENRENCEGENDERTITLE):

            ele1 = self.waitElePresents(self.getRandomGender())
            self.tapXY(ele1)
            if self.waitEleVisiable(BP.USERPREFENRENCEAGETITLE):
                ele2 = self.waitElePresents(self.getRandomAge())
                self.tapXY(ele2)
                if self.waitEleVisiable(BP.USERPREFENRENCEGENRETITLE):
                    jump,genre = self.getRandomGenre()
                    for i in genre:
                        ele = self.waitElePresents(i)
                        if ele:
                            self.tapXY(ele)
                        else:
                            jump = 1
                            break
                    if jump == 1:
                        ele = self.waitElePresents(BP.USERPREFENRENCEJUMP)
                        self.tapXY(ele)
                    else:
                        self.waitEleClick(BP.USERPREFENRENCEGENRECONFIRM)
                    ele4 = self.waitElePresents(BP.USERPREFENRENCERECOMMENDTODISCOVERY)
                    self.tapXY(ele4)
                    return True
        return False

    def handlePrivacy(self):
        if self.waitEleVisiable(BP.PRIVACYTITLE):
            # self.savePNG("隐私条款页")
            self.waitEleClick(BP.PRIVACYAGREE)
            return True
        else:
            return False


    def startAppCloseAlert(self,env):
        self.waitEleClick(BP.SYSALLOW,seconds=1)
        if env != "real":
            self.waitEleClick(BP.SYSCONFIRM,seconds=1)
        self.handlePrivacy()
        self.handleUserPreference()
        versionUpdate = appClientVersion()
        if versionUpdate:
            self.waitEleClick(BP.UPDATENEXT, seconds=1)
        ele = self.waitElePresents(BP.FIRSTCLOSE,seconds=1)
        if ele:
            self.tapXY(ele)

    def waitTextInPage(self,text,seconds=10,poll_frequency=1):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(lambda x:text in x.page_source)
            logger.info("【%s】在pageSource中" % text)
            return True
        except TimeoutException:
            logger.error("【%s】不在pageSource中" % text)
            return False

    def pickerWheel(self,element):
        self.driver.execute_script('mobile: selectPickerWheelValue', {'order': 'next', 'offset': 0.15, 'element': element});


    ##处理单章节点赞
    def handleEpisodeLikeCount(self,count):
        if count<1000:
            result =  str(count)
        elif count<100000:
            result =  '{:,d}'.format(count)
        else:
            result = '99,999+'
        logger.info("传入：%s,返回：%s" % (count,result))
        return result



    ##小于1000展示赏我个赞吧！，>=100万展示为汉字万
    def handleTitleLikeCount(self,count):
        if count<1000:
            result =  "赏我个赞吧！"
        elif count<1000000:
            result =  '{:,d}'.format(count)
        elif count<100000000:
            result = '{:.1f}'.format(count/10000)+"万"
            if result.endswith(".0万"):
                result = result.replace(".0万","万")
        else:
            result ='{:.1f}'.format(count/100000000)+"亿"
            if result.endswith(".0亿"):
                result = result.replace(".0亿","亿")
        logger.info(result)
        return result
    def getBack(self):
        logger.info("点击【返回 or <--】")
        return self.waitEleClick(BP.BTNBACK)


    def getInMyPage(self,):
        mybtn = self.waitElePresents(BP.MY)
        logger.info("进入【我的】页面")
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
        logger.info("进入【我的漫画】页")
        mybtn = self.waitElePresents(BP.MYCARTOON)
        mybtn.click()




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
        logger.info("进入【更新】页")
        # mybtn = self.waitElePresents(BP.UPDATE)
        # mybtn.click()
        return self.waitEleClick(BP.UPDATE)



    def swipeUp(self):
        self.driver.execute_script("mobile: swipe", {"direction": "up"})

    def swipeDown(self):
        self.driver.execute_script("mobile: swipe", {"direction": "down"})
        logger.info("swipeDown")
        # self.scrollSlow(self.width/2,self.height/4,self.width/2,self.height/2,"swipeDown")


    def swipeLeft(self):
        self.driver.execute_script("mobile: swipe", {"direction": "left"})
        logger.info("swipeLeft")
        # self.scrollSlow(self.width,self.height/2,0,self.height/2,"swipeLeft")

    def swipeLeftA(self):
        self.drag(500,self.width*3/4,self.height/2,0,self.height/2)
        logger.info("swipeLeftA")

    def swipeLeftB(self):
        self.scrollSlow(self.width*3/4,self.height/2,0,self.height/2,500,who="swipeLeftB")
        logger.info("swipeLeftB")


    def swipeRight(self):
        self.driver.execute_script("mobile: swipe", {"direction": "right"})

    def scrollUp(self):
        self.driver.execute_script("mobile: scroll", {"direction": "up"})

    def scrollDown(self):
        self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def scrollDownEle(self,ele):
        self.driver.execute_script("mobile: scroll", {"direction": "down","element":ele})

    def scrollLeft(self):
        self.driver.execute_script("mobile: scroll", {"direction": "left"})

    def scrollRight(self):
        self.driver.execute_script("mobile: scroll", {"direction": "right"})


    def drag(self,duration,fromX,fromY,toX,toY):
        self.driver.execute_script("mobile: dragFromToForDuration", {"duration": duration,"fromX": fromX,"fromY": fromY,"toX": toX,"toY": toY})

    def tapElement(self,element):
        # actions = TouchAction(self.driver)
        # actions.tap(element)
        # actions.perform()
        self.driver.execute_script('mobile: tap', {'element': element.get_attribute("name"),'x':0.1,'y':0.1});

    def terminalAPP(self,name="QQ"):
        lowername = name.lower()
        if lowername == "qq":
            logger.info("【激活QQ】")
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.tencent.mqq'})
            logger.info("【结束进程-QQ】")
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.tencent.mqq'})
            logger.info("【激活咚漫】")
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.naver.linewebtoon.cn'})

        elif lowername == "weibo":
            logger.info("【激活微博】")
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.sina.weibo'})
            logger.info("【结束进程-微博】")
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.sina.weibo'})
            logger.info("【激活咚漫】")
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.naver.linewebtoon.cn'})

        elif lowername == "wechat":
            logger.info("【激活微信】")
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.tencent.xin'})
            logger.info("【结束进程-微信】")
            self.driver.execute_script('mobile: terminateApp',{'bundleId':'com.tencent.xin'})
            logger.info("【激活咚漫】")
            self.driver.execute_script('mobile: activateApp',{'bundleId':'com.naver.linewebtoon.cn'})

        else:
            logger.info("【结束进程-咚漫】")
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


    def Scroll2Share(self):
        moon = self.waitElePresents(BP.MOONICON)
        self.waitStaleness(moon)
        # sv = self.waitElePresents(BP.SCROLLVIEWER)
        topEle = self.waitElePresents(BP.TOTOP)
        self.driver.execute_script('mobile: scroll', {'element': topEle.get_attribute("name").e,'toVisible':True})
        self.savePNG("SCROLLTO TOP")



    def scroll2VisibleById(self,id):
        self.driver.execute_script('mobile: scroll', {'name': id,'toVisible':True})

    def clickScrollviewer(self):
        self.waitEleClick(BP.SCROLLVIEWER)

    def clickViewerList(self):
        self.waitEleClick(BP.TOLIST)

    def clickViewerShareTop(self):
        self.waitEleClick(BP.SHARE)

    def getBackRe(self):
        self.waitEleClick(BP.BACKRE)

    def getBackBTS(self):
        logger.info("getBackBTS，返回")
        return self.waitEleClick(BP.BACK)


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
        logger.info("tapXY元素：%s" % str(ele.text))
        self.driver.execute_script('mobile: tap', {'x':x,'y':y})

    def tapByXY(self,x,y):
        # logger.info("tapByXY: %s,%s" % (x,y))
        self.driver.execute_script('mobile: tap', {'x':x,'y':y})

    def getScreenSize(self):
        return self.driver.get_window_size()

    def clickViewer(self):
        self.waitEleClick(BP.SCROLLVIEWER)

    def ifHasNavigator(self):
        return self.waitElePresents(BP.MOONICON,seconds=2)

    def navigatorOn(self,times=0,waitTime=5,loading=False):
        logger.info("navigatorOn等待导航栏出现")
        if loading:
            ele = self.waitEleVisiable(BP.LOADINGTEXT,seconds=1)
            if ele:
                self.waitStaleness(ele,seconds=10)
        if waitTime:
            self.sleep(waitTime)
        if times >3:
            return False
        try:
            if self.waitEleVisiable(BP.MOONICON,seconds=1):
                return True
            else:
                self.tapByXY(self.width / 2, self.height / 2)
                return self.navigatorOn(times)
        except ElementNotVisibleException:
            times += 1
            self.tapByXY(self.width / 2, self.height / 2)
            return self.navigatorOn(times)

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
        inputComment = self.waitElePresents(BP.INPUTCOMMENT)
        if inputComment:
            inputComment.click()
            inputComment.send_keys(text)
            ele = self.waitElePresents(BP.COMMENTSUBMIT)
            if ele:
                self.tapXY(ele)
            else:
                return ele
        return False

    def hideKeyboard(self):
        self.driver.hide_keyboard()


    def getHotWord(self):
        return appGetHotWordNew()

    def sleep(self,seconds=2):
        time.sleep(seconds)

    def getBackFromViewer(self,times=0):
        logger.info("执行getBackFromViewer")
        # if times >=3:
        #     return False
        # try:
        #     if self.waitEleClick(BP.VIEWERBACK,seconds=2):
        #         pass
        #     else:
        #         self.tapByXY(self.width / 2, self.height / 2)
        #         return self.getBackFromViewer(times)
        # except ElementNotVisibleException:
        #     times += 1
        #     self.tapByXY(self.width / 2, self.height / 2)
        #     return self.getBackFromViewer(times)
        return self.getBackFromViewerByTapXY()

    def getBackFromViewerByTapXY(self):
        logger.info("getBackFromViewerByTapXY")
        # self.tapByXY(self.width / 2, self.height / 2)
        if self.navigatorOn():
            return self.waitEleClick(BP.VIEWERBACK, seconds=2)
        else:
            logger.error("getBackFromViewerByTapXY失败")
            return False

    def getBackFromCutViewer(self):
        logger.info("getBackFromCutViewer")
        if self.swipeLeftUntilDispaly(BP.VIEWERBACK):
            return self.waitEleClick(BP.VIEWERBACK, seconds=2)
        else:
            logger.error("getBackFromCutViewer失败")
            return False

    def swipeLeftUntilDispaly(self,loc,times=0):
        if times>50:
            return False
        ele = self.waitEleVisiable(loc)
        if ele:
            return ele
        else:
            self.swipeLeft()
            return self.swipeLeftUntilDispaly(loc,times)

    def getBackFromViewerByViewerType(self,viewerType="CUT"):
        if viewerType == "CUT":
            return self.getBackFromCutViewer()
        else:
            return self.getBackFromViewerByTapXY()

    def getBackBTV(self):
        return self.waitEleClick(BP.VIEWERBACK)

    def getBackFromList(self):
        logger.info("从列表返回，getBackFromList")
        return self.waitEleClick(BP.LISTBACK,seconds=2)

    def closePreivewOrPopupDisplay(self):
        self.tapByXY(self.width/2,self.height/2)
        return self.waitEleClick(BP.PREVIEWCLOSE,seconds=2)

    def scrollDownDisplay(self,ele):
        if ele.is_displayed():
            pass
        else:
            self.scrollDown()
            if ele.is_displayed():
                pass
            elif self.bottomPopup():
                self.closeBottomPopup()
            self.scrollDownDisplay(ele)

    def swipeUpDisplay(self,ele):
        if ele.is_displayed():
            return True
        else:
            self.swipeUp()
            return self.swipeUpDisplay(ele)


    def swipeUpUntilSubEleDisplay(self,fatherloc,loc,startTimes=0,maxTimes=50):
        if startTimes >= maxTimes:
            return False
        if self.checkChildEleDisplay(fatherloc,loc,seconds=1):
            return True
        else:
            startTimes+=1
            self.swipe1per5Screen()
            return self.swipeUpUntilSubEleDisplay(fatherloc,loc,startTimes,maxTimes)


    def swipeUpUntilDisplay(self,loc,startTimes=0,maxTimes=50):
        if startTimes >= maxTimes:
            logger.info("尝试次数：%s，退出尝试" % maxTimes)
            return False
        if self.waitEleVisiable(loc,seconds=1):
            logger.info("元素可见：%s" % str(loc))
            return True
        else:
            startTimes+=1
            logger.info("元素%s第%s次不可见" % (str(loc),startTimes))
            self.swipe1per5Screen(str(loc))
            return self.swipeUpUntilDisplay(loc,startTimes,maxTimes)


    def swipeUpUntilDisplayFast(self,loc,startTimes=0,maxTimes=50):
        if startTimes >= maxTimes:
            logger.info("尝试次数：%s，退出尝试" % maxTimes)
            return False
        if self.waitEleVisiable(loc,seconds=1):
            logger.info("元素可见：%s" % str(loc))
            return True
        else:
            startTimes+=1
            logger.info("元素%s第%s次不可见" % (str(loc),startTimes))
            self.swipeHalfScreen(str(loc))
            return self.swipeUpUntilDisplayFast(loc,startTimes,maxTimes)


    def swipeUpUntilDisplayByEle(self,ele,loc,startTimes=0,maxTimes=50):
        subele = self.findSubElement(ele,loc)
        if subele:
            if startTimes >= maxTimes:
                logger.info("尝试次数：%s，退出尝试" % maxTimes)
                return False
            if subele.is_displayed():
                logger.info("元素可见：%s" % str(loc))
                return True
            else:
                startTimes+=1
                logger.info("元素%s第%s次不可见" % (str(loc),startTimes))
                self.swipe1per5Screen(str(ele.text))
                return self.swipeUpUntilDisplayByEle(ele,loc,startTimes,maxTimes)
        else:
            return False



    def swipeLeftByEleLocation(self,loc,ele,startTimes=0,maxTimes=50):
        if startTimes >= maxTimes:
            logger.info("元素不可见，超过了尝试最大次数%s" % maxTimes)
            return False
        if self.waitEleVisiable(loc,seconds=1):
            logger.info("元素可见：%s" % str(loc))
            return True
        else:
            startTimes+=1
            logger.info("元素不可见，尝试第%s次" % startTimes)
            location = self.getXY(ele)
            self.scrollSlow(location[0]+100,location[1],0,location[1],who="swipeLeftByEleLocation")
            return self.swipeLeftByEleLocation(loc,ele,startTimes,maxTimes)



    def swipeLeftByFatherLoc(self,ele,loc,startTimes=0,maxTimes=50):
        subele = self.findSubElement(ele,loc)
        if subele:
            if startTimes >= maxTimes:
                logger.info("尝试次数：%s，退出尝试" % maxTimes)
                return False
            if subele.is_displayed():
                logger.info("元素可见：%s" % str(loc))
                return True
            else:
                startTimes+=1
                logger.info("元素%s第%s次不可见" % (str(loc),startTimes))
                location = self.getXY(ele)
                self.scrollSlow(location[0] + 100, location[1], 0, location[1], who="swipeLeftByFatherLoc")
                return self.swipeLeftByFatherLoc(ele,loc,startTimes,maxTimes)
        else:
            return False





    def swipeUpUntilDisplayHalf(self,loc,startTimes=0,maxTimes=50):
        if startTimes >= maxTimes:
            logger.error("执行swipeUpUntilDisplayHalf次数超过%s次 %s" % (maxTimes,str(loc)))
            return False
        if self.waitEleVisiable(loc,seconds=1):
            logger.info("执行swipeUpUntilDisplayHalf元素可见 %s" % str(loc))
            return True
        else:
            startTimes += 1
            self.swipeHalfScreen(str(loc))
            return self.swipeUpUntilDisplayHalf(loc,startTimes,maxTimes)



    # def swipeLeftDisplay(self,ele):
    #     if ele.is_displayed():
    #         return True
    #     else:
    #         self.swipeLeft()
    #         return self.swipeLeftDisplay(ele)


    def scrollSlow(self,fromX,fromY,toX,toY,duration=1000,who="who"):
        logger.info("执行scrollSlow:%s" % who)
        actions = TouchAction(self.driver)
        return actions.press(x=fromX, y=fromY).wait(duration).move_to(x=toX, y=toY).release().perform()

    def swipeHalfScreen(self,who="who"):
        logger.info("swipeHalfScreen执行")
        self.scrollSlow(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4,who=who)

    def swipe1per5Screen(self,who="who"):
        self.scrollSlow(self.width / 2, self.height * 3 / 5, self.width / 2, self.height*2/ 5,who=who)


    def swipe2per5Screen(self,who="who"):
        self.scrollSlow(self.width / 2, self.height * 4 / 5, self.width / 2, self.height*2/ 5,who=who)


    def swipeLeftOneScreen(self):
        self.scrollSlow(self.width*9/10, self.height/4, self.width /10, self.height/4)


    def swipe2Per3Screen(self,who):
        self.scrollSlow(self.width / 2, self.height * 5 / 6, self.width / 2, self.height / 6,who=who)

    def swipeOneScreen(self,who):
        self.scrollSlow(self.width / 2, self.height * 9 / 10, self.width / 2, self.height / 10,500,who=who)

    def bottomPopup(self):
        return self.waitElePresents(BP.ALERTPOPUPDISPLAY,seconds=2)

    def closeBottomPopup(self):
        self.waitEleClick(BP.ALERTPOPUPCLOSE)

    def checkDefaultSearchUI(self,hotwordcount=3,pagefrom="发现页"):
        result = appGetHotWordNew()
        if result:
            hotwordresult = 0
            for i in range(0,hotwordcount):
                if self.waitElePresents((BP.IDTOBE[0],BP.IDTOBE[1] % result[i]["hotWord"])):
                    hotwordresult += 1
            if hotwordresult == hotwordcount:
                return self.waitEleClick(BP.SEARCHCANCEL)
            else:
                self.savePNG("搜索页")
                self.waitEleClick(BP.SEARCHCANCEL)
                return False
        else:
            return False

    def checkSearchGenreUI(self):
        codeName = appGenrelist2()
        for k,v in codeName.items():
            if self.waitElePresents((BP.IDTOBE[0],BP.IDTOBE[1] % v)):
                pass
            else:
                return False
        return True

    def checkGenreUI(self):
        genres = appGenrelist2(False).values()
        res_count = 0
        for genre in genres:
            res = self.waitElePresents((BP.IDTOBE[0],BP.IDTOBE[1] % genre))
            if res:
                res_count+=1
        res_count_bool = False
        if res_count == len(genres):
            res_count_bool = True
        return res_count_bool


    def clickHotWord(self):
        hotword = appGetHotWordNew()
        for i in range(0,3):
            self.waitEleClick((BP.IDTOBE[0],BP.IDTOBE[1] % hotword[i]["hotWord"]))
            titleNo = hotword[i]["titleNo"]
            linkType = hotword[i]["linkType"]
            print(type(titleNo),type(linkType))
            if linkType == "1":    ##1是列表
                pass
            elif linkType == "2":   ##2是viewer记录或者第一话
                pass

    def clickSearchGenre(self):
        genre =  appGenrelist2()
        for i in genre:
            self.waitEleClick((BP.IDTOBE[0],BP.IDTOBE[1] % i))


    def clickIntroduce(self):
        self.waitEleClick(BP.PRODUCTIONINTRO)

    def clickSelectList(self):
        self.waitEleClick(BP.SELECTEPISODE)


    ##### 需要几个通用的viewer和list，简介，预览，底部弹窗的方法（区分viewer类型）
    def checkTitleList(self,titleNo,randomCount=1):
        if self.checkTitleTopBottomViewer(titleNo):
            title = self.getTitleFromList2(titleNo)
            episode_list = appEpisodeListV3(titleNo)
            # hide_episode = appEpisodeListHide(titleNo)
            if episode_list:
                freeepisode = episode_list["episode"]
                episode_list_filter = list(filter(lambda x: x["serviceStatus"] == "SERVICE", freeepisode))
                viewerType = title["viewer"]
                return self.checkTitleListData(episode_list_filter,viewerType,randomCount,maxTimes=100)
            else:
                return False
        else:
            return False



    def checkTitleListData(self, data,viewerType, randomCount=1,maxTimes = 10):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length,reverse=True)
        else:
            randomData = self.getRandomInts(data_length, randomCount,reverse=True)
        count = 0
        for i in range(0,data_length):
            episodeSeq = data[i]["episodeSeq"]
            if episodeSeq in randomData:
                if viewerType == "ACTIVITYAREA":
                    if self.checkChildElePresent((BP.LISTEPISODECELL[0], BP.LISTEPISODECELL[1] % episodeSeq),
                                                     (BP.IDTOBE[0], BP.IDTOBE[1] % data[i]["episodeTitle"]), maxTimes = maxTimes):

                        if self.waitEleClick((BP.LISTEPISODECELL[0], BP.LISTEPISODECELL[1] % episodeSeq)):
                            if self.checkViewer(data[i]["titleNo"],episodeNo=data[i]["episodeNo"],history=False):
                                count +=1

                else:
                    seqText = "#%s" % data[i]["episodeSeq"]
                    if self.checkChildElesPresent((BP.LISTEPISODECELL[0], BP.LISTEPISODECELL[1] % episodeSeq),
                                                      [(BP.IDTOBE[0], BP.IDTOBE[1] % data[i]["episodeTitle"]),
                                                       (BP.IDTOBE[0], BP.IDTOBE[1] % seqText)], maxTimes=maxTimes):
                        if self.waitEleClick((BP.LISTEPISODECELL[0], BP.LISTEPISODECELL[1] % episodeSeq)):
                            if self.checkViewer(data[i]["titleNo"],episodeNo=data[i]["episodeNo"],history=False):
                                count +=1


        if count == len(randomData):
            return self.getBackFromList()
        else:
            self.getBackFromList()
            return False

    def checkTitleIntroduce(self,titleNo):
        title = self.getTitleFromList2(titleNo)
        titleInfo = appTitleInfo2(titleNo)
        authorInfo = appAuthorInfo2(titleNo)
        authorInfoList = [i["authorName"] for i in authorInfo]
        author = "/".join(authorInfoList)
        authorName = "作者：%s" % author
        synopsis = titleInfo["synopsis"]
        res1 = self.eleVisiable((BP.IDTOBE[0], BP.IDTOBE[1] % authorName))
        res2 = self.eleVisiable((BP.IDTOBE[0], BP.IDTOBE[1] % synopsis))
        res4 = self.checkTitleTopBottomViewer(titleNo)
        if title["viewer"] == "ACTIVITYAREA":
            res3 = self.eleVisiable(BP.ASSOCIATIONANNOUNCEMENT)
            self.getBackFromList()
            return res1 and res2 and res3 and res4
        else:
            res3 = self.eleVisiable(BP.INTRODUCTION)
            self.getBackFromList()
            return res1 and res2 and res3 and res4

    def checkTitleTopBottomViewer(self,titleNo):
        title = self.getTitleFromList2(titleNo)
        res1 = self.eleVisiable((BP.IDTOBE[0], BP.IDTOBE[1] % title["title"]))
        res2 = self.eleVisiable(BP.SHARE)
        titleInfo = appTitleInfo2(titleNo)
        if titleInfo:
            if self.checkCache(titleNo):
                bottomEpisode = titleInfo["firstEpisodeTitle"]
                bottomName = "开始阅读"
            else:
                # episodeInfo = appEpisodeInfoV3(titleNo,self.cache[titleNo][1])
                episodeInfo = appEpisodeInfoV3(titleNo,self.getCache(titleNo)[1])
                bottomEpisode = episodeInfo["episodeTitle"]
                bottomName = "继续阅读"
            res3 = self.getChildEleDisplay((BP.LISTBOTTOMID[0], BP.LISTBOTTOMID[1]),(BP.IDTOBE[0],BP.IDTOBE[1] % bottomEpisode))
            res4 = self.getChildEleDisplay((BP.LISTBOTTOMID[0], BP.LISTBOTTOMID[1]),(BP.IDTOBE[0],BP.IDTOBE[1] % bottomName))
            self.savePNG(title["title"],"列表")
            if title["viewer"] == "ACTIVITYAREA":
                res5 = self.eleVisiable(BP.ACTIVITYZONE)
                self.savePNG(title["title"],"活动专区")
                return res1 and res2 and res3 and res4 and res5
            else:
                if self.waitElePresents(BP.ADDSCORE):
                    res5= True
                else:
                    res5= False
                # self.savePNG(title["title"],"评分")
                return res1 and res2 and res3 and res4 and res5
        else:
            return False


    def getTitleFromList2(self,titleNo=""):
        if titleNo:
            try:
                titleNo = int(titleNo)
                title= self.data[titleNo]
                logger.info("getTitleFromList2获取的作品为：%s" % title["title"])
                return title
            except KeyError:
                logger.info("getTitleFromList2获取作品失败，titleNo：%s" % titleNo)
                return False
        else:
            logger.info("getTitleFromList2获取作品所有titleNo")
            return list(self.data.keys())

    def checkCache(self,titleNo):
        titleNo = int(titleNo)
        return titleNo in self.cache

    def addCache(self,titleNo,title,episodeNo,episodeSeq):
        ttime = time.mktime(datetime.datetime.now().timetuple())
        titleNo = int(titleNo)
        self.cache[titleNo]=[title,episodeNo,episodeSeq,ttime]
        logger.info("添加阅读记录addCache,%s" % titleNo)
        logger.info(self.cache.keys())

    def getCache(self,keyTitleNo=""):
        if keyTitleNo:
            keyTitleNo = int(keyTitleNo)
            return self.cache.get(keyTitleNo,None)
        else:
            cache_list = sorted(self.cache.items(),key=lambda x:x[1][3],reverse=True)
            cache_dict = dict(cache_list)
            logger.info("getCache获取到的历史记录：")
            logger.info(cache_dict.keys())
            return cache_dict


    #条漫
    def checkScrollViewer(self,titleNo,episodeNo):
        shareText = self.waitElePresents(BP.VIEWERSHAREBUTTONTEXT)
        title = self.getTitleFromList2(titleNo)
        if shareText:
            self.savePNG(title["title"],episodeNo)
            episodeInfo = appEpisodeInfoV3(titleNo, episodeNo)
            if episodeInfo:
                logger.info("tapByImageInfos:%s_%s_%s" % (title["title"], titleNo, episodeInfo["episodeNo"]))
                self.addCache(titleNo,title,episodeInfo["episodeNo"],episodeInfo["episodeSeq"])
                # imageInfos = episodeInfo["imageInfo"]
                self.tapByImageInfos(titleNo,episodeNo,episodeInfo)
                logger.info("checkScrollViewer成功")
                return self.getBackFromViewerByTapXY()
            else:
                logger.info("checkScrollViewer失败")
                self.noNetClose(title["title"],episodeNo)
                return False
        else:
            if self.noNetClose(title["title"], episodeNo):
                return True
            else:
                return self.getBackFromViewerByTapXY()

    def scrolByImageHeight(self,titleNo,episodeNo):
        title = self.getTitleFromList2(titleNo)
        episodeInfo = appEpisodeInfoV3(titleNo, episodeNo)
        imageInfos = episodeInfo["imageInfo"]
        screenSize = self.getScreenSize()
        width = screenSize["width"]
        height = screenSize["height"]
        imageCount,imageHeight = self.getImageHeight(imageInfos,width)
        scrollTimes = int(imageHeight//(height/2))
        print(width,height,imageCount,imageHeight,scrollTimes)
        for i in range(0,scrollTimes):
            self.scrollSlow(width/2,3*height/4,width/2,height/4,1680)
        self.savePNG(title["title"],episodeInfo["episodeTitle"],"末尾")
        return True

    ## 通过点击观看漫画
    def tapByImageHeight(self,titleNo,episodeNo):
        title = self.getTitleFromList2(titleNo)
        episodeInfo = appEpisodeInfoV3(titleNo, episodeNo)
        if episodeInfo:
            imageInfos = episodeInfo["imageInfo"]
            imageCount,imageHeight = self.getImageHeight(imageInfos,self.width)
            scaleTimes = (imageHeight-self.height)/(2*self.height/3)
            scrollTimes = int(scaleTimes)
            floatTimes =  scaleTimes-scrollTimes
            # print(width,height,imageCount,imageHeight,scrollTimes)
            x,y = self.width/2,3*self.height/4
            for i in range(0,scrollTimes):
                self.tapByXY(x,y)
                self.sleep(0.2)
            self.scrollSlow(self.width/6,floatTimes*(2*self.height/3),self.width/6,0,1800)
            self.scrollSlow(self.width/6,self.height/8,self.width/6,0,1800)
            self.savePNG(title["title"],episodeInfo["episodeTitle"],"末尾")
            return True
        else:
            if self.noNetClose(title["title"], episodeNo):
                return True
            else:
                return self.getBackFromViewerByTapXY()

    def tapByImageInfos(self,titleNo,episodeNo,episodeInfo):
        # slow_times = 0 ##两次点击之前的时间特别慢，达到5次，就不tap了?
        title = self.getTitleFromList2(titleNo)
        imageInfos = episodeInfo["imageInfo"]
        logger.info("viewer阅读页_tapByImageInfos:%s_%s_%s_%s_开始" % (title["title"],titleNo,episodeInfo["episodeTitle"],episodeNo))
        imageCount,imageHeight = self.getImageHeight(imageInfos,self.width)
        scaleTimes = (imageHeight-self.height)/(2*self.height/3)
        scrollTimes = int(scaleTimes)
        logger.info("tapByImageInfos应该滚动%s次" % scrollTimes)
        floatTimes =  scaleTimes-scrollTimes
        if self.tapReadTitle(scrollTimes):
            self.scrollSlow(self.width/6,floatTimes*(2*self.height/3),self.width/6,0,1800,who="tapByImageInfos_按照计算次数滚动")
            self.scrollSlow(self.width/6,self.height/8,self.width/6,0,1800,who="tapByImageInfos_滚动1/8屏幕")
            self.savePNG(title["title"],episodeNo,"末尾")
            logger.info("viewer阅读页_tapByImageInfos:%s_%s_%s_%s_结束" % (title["title"],titleNo,episodeInfo["episodeTitle"],episodeNo))
            return True
        else:
            self.savePNG(title["title"],episodeNo,"中断")
            logger.info("viewer阅读页_tapByImageInfos:%s_%s_%s_%s_中断" % (title["title"],titleNo,episodeInfo["episodeTitle"],episodeNo))
            return True


    def tapByImageHeightPreview(self,titleNo,episodeNo,loc):
        title = self.getTitleFromList2(titleNo)
        episodeInfo = appEpisodeInfoV3(titleNo, episodeNo)
        if episodeInfo:
            imageInfos = episodeInfo["imageInfo"]
            imageCount,imageHeight = self.getImageHeight(imageInfos,self.width)
            scaleTimes = (imageHeight-self.height)/(2*self.height/3)
            scrollTimes = int(scaleTimes)
            floatTimes =  scaleTimes-scrollTimes
            logger.info("预览阅读页_tapByImageHeightPreview:%s_%s_%s_开始" % (title["title"],titleNo,episodeInfo["episodeTitle"]))
            logger.info("应该TAP %s次" % scrollTimes)
            if self.tapReadTitle(scrollTimes,plusTimes=2):
                self.scrollSlow(self.width/6,floatTimes*(2*self.height/3),self.width/6,0,1800,who="tapByImageHeightPreview")
                if self.swipeUpUntilDisplay(loc):
                    self.savePNG(title["title"], episodeNo, "结束","预览阅读页")
                    logger.info("预览阅读页_tapByImageHeightPreview:%s_%s_%s_结束" % (title["title"], titleNo, episodeInfo["episodeTitle"]))
                    return True
                else:
                    return False
            else:
                self.savePNG(title["title"], episodeNo, "中断","预览阅读页")
                logger.info("预览阅读页_tapByImageHeightPreview:%s_%s_%s_中断" % (title["title"], titleNo, episodeInfo["episodeTitle"]))
                return True

        else:
            logger.error("tapByImageHeightPreview失败")
            if self.noNetClose(title["title"], episodeNo):
                return True
            else:
                return self.closePreivewOrPopupDisplay()

    def getImageHeight(self,imageInfo,width):
        # screenSize = self.getScreenSize()
        # width = screenSize["width"]
        # height = screenSize["height"]
        # logger.info("执行getImageHeight")
        sum = 0
        for i in imageInfo:
            scaleHeight = (i["height"]/i["width"])*width
            sum += scaleHeight
        return len(imageInfo),sum


    ##页漫
    def checkCutViewer(self,titleNo,episodeNo):
        title = self.getTitleFromList2(titleNo)
        episodeInfo = appEpisodeInfoV3(titleNo, episodeNo)
        if episodeInfo:
            logger.info("tapByImageInfos:%s_%s_%s" % (title["title"], titleNo, episodeInfo["episodeTitle"]))
            self.addCache(titleNo, title, episodeInfo["episodeNo"], episodeInfo["episodeSeq"])
            imageInfos = episodeInfo["imageInfo"]
            swipe_times = len(imageInfos)
            pplInfo = appPPLInfo(titleNo, episodeNo)
            if pplInfo:
                swipe_times+=1
            for i in range(0,swipe_times):
                # self.swipeLeft()
                self.swipeLeftB()
                self.sleep(1)
            if self.waitEleVisiable(BP.VIEWERSHAREBUTTONTEXT):
                logger.info("checkCutViewer成功")
                return self.getBackFromCutViewer()
            else:
                logger.info("checkCutViewer失败")
                self.savePNG("checkCutViewer失败,%s_%s" % (titleNo,episodeNo))
                return False
        else:
            logger.error("checkCutViewer失败")
            self.savePNG("checkCutViewer失败")
            self.noNetClose()
            return False

    ##活动专区
    def checkActivityViewer(self,titleNo,episodeNo):
        shareText = self.waitElePresents(BP.VIEWERSHAREBUTTONTEXT)
        if shareText:
            title = self.getTitleFromList2(titleNo)
            self.savePNG(title["title"],episodeNo)
            episodeInfo = appEpisodeInfoV3(titleNo, episodeNo)
            if episodeInfo:
                self.addCache(titleNo,title,episodeInfo["episodeNo"],episodeInfo["episodeSeq"])
                # recommendInfo = appTitleRecommend2(titleNo)
                # pplInfo = appPPLInfo(titleNo, episodeNo)
                # imgageInfos = episodeInfo["imageInfo"]
                self.tapByImageHeight(titleNo,episodeNo)
                return self.getBackFromViewerByTapXY()
            else:
                self.noNetClose(title["title"],episodeNo)
                return False

        else:
            return self.getBackFromViewerByTapXY()

    ###各种类型跳转viewer后的检验，history为True,查缓存，没有的话去第一话；history为False，不查缓存，直接去episodeNo对应章节
    def checkViewer(self,titleNo,episodeNo=1,history=True):
        title = self.getTitleFromList2(titleNo)
        viewerType = title.get("viewer", None)
        if history:
            cacheTitle = self.getCache(titleNo)
            if cacheTitle:
                if viewerType == "CUT":
                    logger.info("checkViewer：%s_%s_%s" % (title["title"],titleNo,cacheTitle[1]))
                    self.savePNG("书签章节",title["title"],cacheTitle[1])
                    return self.getBackFromCutViewer()
                else:
                    logger.info("checkViewer：%s_%s_%s" % (title["title"],titleNo,cacheTitle[1]))
                    self.savePNG("书签章节",title["title"],episodeNo)
                    return self.getBackFromViewer()
            else:
                if viewerType == "SCROLL":
                    return self.checkScrollViewer(titleNo,1)
                elif viewerType == "MOTION":
                    return self.checkScrollViewer(titleNo,1)
                elif viewerType == "CUT":
                    return self.checkCutViewer(titleNo,1)
                elif viewerType == "ACTIVITYAREA":
                    return self.checkActivityViewer(titleNo,1)
        else:
            # cacheTitle = self.cache.get(titleNo,None)
            cacheTitle = self.getCache(titleNo)
            if cacheTitle and cacheTitle[1] == episodeNo:
                if viewerType == "CUT":
                    logger.info("checkViewer：%s_%s_%s" % (title["title"],titleNo,episodeNo))
                    self.savePNG("请求章节与书签章节一致",title["title"],episodeNo)
                    return self.getBackFromCutViewer()
                else:
                    logger.info("checkViewer：%s_%s_%s" % (title["title"],titleNo,episodeNo))
                    self.savePNG("请求章节与书签章节一致",title["title"],episodeNo)
                    return self.getBackFromViewer()
            else:
                if viewerType == "SCROLL":
                    logger.info('viewerType == "SCROLL"')
                    return self.checkScrollViewer(titleNo,episodeNo)
                elif viewerType == "MOTION":
                    logger.info('viewerType == "MOTION"')
                    return self.checkScrollViewer(titleNo,episodeNo)
                elif viewerType == "CUT":
                    logger.info('viewerType == "CUT"')
                    return self.checkCutViewer(titleNo,episodeNo)
                elif viewerType == "ACTIVITYAREA":
                    logger.info('viewerType == "ACTIVITYAREA"')
                    return self.checkActivityViewer(titleNo,episodeNo)

    ##需要确认跳预览还是viewer，通过查看历史数据
    def checkGetInViewerOrPreview(self,titleNo,episodeNo=1):
        title = self.getTitleFromList2(titleNo)
        viewerType = title.get("viewer", None)
        if (viewerType == "SCROLL" or "MOTION") and not self.checkCache(titleNo):
            return self.checkPreview(titleNo)
        elif self.checkCache(titleNo):
            return self.checkViewer(titleNo,episodeNo,history=True)
        else:
            return self.checkViewer(titleNo,episodeNo,False)


    ##预览
    def checkPreview(self,titleNo,episodeNo=1):
        title = self.getTitleFromList2(titleNo)
        episodeInfo = appEpisodeInfoV3(titleNo,episodeNo)
        if episodeInfo:
            logger.info("checkPreview:%s_%s_%s" % (title["title"], titleNo, episodeInfo["episodeNo"]))
            tsec = "已更新至第%s话" % title["totalServiceEpisodeCount"]
            ele = self.waitElePresents((BP.IDTOBE[0],BP.IDTOBE[1] % tsec))
            if ele:
                self.addCache(titleNo,title,episodeInfo["episodeNo"],episodeInfo["episodeSeq"])
                self.savePNG("预览",title["title"])
                if self.tapByImageHeightPreview(titleNo,episodeNo,BP.PREVIEWNEXTEPISODE):
                    self.savePNG("预览","下一话",title["title"])
                    logger.info("checkPreview成功")
                    return self.closePreivewOrPopupDisplay()
                else:
                    return False

            else:
                if self.noNetClose():
                    return True
                else:
                    return False
        else:
            logger.error("checkPreview失败")
            self.noNetClose()
            return False

    ##底部弹窗
    def checkBottomPopupDispaly(self,titleNo,episodeNo=1):
        title = self.getTitleFromList2(titleNo)
        episodeInfo = appEpisodeInfoV3(titleNo,episodeNo)
        if episodeInfo:
            ele = self.waitElePresents(BP.ALERTTIPS)
            if ele:
                self.addCache(titleNo,title,episodeInfo["episodeNo"],episodeInfo["episodeSeq"])
                self.savePNG("底部弹窗",title["title"])

                if self.tapByImageHeightPreview(titleNo,episodeNo,BP.ALERTNEXTEPISODE):
                    self.savePNG("底部弹窗","下一话",title["title"])
                    return self.closePreivewOrPopupDisplay()
                else:
                    return False

            else:
                return False
        else:
            self.noNetClose()
            return False

    def checkH5(self,text="",bar=True,share=True):
        if bar:
            if share:
                if text:
                    res1 = False
                    if self.waitTextInPage(text):
                        res1 = True
                    res2 = self.eleVisiable(BP.H5SHARE)
                    res3 = self.eleVisiable(BP.BTNBACK)
                    self.savePNG("H5")
                    self.H5Back()
                    return res1 and res2 and res3
                else:
                    res2 = self.eleVisiable(BP.H5SHARE)
                    res3 = self.eleVisiable(BP.BTNBACK)
                    self.savePNG("H5")
                    self.H5Back()
                    return res2 and res3
            else:
                if text:
                    res1 = False
                    if self.waitTextInPage(text):
                        res1 = True
                    res2 = self.eleVisiable(BP.BTNBACK)
                    self.savePNG("H5")
                    self.H5Back()
                    return res1 and res2

                else:
                    res3 = self.eleVisiable(BP.BTNBACK)
                    self.savePNG("H5")
                    self.H5Back()
                    return res3
        else:
            if text:
                res1 = self.waitTextInPage(text)
                self.savePNG("H5")
                self.H5Close()
                return res1
            else:
                self.H5Close()
                self.savePNG("H5")
                return True


    ## viewer,episodeList,web;返回的key，
    ##{'titleNo': ['1577'], 'episodeNo': ['2']}
    ##{'titleNo': ['1577'], 'position': ['0']}
    def parseScheme(self,linkUrl,banner):
        res =  parse.urlparse(linkUrl)
        logger.info("执行parseScheme")
        logger.info(res)
        scheme = res.scheme
        netloc = res.netloc
        # self.savePNG(linkUrl)
        if scheme == "dongman":
            queryDict = parse.parse_qs(res.query)
            if netloc == "viewer":
                titleNo = int(queryDict["titleNo"][0])
                episodeNo = int(queryDict["episodeNo"][0])
                return self.checkViewer(titleNo,episodeNo,False)
            elif netloc == "episodeList":
                titleNo = int(queryDict["titleNo"][0])
                position = queryDict["position"][0]
                if position == "1":
                    return self.checkTitleList(titleNo)
                elif position == "0":
                    return self.checkTitleIntroduce(titleNo)
        else:
            if banner["barDisplay"] == "Y":
                if banner["containShare"] == "Y":
                    logger.info("checkH5(%s)" % linkUrl)
                    return self.checkH5()
                else:
                    logger.info("checkH5(%s,bar=True,share=False)" % linkUrl)
                    return self.checkH5(bar=True,share=False)
            else:
                logger.info("checkH5(%s, bar=False, share=False)" % linkUrl)
                return self.checkH5(bar=False, share=False)


    def H5Share(self):
        return self.waitEleClick(BP.H5SHARE)

    def H5Back(self):
        logger.info("H5Back")
        return self.waitEleClick(BP.BTNBACK)

    def H5Close(self):
        self.waitEleClick(BP.H5CLOSE)


    def noNetClose(self,*args):
        if self.waitEleVisiable(BP.NONETALERT):
            self.savePNG(*args,"无网络连接请重试")
            return self.waitEleClick(BP.NONETALERTCLOSE)
        else:
            return False

    def getRandomInt(self,maxValue=10):
        result = random.randint(0,maxValue)
        logger.info("getRandomInt:%s" % result)
        return result

    def getRandomInts(self,length,count=3,reverse=False):
        result = sorted(random.sample(range(0, length), count),reverse=reverse)
        logger.info("getRandomInts:%s" % str(result))
        return result

    def getRandomDictKeys(self,keys,count=3):
        result = random.sample(list(keys),count)
        logger.info("getRandomChoice:%s" % str(result))
        return result

    def getNewTitle(self):
        newTitles = []
        for k,v in self.data.items():
            if v["newTitle"]:
                newTitles.append(v)
        newTitles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
        return newTitles

    def getGenreDataAll(self,genre="全部", status="全部", sortby="人气"):
        genreDict = {"恋爱": "LOVE",
                     "少年": "BOY",
                     "古风": "ANCIENTCHINESE",
                     "奇幻": "FANTASY",
                     "搞笑": "COMEDY",
                     "校园": "CAMPUS",
                     "都市": "METROPOLIS",
                     "治愈": "HEALING",
                     "悬疑": "SUSPENSE",
                     "励志": "INSPIRATIONAL",
                     # "影视化":"FILMADAPTATION"
                     }
        statusDict = {"连载": "SERIES", "完结": "TERMINATION"}
        titles = list(self.data.values())
        genre = genre.strip()
        status = status.strip()
        sortby = sortby.strip()
        if genre == "全部":
            if status == "全部":
                if sortby == "人气":
                    titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                    return titles
                elif sortby == "最新":
                    titles.sort(key=lambda x: (x["lastEpisodeRegisterYmdt"], x["titleNo"]), reverse=True)
                    return titles
            elif status in statusDict:
                if sortby == "人气":
                    if status == "完结":
                        titles.sort(key=lambda x: (x["likeitCount"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        return result
                    else:
                        titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        return result
                elif sortby == "最新":
                    titles.sort(key=lambda x: (x["lastEpisodeRegisterYmdt"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                    return result

        elif genre in genreDict:
            if status == "全部":
                if sortby == "人气":
                    titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],titles))
                    return result
                elif sortby == "最新":
                    titles.sort(key=lambda x: (x["lastEpisodeRegisterYmdt"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],titles))
                    return result
            elif status in statusDict:
                if sortby == "人气":
                    if status == "完结":
                        titles.sort(key=lambda x: (x["likeitCount"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        result = list(filter(lambda x: genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                        return result
                    else:
                        titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        result = list(filter(lambda x: genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                        return result
                elif sortby == "最新":
                    titles.sort(key=lambda x: (x["lastEpisodeRegisterYmdt"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                    result = list(filter(lambda x: genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                    return result

        elif genre == "影视化":
            if status == "全部":
                if sortby == "人气":
                    titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: x["filmAdaptation"], titles))
                    return result

                elif sortby == "最新":
                    titles.sort(key=lambda x: (x["lastEpisodeRegisterYmdt"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: x["filmAdaptation"], titles))
                    return result
            elif status in statusDict:
                if sortby == "人气":
                    if status == "完结":
                        titles.sort(key=lambda x: (x["likeitCount"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        result = list(filter(lambda x: x["filmAdaptation"], result))
                        return result
                    else:
                        titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        result = list(filter(lambda x: genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                        return result
                elif sortby == "最新":
                    titles.sort(key=lambda x: (x["lastEpisodeRegisterYmdt"], x["titleNo"]), reverse=True)
                    result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                    result = list(filter(lambda x: x["filmAdaptation"], result))
                    return result

    def getAuthorText(self,title):
        # logger.info(title)
        writingAuthorName = title.get("writingAuthorName")
        pictureAuthorName = title.get("pictureAuthorName")
        if writingAuthorName == pictureAuthorName:
            return writingAuthorName
        else:
            return "%s/%s" % (writingAuthorName,pictureAuthorName)



    def getRandomGender(self):
        result = random.choice([BP.USERPREFENRENCEGENDERMALE,BP.USERPREFENRENCEGENDERFEMALE])
        logger.info("getRandomGender：%s" % str(result))
        return result


    def getRandomAge(self):
        result = random.choice([BP.USERPREFENRENCEAGE12, BP.USERPREFENRENCEAGE13,BP.USERPREFENRENCEAGE16,BP.USERPREFENRENCEAGE19,
                                BP.USERPREFENRENCEAGE23,BP.USERPREFENRENCEAGE26,BP.USERPREFENRENCEAGE36,BP.USERPREFENRENCEJUMP])
        logger.info("getRandomAge：%s" % str(result))
        return result

    def getRandomGenre(self):
        jump = random.randint(0,1)
        count = random.randint(1,12)
        result = random.sample([BP.USERPREFENRENCEGENRBOY, BP.USERPREFENRENCEGENRELOVE,BP.USERPREFENRENCEGENRECHINA, BP.USERPREFENRENCEGENREFANTASY,
                                BP.USERPREFENRENCEGENRECOMEDY, BP.USERPREFENRENCEGENRESCHOOL,BP.USERPREFENRENCEGENREDUSHI, BP.USERPREFENRENCEGENREHEALING,
                                BP.USERPREFENRENCEGENREXUANYI, BP.USERPREFENRENCEGENRELIZHI,BP.USERPREFENRENCEGENREFILM, BP.USERPREFENRENCEGENREFINISH],count)
        logger.info("jump:%s" % jump)
        logger.info("count:%s" % count)
        logger.info("getRandomGenre：%s" % str(result))
        return jump,result

    def checkPageWebtoonData(self,data,randomCount=1):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        for i in range(0,data_length):
            # likeText = self.handleTitleLikeCount(data[i]["webtoon"]["likeitCount"])
            # print(likeText)

            # res2 = self.swipeUpUntilDisplay((DP.IDTOBE[0],DP.IDTOBE[1] % likeText),maxTimes=10)
            if i in randomData:
                if self.swipeUpUntilDisplay((BP.IDTOBE[0], BP.IDTOBE[1] % data[i]["webtoon"]["title"]), maxTimes=20):
                    if self.waitEleClick((BP.IDTOBE[0],BP.IDTOBE[1] % data[i]["webtoon"]["title"])):
                        if self.checkGetInViewerOrPreview(data[i]["webtoon"]["titleNo"]):
                            count+=1

        if count == len(randomData):
            return True
        else:
            return False

    ##只会进入viewer，没有预览的可能，只进入第一话（大家都在看用）
    def checkPageWebtoonDataViewer(self,data,randomCount=1,addFavourite=False,addComment=False,downloadEpisode=False):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        for i in range(0,data_length):
            if self.swipeUpUntilDisplay((BP.IDTOBE[0],BP.IDTOBE[1] % data[i]["webtoon"]["title"]),maxTimes=10):
                if i in randomData:
                    if self.waitEleClick((BP.IDTOBE[0],BP.IDTOBE[1] % data[i]["webtoon"]["title"])):
                        if addFavourite:
                            self.addFavouriteInViewer(loading=True)
                        if addComment:
                            self.addCommentInViewer()
                        if downloadEpisode:
                            self.downloadEpisode(data[i]["webtoon"]["titleNo"])
                        if self.checkViewer(data[i]["webtoon"]["titleNo"],1,False):
                            count +=1

        if count == len(randomData):
            return True
        else:
            return False


    def addCommentInViewer(self,loading=False):
        if self.navigatorOn(waitTime=5,loading=loading):
            return self.sendCommentInViewer(BP.COMMENTDATA)
        else:
            return False

    def addFavouriteInViewer(self,times=0,loading=False):
        logger.info("执行addFavouriteInViewer")
        if self.navigatorOn(times=times,loading=loading):
            ele = self.waitElePresents(BP.VIEWERPLUSFAVOURITE,seconds=2)
            if ele:
                self.tapXY(ele)
                return True
            else:
                return False
        return False

    def downloadEpisode(self,titleNo,times=0,loading=False):
        logger.info("执行downloadEpisode")
        if self.navigatorOn(times=times,loading=loading):
            if self.waitEleClick(BP.VIEWERSHARE,seconds=2):
                if self.waitEleClick(BP.SHAREDOWNLOAD):
                    return self.handleDownloadPage(titleNo)
        
        return False



    def handleDownloadPage(self,titleNo):
        list_data = appEpisodeListV3(titleNo)["episode"]
        list_data_filter = list(filter(lambda x:x["serviceStatus"] == "SERVICE",list_data))
        if self.handlePickerWheelValue(BP.DOWNLOADPICKERWHEELTO,dest=list_data_filter[-1]["episodeSeq"]):
            if self.waitEleClick(BP.DOWNLOADSTART):
                # if self.waitEleVisiable(BP.DOWNLOAD100):
                self.sleep(5)
                if self.handleDownloadFinish():
                    self.addSaveData(titleNo,list_data_filter[-1]["episodeTitle"])
                    return True
        return False

    def handlePickerWheelValue(self,loc,times=0,dest="1"):
        if times>10:
            logger.error("handlePickerWheelValue次数过多，%s次" % times)
            # return False
            ##因为获取不到text执行，10次之后返回True
            return True
        ele = self.waitElePresents(loc)
        if ele:
            ele_text = ele.text
            if ele_text:
                if ele_text == str(dest):
                    logger.info("handlePickerWheelValue成功")
                    return True
                else:
                    x,y = self.getXY(ele)
                    self.scrollSlow(x,y,x,self.height,duration=200,who="handlePickerWheelValue")
                    time.sleep(2)
                    times+=1
                    logger.info("handlePickerWheelValue第%s次失败，dest为%s,当前text为：%s" % (times,dest,ele_text))
                    return self.handlePickerWheelValue(loc,times,dest)
            else:
                x, y = self.getXY(ele)
                self.scrollSlow(x, y, x, self.height, duration=200, who="handlePickerWheelValue")
                times += 1
                logger.info("handlePickerWheelValue第%s次失败，dest为%s,当前text为：%s" % (times, dest, ele_text))
                return self.handlePickerWheelValue(loc, times, dest)
        else:
            logger.error("handlePickerWheelValue失败，获取元素失败%s" % str(loc))
            return False

    def handlePickerWheelValueByEle(self,ele,times=0,dest="1"):
        if times>10:
            return False
        if ele.text == str(dest):
            return True
        else:
            x,y = self.getXY(ele)
            self.scrollSlow(x,y,x,self.height,duration=100,who="handlePickerWheelValue")
            times += 1
            return self.handlePickerWheelValueByEle(ele,times,dest)

    def handleDownloadFinish(self,times=0):
        logger.info("handleDownloadFinish")
        if times > 20:
            logger.info("handleDownloadFinish失败次数过多，失败%s次" % times)
            return False
        cl = self.waitEleVisiable(BP.DOWNLOADCLOSE)
        if cl:
            if cl.is_enabled():
                logger.info("handleDownloadFinish_成功")
                return self.waitEleClick(BP.DOWNLOADCLOSE)
            else:
                self.sleep(5)
                times+=1
                logger.info("handleDownloadFinish第%s次失败" % times)
                return self.handleDownloadFinish(times)
        else:
            logger.info("handleDownloadFinish失败，元素不可见" % str(BP.DOWNLOADCLOSE))
            return False


    ##我的漫画页，我的关注我的评论未登录时，点击登录的位置
#     '''
#     x	0
#     y	136
#     width	414
#     height	669，187，349

#     x	0
# y	124
# width	375
# height	606，169，316
#
#     x
#     0
#     y
#     100
#     width
#     375
#     height
#     519，169，293
#     '''
    def tapTopLogin(self,ele):
        rect = self.getXY(ele,False)
        y = rect["y"]
        if y >= 136:
            self.tapByXY(self.width/2,214+y)
        else:
            self.tapByXY(self.width/2,193+y)

    def closeFirstMengCeng(self):
        if self.waitEleVisiable((BP.MYCARTOONMENGCENGRECENTLY),seconds=1,poll_frequency=1):
            logger.info("监测到有蒙层，关闭蒙层")
            return self.waitEleClick((BP.MYCARTOONMENGCENGCLOSE))
        logger.info("没有检测到有蒙层")
        return True

    def addSaveData(self,titleNo,episodeNo):
        if titleNo in self.saveData:
            if episodeNo not in self.saveData[titleNo]:
                self.saveData[titleNo].append(episodeNo)
        else:
            self.saveData[titleNo]=[episodeNo]
        logger.info("addSaveData下载成功")

    def swith2PassLogin(self,seconds=1):
        topass =  self.waitElePresents(BP.TOPASSLOGIN,seconds=seconds)
        if topass:
            logger.info("切换到【密码登录】")
            topass.click()
            return True
        logger.info("没有切换到【密码登录】")


    def switch2CodeLogin(self,seconds=1):
        tocode =  self.waitElePresents(BP.TOCODELOGIN,seconds=seconds)
        if tocode:
            logger.info("切换到【验证码登录】")
            tocode.click()
            return True
        logger.info("没有切换到【验证码登录】")

    def loginByPassNotLoginPage(self,user,passwd,successText="登录成功"):
        self.swith2PassLogin(seconds=2)
        ele_account = self.waitElePresents(BP.INPUTUSERACCOUNT)
        ele_accountx, ele_accounty = self.getXY(ele_account)
        self.tapByXY(ele_accountx + 50, ele_accounty)
        self.waitElePresents(BP.INPUTUSER).send_keys(user)

        # ele_password = self.waitElePresents(MP.INPUTUSERPASSWORD)
        # ele_passwordx,ele_passwordy = self.getXY(ele_password)
        # self.tapByXY(ele_passwordx+50,ele_passwordy)
        self.waitElePresents(BP.INPUTPASS).send_keys(passwd)
        logger.info("点击【登录】")
        if self.waitEleClick(BP.LOGINCONFIRM):
            if successText:
                if self.waitTextInPage(successText):
                    logger.info("【%s登录成功】" % user)
                    return True
            else:
                return True
        self.savePNG("登录失败", user)
        return False


    def deleteFavourites(self):
        return appFavoriteTotalRemoveAll()

    def deleteComments(self):
        ids = v1CommentOwnAllOnlyIds()
        count = 0
        for id in ids:
            deleteComment(id)
        if count == len(ids):
            return True
        else:
            return False

    def getRandomTitleNo(self):
        titles = self.getTitleFromList2()
        titleNo = random.choice(titles)
        logger.info("getRandomTitle获取的随机titleNo为%s" % titleNo)
        return titleNo

    def getNowDatetime(self):
        return datetime.datetime.now()

    def getDiffSeconds(self,a,b):
        return (b-a).seconds


    def tapReadTitle(self,scrollTimes,plusTimes=1):
        slowTimes = 0
        breakFlag = False
        x, y = self.width / 2, 3 * self.height / 4
        for i in range(1, scrollTimes + plusTimes):
            starttime = self.getNowDatetime()
            self.tapByXY(x, y)
            self.sleep(0.2)
            logger.info("TAP >> %s次" % i)
            endtime = self.getNowDatetime()
            if self.getDiffSeconds(starttime, endtime) > 5:
                slowTimes += 1
                logger.info("TAP时间超过5秒，超时次数为：%s" % slowTimes)
            if slowTimes > 2:
                logger.info("TAP速度太慢，超时次数超过2次，退出处理")
                breakFlag = True
                break
        if breakFlag:
            return False
        else:
            return True


if __name__ == "__main__":
    pass
    bpa = BasePageAction(1,2,3,4,5,6,7,8)
    # print(bpa.handleTitleLikeCount(999))
    # print(bpa.handleTitleLikeCount(123123))
    # print(bpa.handleTitleLikeCount(2214523))
    # bpa.parseScheme("dongman://viewer/webtoon?titleNo=1577&episodeNo=2")
    # bpa.parseScheme("dongman://episodeList/webtoon?titleNo=1577&position=1")
    # bpa.parseScheme("dongman://episodeList/webtoon?titleNo=1577&position=0")
    # bpa.parseScheme("https://itunes.apple.com/cn/app/dong-man/id1168836057?mt=8")
    # a = list(bpa.getWeekday())
    # for i in a:
    #     print(i,a.index(i))

