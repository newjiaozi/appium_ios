#coding=utf-8

from selenium.webdriver.common.by import By
from .basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
By.IOS_PREDICATE = MobileBy.IOS_PREDICATE


class MyPage(BasePage):

    ## 首页

    USERNAME = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value ENDSWITH '账号'")
    ACCOUNTMANAGE = (By.ACCESSIBILITY_ID,"账号管理")
    MYWALLET = (By.ACCESSIBILITY_ID,"我的钱包") ## 我的钱包
    MESSAGE= (By.ACCESSIBILITY_ID,'咚漫消息')##
    ALARM = (By.ID,"推送设置")
    FEEDBACK = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value == '写反馈'")
    APPINFO = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value == 'APP信息'")



    ## 验证码登录页面
    TOPASSLOGIN = (By.ACCESSIBILITY_ID,"密码登录") ##点击切换到密码登录
    CLOSELOGIN = (By.ACCESSIBILITY_ID,"invalidLogin") ##关闭登录页面
    WECHATLOGIN = (By.ACCESSIBILITY_ID,"wechatLogin")
    QQLOGIN = (By.ACCESSIBILITY_ID,"qqLogin")
    WEIBOLOGIN = (By.ACCESSIBILITY_ID,"weiboLogin")




    ## 密码登录页面
    TOCODELOGIN = (By.ACCESSIBILITY_ID,"验证码登录")
    INPUTUSER = (By.IOS_PREDICATE,"type =='XCUIElementTypeTextField' and value =='请输入手机号/邮箱'")
    INPUTPASS = (By.IOS_PREDICATE,"type=='XCUIElementTypeSecureTextField' and value=='请输入密码'")
    LOGINCONFIRM = (By.ACCESSIBILITY_ID,"登录")
    RESETPASS = (By.ACCESSIBILITY_ID,"密码重置")

    ##密码重置
    RESETBYMOBILE = (By.ACCESSIBILITY_ID,"手机密码重置")
    RESETBYEMAIL = (By.ACCESSIBILITY_ID,"邮箱密码重置")
    RESETCANCEL = (By.ACCESSIBILITY_ID,"取消")

    ##编辑个人资料
    EDITINFO = (By.ACCESSIBILITY_ID,"编辑个人资料")
    EDITINFOCANCEL = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name =='取消'")
    NICKNAME = (By.IOS_PREDICATE,"type == 'XCUIElementTypeTextField' and value == '手机账号'")
    NICKNAMERE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value ENDSWITH '账号'")

    SELECTGENDER = (By.ACCESSIBILITY_ID,"请选择性别")
    SELECTBIRTH = (By.ACCESSIBILITY_ID,"请选择生日")
    SAVE = (By.ACCESSIBILITY_ID,"保存")
    SAVECLOSE = (By.XPATH,'//XCUIElementTypeApplication[@name="咚漫"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
    SAVETIPS = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value ENDWITH '下周再来试试吧'")
    PICKERWHEEL = (By.IOS_PREDICATE,"type=='XCUIElementTypePickerWheel and visible==True") ## PICKER WHEEL
    CONFIRMSELECT = (By.ACCESSIBILITY_ID,"确定")
    PICKERWHEELBIRTHDAY = (By.IOS_PREDICATE,"type=='XCUIElementTypePickerWheel and visible==True and value=='2019年'") ## PICKER WHEEL


    ##账号管理
    ACCOUNTTITLE = (By.ACCESSIBILITY_ID,"账号管理")
    ACCOUNTNICKNAMEMOBILE = (By.ACCESSIBILITY_ID,"手机账号")
    ACCOUNTIDRE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value MATCHES '^咚漫ID: \d{7,8}$'")
    ACCOUNTRESETPASS = (By.ACCESSIBILITY_ID,"密码重置")
    ACCOUNTEMAILNULL = (By.ACCESSIBILITY_ID,"认证邮箱，接收作品最新信息")
    ACCOUNTMOBILENULL = (By.ACCESSIBILITY_ID,"认证手机，接收作品最新信息")
    ACCOUNTLOGOUT = (By.IOS_PREDICATE,"type== 'XCUIElementTypeButton' and name == '退出'")
    ACCOUNTMOBILE = (By.ACCESSIBILITY_ID,"13683581996")
    ACCOUNTMOBILERE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value MATCHES '^\d{11}$'")
    ACCOUNTEMAILRE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value MATCHES '^.*?@.*?\.com$")
    ACCOUNTEMAIL = (By.ACCESSIBILITY_ID,"newjiaozi@163.com")
    ACCOUNTLOGOUT = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name =='退出'")

    ACCOUNTWEIBOTAG = (By.ACCESSIBILITY_ID,"weiboLogin")
    ACCOUNTWECHATTAG = (By.ACCESSIBILITY_ID,"wechatLogin")
    ACCOUNTQQTAG = (By.ACCESSIBILITY_ID,"qqLogin")
    ACCOUNTMOBILETAG = (By.IOS_PREDICATE,"type =='XCUIElementTypeStaticText' and value MATCHES '^\d{3}\*{4}\d{4}$'")
    ACCOUNTEMAILTAG = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value MATCHES '^.*?@.*?\.com$")

    ##邮箱认证

    ##更改邮箱认证
    CHANGEEMAIL = (By.ACCESSIBILITY_ID,"修改")
    ##手机认证

    ##更改手机好认证
    CHANGEMOBILE = (By.ACCESSIBILITY_ID,"更换手机号")
    CHANGEMOBILESENDCODE = (By.ACCESSIBILITY_ID,"发送验证码")
    BACK = (By.ACCESSIBILITY_ID,"recommend back btn") ##返回

    ##快捷登录
    QUICKLOGIN = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '快捷登录'")
    OTHERLOGIN = (By.IOS_PREDICATE,"type=='XCUIElementTypeStaticText' and value =='其他方式登录'")

    ##充值：
    PURCHASEHISTORY = (By.ACCESSIBILITY_ID,"消费记录")
    RECHARGERECORD = (By.ACCESSIBILITY_ID,"充值记录")

    ##公告
    MESSAGETITLE = (By.ACCESSIBILITY_ID,"公告事项")

    ##推送设置：
    NEWONLINE = (By.ACCESSIBILITY_ID,"新作品上线")

    ##意见反馈
    FEEDBACKSUBMIT = (By.ACCESSIBILITY_ID,"社交帐号")

    ##APP信息
    APPHELP = (By.ACCESSIBILITY_ID,"帮助")
