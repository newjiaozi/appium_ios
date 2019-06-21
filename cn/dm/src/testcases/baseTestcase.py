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


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID


class BaseTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        desired_caps = {}
        # cls.appPath = "/Users/dongman/PycharmProjects/appium_ios/cn/dm/src/app/linewebtoon_CN.ipa"
        cls.appPath = "https://deploy.dongmancorp.cn/load/app/ios/qa2/2.1.1.5_qa2_0524/2.1.1.5_qa2_0524.ipa"
        desired_caps['platformName'] = 'iOS'
        ## xs max
        desired_caps['udid'] = '00008020-000E502E0E04002E'
        desired_caps['deviceName'] = 'xs'
        desired_caps['platformVersion'] = '12.2'
        ## ip6
        # desired_caps['udid'] = '3ba121fe9efb423329abcbfc1a85fbbad305af8c'
        # desired_caps['deviceName'] = 'ip'
        # desired_caps['platformVersion'] = '10.3.3'
        #
        desired_caps["xcodeOrgId"]= "R7S9UW83XA"
        desired_caps["xcodeSigningId"]= "iPhone Developer"
        desired_caps["keychainPath"] = "/Users/dongman/Library/Keychains/login.keychain-db"
        desired_caps["keychainPassword"] = "111111"
        desired_caps['noReset'] = True
        desired_caps['app'] = cls.appPath
        desired_caps['useNewWDA'] = False
        desired_caps['newCommandTimeout'] = 200
        # desired_caps['automationName'] = "XCUITest"
        # desired_caps['useNewWDA'] = True
        desired_caps['automationName'] = "XCUITest"
        desired_caps['bundleId'] = 'com.naver.linewebtoon.cn'


        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(20)
        cls.BPA = BPA(cls.driver)
        cls.MPA = MPA(cls.driver)
        cls.DPA = DPA(cls.driver)
        cls.UPA = UPA(cls.driver)
        cls.MCPA = MCPA(cls.driver)
        cls.BPA.startAppCloseAlert()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()