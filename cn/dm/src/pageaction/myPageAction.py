#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.myPage import MyPage as MP
from ..logger import logger

class MyPageAction(BasePageAction):


    # def getInMyPage(self):
    #     # mybtn = self.waitElePresents(MP.MY)
    #     # mybtn.click()
    #     self.waitEleClick(MP.MY)

    def tapAccountManage(self,tologin=True):
        logger.info("点击【账号管理】")
        if tologin:
            if self.waitEleClick(MP.ACCOUNTMANAGE):
                if self.waitElePresents(MP.QUICKLOGIN,seconds=1):
                    logger.info("点击【其他方式登录】")
                    return self.waitEleClick(MP.OTHERLOGIN)
                else:
                    return True
            else:
                return False
        else:
            return self.waitEleClick(MP.ACCOUNTMANAGE)



    def loginByPass(self,user,passwd,type="MOBILE",quick=False):
        if type == "MOBILE":
            nickName = MP.ACCOUNTNICKNAMEMOBILE
        elif type == "EMAIL":
            nickName = MP.ACCOUNTNICKNAMEEMAIL
        if quick:
            if self.tapAccountManage(False):
                if self.waitEleClick(MP.QUICKLOGIN):
                    self.waitElePresents(MP.QUICKMOBILEPASSWD).send_keys(passwd)
                    self.waitEleClick(MP.LOGINCONFIRM)
                    if self.waitElePresents(MP.LOGINSUCCESS):
                        if self.waitElePresents(nickName):
                            logger.info("【%s登录成功】" % user)
                            return True

        else:
            if self.tapAccountManage():
                self.swith2PassLogin()
                self.waitElePresents(MP.INPUTUSER).send_keys(user)
                self.waitElePresents(MP.INPUTPASS).send_keys(passwd)
                logger.info("点击【登录】")
                self.waitEleClick(MP.LOGINCONFIRM)
                if self.waitElePresents(MP.LOGINSUCCESS):
                    if self.waitElePresents(nickName):
                        logger.info("【%s登录成功】" % user)
                        return True

        logger.info("【%s登录失败】" % user)
        self.savePNG("登录失败", user)
        return False

    def loginByWechat(self,quick=False):
        if quick:
            if self.tapAccountManage(False):
                if self.waitEleClick(MP.QUICKLOGIN):
                    if self.waitElePresents(MP.LOGINSUCCESS):
                        if self.waitElePresents(MP.ACCOUNTNICKNAMEWEIXIN):
                            logger.info("【wechat登录成功】")
                            self.terminalAPP("wechat")
                            return True

        else:
            if self.tapAccountManage():
                self.switch2CodeLogin()
                logger.info("点击【微信登录】")
                if self.waitEleClick(MP.WECHATLOGIN):
                    if self.waitElePresents(MP.LOGINSUCCESS):
                        if self.waitElePresents(MP.ACCOUNTNICKNAMEWEIXIN):
                            logger.info("【微信登录成功】")
                            self.terminalAPP("wechat")
                            return True
        logger.info("【微信登录失败】")
        self.savePNG("登录失败", "wechat")
        self.terminalAPP("wechat")
        return False

    def loginByQQ(self,quick=False):
        if quick:
            if self.tapAccountManage(False):
                if self.waitEleClick(MP.QUICKLOGIN):
                    if self.waitEleClick(MP.LOGINCONFIRM):
                        if self.waitElePresents(MP.LOGINSUCCESS):
                            self.waitElePresents(MP.ACCOUNTNICKNAMEQQ)
                            logger.info("【QQ登录成功】")
                            self.terminalAPP("QQ")
                            return True

        else:
            if self.tapAccountManage():
                self.switch2CodeLogin()
                logger.info("点击【QQ登录】")
                if self.waitEleClick(MP.QQLOGIN):
                    lc = self.waitElePresents(MP.LOGINCONFIRM)
                    if lc:
                        lc.click()
                        if self.waitElePresents(MP.LOGINSUCCESS):
                            self.waitElePresents(MP.ACCOUNTNICKNAMEQQ)
                            logger.info("【QQ登录成功】")
                            self.terminalAPP("QQ")
                            return True
        logger.info("【QQ登录失败】")
        self.savePNG("登录失败","QQ")
        self.terminalAPP("QQ")
        return False


    def loginByWeibo(self,quick=False):
        if quick:
            if self.tapAccountManage(False):
                if self.waitEleClick(MP.QUICKLOGIN):
                    if self.waitElePresents(MP.LOGINSUCCESS):
                        self.waitElePresents(MP.ACCOUNTNICKNAMEWEIBO)
                        logger.info("【微博登录成功】")
                        self.terminalAPP("weibo")
                        return True

        else:
            if self.tapAccountManage():
                self.switch2CodeLogin()
                logger.info("点击【微博登录】")
                if self.waitEleClick(MP.WEIBOLOGIN):
                    if self.waitElePresents(MP.LOGINSUCCESS):
                        self.waitElePresents(MP.ACCOUNTNICKNAMEWEIBO)
                        logger.info("【微博登录成功】")
                        self.terminalAPP("weibo")
                        return True
        logger.info("【微博登录失败】")
        self.terminalAPP("weibo")
        self.savePNG("登录失败","WEIBO")
        return False


    def logout(self):
        # self.getInMyPage()
        self.tapAccountManage(tologin=False)
        logger.info("点击【退出】")
        return self.waitEleClick(MP.ACCOUNTLOGOUT)

    def getInPersonInfo(self):
        self.waitEleClick(MP.NICKNAMERE)
        cancel = self.waitElePresents(MP.EDITINFOCANCEL)
        if cancel:
            logger.info("点击【取消】")
            # self.savePNG("编辑个人资料cancel")
            cancel.click()
        self.waitEleClick(MP.NICKNAMERE)
        logger.info("点击【编辑个人资料】")
        self.waitEleClick(MP.EDITINFO)
        if self.waitEleClick(MP.SAVE):
            logger.info("点击【保存】")
            return True
        else:
            self.savePNG("点击【保存】失败")
            logger.info("点击【保存】失败")
            return False


    def getInAccountManage(self):
        if self.waitEleClick(MP.ACCOUNTMANAGE):
            if self.waitElePresents(MP.ACCOUNTID):
                logger.info("进入到【账号管理】成功")
                # self.savePNG("账号管理页面")
                return self.getBack()
        self.savePNG("进入到【账号管理】失败")
        logger.info("进入到【账号管理】失败")
        return False

    def getInMyWallet(self):
        if self.waitEleClick(MP.MYWALLET):
            if self.waitElePresents(MP.RECHARGERECORD):
                logger.info("进入到【我的钱包】成功")
                # self.savePNG("我的钱包页面")
                return self.getBack()
        self.savePNG("进入到【我的钱包】失败")
        logger.info("进入到【我的钱包】失败")
        return False


    def getInDongManMsg(self):
        if self.waitEleClick(MP.MESSAGE):
            if self.waitElePresents(MP.MESSAGETITLE):
                logger.info("进入到【公告事项】成功")
                # self.savePNG("公告事项")
                return self.getBack()
        self.savePNG("进入到【公告事项】失败")
        logger.info("进入到【公告事项】失败")
        return False

    def getInPushSetup(self):
        if self.waitEleClick(MP.ALARM):
            if self.waitElePresents(MP.NEWONLINE):
                logger.info("进入到【推送设置】成功")
                # self.savePNG("推送设置")
                return self.waitEleClick(MP.BACK)
        self.savePNG("进入到【推送设置】失败")
        logger.info("进入到【推送设置】失败")
        return False

    def getInFeedback(self):
        if self.waitEleClick(MP.FEEDBACK):
            if self.waitElePresents(MP.FEEDBACKSUBMIT):
                logger.info("进入到【意见反馈】成功")
                # self.savePNG("意见反馈")
                return self.waitEleClick(MP.BACK)
        self.savePNG("进入到【意见反馈】失败")
        logger.info("进入到【意见反馈】失败")
        return False

    def getInAPPInfo(self):
        if self.waitEleClick(MP.APPINFO):
            if self.waitElePresents(MP.APPHELP):
                logger.info("进入到【APP信息】成功")
                # self.savePNG("APP信息")
                return self.waitEleClick(MP.BACK)
        self.savePNG("进入到【APP信息】失败")
        logger.info("进入到【APP信息】失败")
        return False




