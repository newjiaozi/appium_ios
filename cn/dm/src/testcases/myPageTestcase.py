#coding=utf-8

from cn.dm.src.testcases.baseTestcase import BaseTestcase
import unittest

from ..login import Config
from ..handleSqlite import getConfig as gc


class MyPageTestcase(BaseTestcase):

    @unittest.skipIf(gc("skip_login") == "0","不能第三方登录")
    def test002_loginByQQ(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ())
        self.assertTrue(self.MPA.logout())

    @unittest.skipIf(gc("skip_login") == "0","不能第三方登录")
    def test003_loginByQQQuick(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    @unittest.skipIf(gc("skip_login") == "0","不能第三方登录")
    def test004_loginByWeibo(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByWeibo())
        self.assertTrue(self.MPA.logout())

    @unittest.skipIf(gc("skip_login") == "0","不能第三方登录")
    def test005_loginByWeiboQuick(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByWeibo(quick=True))
        self.assertTrue(self.MPA.logout())

    @unittest.skipIf(gc("skip_login") == "0","不能第三方登录")
    def test006_loginByWechat(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByWechat())
        self.assertTrue(self.MPA.logout())

    @unittest.skipIf(gc("skip_login") == "0","不能第三方登录")
    def test007_loginByWechatQuick(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByWechat(quick=True))
        self.assertTrue(self.MPA.logout())

    def test008_loginByEmail(self,user=Config("email"),passwd=Config("passwd")):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByPass(user=user,passwd=passwd,type="EMAIL"))
        self.assertTrue(self.MPA.logout())


    def test009_loginByEmailQuick(self,user=Config("email"),passwd=Config("passwd")):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByPass(user=user,passwd=passwd,type="EMAIL",quick=True))
        self.assertTrue(self.MPA.logout())

    def test010_loginByMobile(self,user=Config("mobile"),passwd=Config("passwd")):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByPass(user=user,passwd=passwd,type="MOBILE"))
        self.assertTrue(self.MPA.logout())

    def test011_loginByMobileQuick(self,user=Config("mobile"),passwd=Config("passwd")):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByPass(user=user,passwd=passwd,type="MOBILE",quick=True))

    def test021_editNickName(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInPersonInfo())

    def test022_getInAccountManage(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInAccountManage())

    @unittest.skip("skip")
    def test023_getInMyWallet(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInMyWallet())

    def test024_getInDmMsg(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInDongManMsg())

    def test025_getInPushSetup(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInPushSetup())

    def test026_getInFeedback(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInFeedback())

    def test027_getInAppInf(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.getInAPPInfo())