#coding=utf-8

import unittest
import warnings
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from ..pageaction.basePageAction import BasePageAction as BPA
from ..pageaction.myPageAction import MyPageAction as MPA
from ..pageaction.discoveryPageAction import DiscoveryPageAction as DPA
from ..pageaction.updatePageAction import UpdagePageAction as UPA
from ..pageaction.myCartoonPageAction import MyCartoonPageAction as MCPA
from ..login import login,Config
from ..interface import appTitleList2,appHome4,appHomeMenus,appHomeMenuDetail
from ..login import getConfig,setConfig


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID



class BaseTestcase(unittest.TestCase):
    #
    # def skipCondition(self):
    #     if self.driver.desired_capabilities()["udid"] == getConfig("udid","real"):
    #         return True
    #     else:
    #         return False

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        desired_caps = {}
        # app_path = 'http://iosapps.itunes.apple.com/itunes-assets/Purple113/v4/93/6d/fc/936dfc4a-e3e1-3920-b90b-d53086a70a13/pre-thinned17555684376910244084.thinned.signed.beta.ipa?accessKey=1568966328_2501250152641289370_DqRe7scWPW6q6rQOEedOkyK0x4cs2QM9iYVNGCMgPWoIK8SEbIdFnDDIHUJGCnasV8LnJg8C5UQyKur%2BT90DI2qsafvnzRE4vWiuuNytUKuoTiF3K0HWigFFGnawdkZs%2FckEfx4R2OrR8y7BOTX6JuYwBplL3Wxa8k47sG%2FSxDgKA40mXzLkaeeMZzARQHLKCx8bxTFciJAlr6n7BacsZQ%3D%3D'
        # app_path = "https://deploy.dongmancorp.cn/load/app/ios/qa2/2.2.2.10_qa2_0917/2.2.2.10_qa2_0917.ipa"
        app_path = "https://deploy.dongmancorp.cn/load/app/ios/qa2/2.2.1_pro_0918/2.2.1_pro_0918.ipa"
        # app_path ="/Users/dongman/Downloads/dm.ipa"
        cls.appPath = app_path
        desired_caps["showXcodeLog"] = True
        desired_caps['platformName'] = 'iOS'
        desired_caps['clearSystemFiles'] = True

        # ## xs max
        # desired_caps['udid'] = '00008020-000E502E0E04002E'
        # desired_caps['deviceName'] = 'xs'
        # desired_caps['platformVersion'] = '13.0'

        ## ip6
        # desired_caps['udid'] = '3ba121fe9efb423329abcbfc1a85fbbad305af8c'
        # desired_caps['deviceName'] = 'ip'
        # desired_caps['platformVersion'] = '10.3.3'
        #


        # ip8
        desired_caps['udid'] = '8420d2edfc2ea6dcf8e3d4c32eb9be0c84f2ee91'
        desired_caps['deviceName'] = 'iPhone8'
        desired_caps['platformVersion'] = '12.4'



        # ## iPhone X
        # desired_caps['udid'] = "f1066a9e302a39acc03838cbffea0891bfc97675"
        # desired_caps['deviceName'] = 'iPhone x'
        # desired_caps['platformVersion'] = '12.3.1'


        desired_caps["xcodeOrgId"]= "R7S9UW83XA"
        desired_caps["xcodeSigningId"]= "iPhone Developer"
        desired_caps["keychainPath"] = "/Users/dongman/Library/Keychains/login.keychain-db"
        desired_caps["keychainPassword"] = "111111"
        desired_caps['useNewWDA'] = False
        desired_caps["derivedDataPath"]="/Users/dongman/Library/Developer/Xcode/DerivedData/WebDriverAgent-dikkwtrisltbeobjmfvpthwwekvs"
        desired_caps['noReset'] = False
        desired_caps['app'] = cls.appPath
        desired_caps['newCommandTimeout'] = 200
        # desired_caps['automationName'] = "XCUITest"
        # desired_caps['useNewWDA'] = True
        desired_caps['automationName'] = "XCUITest"
        desired_caps['bundleId'] = 'com.naver.linewebtoon.cn'


        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(10)
        # cls.driver.start_recording_screen(**{"timeLimit":"600"})
        if desired_caps['udid'] == '00008020-000E502E0E04002E':
            ##开始跳过第三方登录
            setConfig("skip","login","1")
        else:
            ##关闭跳过第三方登录
            setConfig("skip","login","0")
        cls.data = appTitleList2()  ##list2，请求的数据
        login(Config("mobile"), Config("passwd"), "PHONE_NUMBER")
        cls.home = appHome4()
        cls.menus = appHomeMenus()
        cls.menusDetail = []
        for i in cls.menus:
            menuId = i['id']
            if menuId != 0:
                menuDetail = appHomeMenuDetail(menuId)
                cls.menusDetail.append(menuDetail)
                i["menuDetail"] = menuDetail

        cls.cache = {}  ## 进入viewer的记录
        screenSize = cls.driver.get_window_size()
        cls.width = screenSize["width"]
        cls.height = screenSize["height"]
        cls.defaultPage = False
        cls.saveData = {}
        tupleParams = (cls.driver,cls.defaultPage,cls.data,cls.saveData,cls.cache,cls.width,cls.height,cls.home,cls.menus,cls.menusDetail)
        cls.BPA = BPA(*tupleParams)
        cls.MPA = MPA(*tupleParams)
        cls.DPA = DPA(*tupleParams)
        cls.UPA = UPA(*tupleParams)
        cls.MCPA = MCPA(*tupleParams)
        cls.BPA.startAppCloseAlert(Config("env"))

    @classmethod
    def tearDownClass(cls):
        # cls.driver.stop_recording_screen()
        cls.driver.quit()