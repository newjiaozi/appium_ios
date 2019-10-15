import unittest
import warnings
from appium import webdriver
from ..pageaction.basePageAction import BasePageAction as BPA
from ..pageaction.myPageAction import MyPageAction as MPA
from ..pageaction.myCartoonPageAction import MyCartoonPageAction as MCPA
from ..pageaction.discoveryPageAction import DiscoveryPageAction as DPA
from ..pageaction.updatePageAction import UpdagePageAction as UPA



driver = ''
bpq = ''
mpa = ''
mcpa = ''
dpa = ''
upa = ''


### 修改成这个年头日module执行一次 setup

def setUpModule():
    warnings.simplefilter("ignore", ResourceWarning)
    desired_caps = {}
    appPath = "/Users/dongman/PycharmProjects/appium_ios/cn/dm/src/app/linewebtoon_CN.ipa"
    desired_caps['platformName'] = 'iOS'
    ## xs max
    desired_caps['udid'] = '00008020-000E502E0E04002E'
    desired_caps['deviceName'] = 'xs'
    desired_caps['platformVersion'] = '12.1.2'
    ## ip6
    # desired_caps['udid'] = '3ba121fe9efb423329abcbfc1a85fbbad305af8c'
    # desired_caps['deviceName'] = 'ip'
    # desired_caps['platformVersion'] = '10.3.3'
    #
    # desired_caps["xcodeOrgId"]= "R7S9UW83XA"
    # desired_caps["xcodeSigningId"]= "iPhone Developer"
    # desired_caps['noReset'] = True
    desired_caps['app'] = appPath
    desired_caps['useNewWDA'] = False
    # desired_caps['useNewWDA'] = True
    desired_caps['automationName'] = "XCUITest"
    desired_caps['bundleId'] = 'com.naver.linewebtoon.cn'
    global driver,bpa,mpa,mcpa,dpa,upa
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    bpa = BPA(driver)
    mpa = MPA(driver)
    mcpa = MCPA(driver)
    dpa = DPA(driver)
    upa = UPA(driver)
    bpa.startAppCloseAlert()

def tearDownModule():
    global driver
    driver.quit()



class MyPageTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global mpa
        cls.mpa = mpa

    def test1_loginByMobile(self,user="13683581996",passwd="qwe123"):
        self.mpa.getInMyPage()
        self.mpa.tapAccountManage(tologin=False)
        self.mpa.loginByPass(user=user,passwd=passwd)

    def test2_editNickName(self):
        self.mpa.getInPersonInfo()

    def test3_getInMyWallet(self):
        self.mpa.getInMyWallet()

    def test4_getInDmMsg(self):
        self.mpa.getInDongManMsg()

    def test5_getInPushSetup(self):
        self.mpa.getInPushSetup()

    def test5_getInFeedback(self):
        self.mpa.getInFeedback()

    def test6_getInAppInf(self):
        self.mpa.getInAPPInfo()


class MyCartoonTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global mcpa
        cls.mcpa = mcpa
        cls.mcpa.getInMyToon()

    def test1_recentlyLooking(self):
        # self.mcpa.getInMyToon()
        self.mcpa.getInRecentLook()


    def test2_mySubscribe(self):
        # self.mcpa.getInMyToon()
        self.mcpa.getInMySubscribe()


    def test3_save(self):
        # self.mcpa.getInMyToon()
        self.mcpa.getInSave()


    def test4_Comment(self):
        # self.mcpa.getInMyToon()
        self.mcpa.getInMyComment()



class DiscoveryTestcaee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global dpa
        cls.dpa = dpa
        cls.dpa.getInFoundPage()

    def test1_checkDefault(self):
        self.dpa.getInRQ()

class UpdateTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global upa
        cls.upa = upa
        cls.upa.getInUpdatePage()

    def test1_checkDefault(self):
        self.upd.getInDefault()
