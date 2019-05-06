#coding=utf-8

import unittest
from appium import webdriver
from cn.dm.src.testcases.baseTestcase import BaseTestcase
from ..pageaction.basePageAction import BasePageAction as BPA
from ..pageaction.myPageAction import MyPageAction as MPA

import warnings


class MyPageLoginTestcase(BaseTestcase):


    def test002_loginByQQ(self):
        self.MPA.getInMyPage()
        self.MPA.tapAccountManage()
        self.MPA.loginByQQ()
        self.MPA.logout()

    def test003_loginByWeibo(self):
        self.MPA.getInMyPage()
        self.MPA.tapAccountManage()
        self.MPA.loginByWeibo()
        self.MPA.logout()

    def test004_loginByWechat(self):
        self.MPA.getInMyPage()
        self.MPA.tapAccountManage()
        self.MPA.loginByWechat()
        self.MPA.logout()

    def test005_loginByEmail(self,user="weixindogs@163.com",passwd="qwe123"):
        self.MPA.getInMyPage()
        self.MPA.tapAccountManage()
        self.MPA.loginByPass(user=user,passwd=passwd)
        self.MPA.logout()

    def test006_loginByMobile(self,user="13683581996",passwd="qwe123"):
        self.MPA.getInMyPage()
        self.MPA.tapAccountManage()
        self.MPA.loginByPass(user=user,passwd=passwd)
        # self.MPA.logout()


class MyPageTestcase(BaseTestcase):

    def test002_editNickName(self):
        self.MPA.getInPersonInfo()

    def test003_getInMyWallet(self):
        self.MPA.getInMyWallet()

    def test004_getInDmMsg(self):
        self.MPA.getInDongManMsg()

    def test005_getInPushSetup(self):
        self.MPA.getInPushSetup()

    def test006_getInFeedback(self):
        self.MPA.getInFeedback()

    def test007_getInAppInf(self):
        self.MPA.getInAPPInfo()

