#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.myPage import MyPage as MP

class MyPageAction(BasePageAction):


    # def getInMyPage(self):
    #     # mybtn = self.waitElePresents(MP.MY)
    #     # mybtn.click()
    #     self.waitEleClick(MP.MY)

    def tapAccountManage(self,tologin=True):

        self.waitEleClick(MP.ACCOUNTMANAGE)
        if tologin:
            if self.waitElePresents(MP.QUICKLOGIN):
                self.waitEleClick(MP.OTHERLOGIN)


    def swith2PassLogin(self):
        topass =  self.waitElePresents(MP.TOPASSLOGIN,seconds=5)
        if topass:
            topass.click()

    def switch2CodeLogin(self):
        tocode =  self.waitElePresents(MP.TOCODELOGIN,seconds=5)
        if tocode:
            tocode.click()

    def loginByPass(self,user,passwd):
        self.swith2PassLogin()
        self.waitElePresents(MP.INPUTUSER).send_keys(user)
        self.waitElePresents(MP.INPUTPASS).send_keys(passwd)
        self.waitEleClick(MP.LOGINCONFIRM)
        if self.waitElePresents(MP.LOGINSUCCESS):
            self.waitElePresents(MP.ACCOUNTNICKNAMEMOBILE)
            self.savePNG("登录成功"+user)

    def loginByWechat(self):
        self.switch2CodeLogin()
        self.waitEleClick(MP.WECHATLOGIN)
        if self.waitElePresents(MP.LOGINSUCCESS):
            self.savePNG("登录成功"+"wechat")
        self.terminalAPP("wechat")

    def loginByQQ(self):
        self.switch2CodeLogin()
        self.waitEleClick(MP.QQLOGIN)
        lc = self.waitElePresents(MP.LOGINCONFIRM)
        if lc:
            lc.click()
        if self.waitElePresents(MP.LOGINSUCCESS):
            self.savePNG("登录成功"+"QQ")
        self.terminalAPP("QQ")

    def loginByWeibo(self):
        self.switch2CodeLogin()
        self.waitEleClick(MP.WEIBOLOGIN)
        if self.waitElePresents(MP.LOGINSUCCESS):
            self.savePNG("登录成功"+"WEIBO")
        self.terminalAPP("weibo")

    def logout(self):
        self.getInMyPage()
        self.tapAccountManage(tologin=False)
        self.waitEleClick(MP.ACCOUNTLOGOUT)

    def getInPersonInfo(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.NICKNAMERE)
        cancel = self.waitElePresents(MP.EDITINFOCANCEL)
        if cancel:
            self.savePNG("编辑个人资料cancel")
            cancel.click()
        self.waitEleClick(MP.NICKNAMERE)
        self.waitEleClick(MP.EDITINFO)
        # saveele = self.waitElePresents(MP.SAVE)
        saveele = self.waitElePresents(MP.SAVECLOSE)
        if saveele:
            self.savePNG("编辑个人资料页")
            saveele.click()


    def getInAccountManage(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.ACCOUNTMANAGE)
        if self.waitElePresents(MP.ACCOUNTIDRE):
            self.savePNG("账号管理页面")
        self.getBack()

    def getInMyWallet(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.MYWALLET)
        if self.waitElePresents(MP.RECHARGERECORD):
            self.savePNG("我的钱包页面")
            self.getBack()

    def getInDongManMsg(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.MESSAGE)
        if self.waitElePresents(MP.MESSAGETITLE):
            self.savePNG("公告事项")
            self.getBack()

    def getInPushSetup(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.ALARM)
        if self.waitElePresents(MP.NEWONLINE):
            self.savePNG("推送设置")
            self.waitEleClick(MP.BACK)

    def getInFeedback(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.FEEDBACK)
        if self.waitElePresents(MP.FEEDBACKSUBMIT):
            self.savePNG("意见反馈")
            self.waitEleClick(MP.BACK)

    def getInAPPInfo(self):
        self.waitEleClick(MP.MY)
        self.waitEleClick(MP.APPINFO)
        if self.waitElePresents(MP.APPHELP):
            self.savePNG("APP信息")
            self.waitEleClick(MP.BACK)


