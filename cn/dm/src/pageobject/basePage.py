#coding = utf-8

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
By.IOS_PREDICATE = MobileBy.IOS_PREDICATE

class BasePage():

    ##IOS
    UPDATENEXT = (By.ACCESSIBILITY_ID,"下次再说")
    BTNBACK = (By.ACCESSIBILITY_ID,"btnBack")
    SYSALLOW = (By.ACCESSIBILITY_ID,"允许")
    SYSCONFIRM = (By.ACCESSIBILITY_ID,"确定")
    H5CLOSE = (By.ACCESSIBILITY_ID,"Close")
    FIRSTCLOSE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == 'Close' and label == 'Close'") ##首次安装app启动的关闭

    UPDATE = (By.ACCESSIBILITY_ID,'daily')
    DISCOVERY = (By.ACCESSIBILITY_ID,'home')
    # MYCARTOON = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value =='我的漫画'")
    MYCARTOON = (By.ACCESSIBILITY_ID,'my')
    MY = (By.ACCESSIBILITY_ID,'more')
    LOGINSUCCESS = (By.ACCESSIBILITY_ID,"登录成功")


    ##LIST
    SUBSCRIBE = (By.ACCESSIBILITY_ID,"关注")
    SHARE = (By.ACCESSIBILITY_ID,"share")
    ADDSCORE = (By.ACCESSIBILITY_ID,"评分")
    SELECTEPISODE = (By.ACCESSIBILITY_ID,"选集")
    PRODUCTIONINTRO = (By.ACCESSIBILITY_ID,"作品介绍")
    LISTBACK = (By.ACCESSIBILITY_ID,"back bt sub")
    STARTREAD = (By.ACCESSIBILITY_ID,"开始阅读")
    CONTINUEREAD = (By.ACCESSIBILITY_ID,"继续阅读")

    ##分享
    SHAREQQ = (By.ACCESSIBILITY_ID,"snsQQDongman")
    SHAREQZONE = (By.ACCESSIBILITY_ID,"snsQZoneDongman")
    SHAREWECHAT = (By.ACCESSIBILITY_ID,"snsWechatDongman")
    SHAREMOMENT = (By.ACCESSIBILITY_ID,"snsMomentDongman")
    SHAREWEIBO = (By.ACCESSIBILITY_ID,"snsWeiboDongman")
    SHAREDOWNLOAD = (By.ACCESSIBILITY_ID,"snsShareDownload")
    SHAREURL = (By.ACCESSIBILITY_ID,"snsUrlDongman")
    SHAREMORE = (By.ACCESSIBILITY_ID,"snsMoreDongman")
    SHARECANCEL = (By.ACCESSIBILITY_ID,"取消")

    ##viewer
    VIEWERBACK = (By.ACCESSIBILITY_ID,"back bt v")
    MOONICON = (By.ACCESSIBILITY_ID,"brightness moon icon")
    TOLIST = (By.ACCESSIBILITY_ID,"list bt vi")
    VIEWERSHARE = (By.ACCESSIBILITY_ID,"share")
    PREVIOUS = (By.ACCESSIBILITY_ID,"list bt b")
    NEXT = (By.ACCESSIBILITY_ID,"list bt f")
    INPUTCOMMENT = (By.ACCESSIBILITY_ID,"请给作品留下评论~")
    COMMENTSUBMIT = (By.ACCESSIBILITY_ID,"发送")
    COMMENTCOUNT = (By.ACCESSIBILITY_ID,"viewer comment")
    COMMENTMORE = (By.ACCESSIBILITY_ID,"viewer_cmt_more.png")
    VIEWERTOTOP = (By.ACCESSIBILITY_ID,"viewer top btn")
    BACK = (By.ACCESSIBILITY_ID,"back bt s")
    VIEWERSUBSCRIBE = (By.ACCESSIBILITY_ID, "关注")
    SCROLLVIEWER = (By.ACCESSIBILITY_ID,"viewerScrollView") ###阅读漫画viewer
    VIEWERLIKEBUTTON = (By.ACCESSIBILITY_ID,"viewer_like_button_icon")
    VIEWERFAVOURITEBUTTON = (By.ACCESSIBILITY_ID,"viewer_favorite_button_icon")
    VIEWERSHAREBUTTON = (By.ACCESSIBILITY_ID,"viewer_share_button_icon")
    SHANGYIHUA = (By.ACCESSIBILITY_ID,"上一话")
    XIAYIHUA = (By.ACCESSIBILITY_ID,"下一话")
    VIEWERPLUSFAVOURITE = (By.ACCESSIBILITY_ID,"viewer_favorDefault")
    LOOKFIRSTEPISODE = (By.ACCESSIBILITY_ID,"看第1话")


    ##搜索
    # INPUTSEARCH = (By.IOS_PREDICATE,"type == 'XCUIElementTypeTextField' and value == '搜索'")
    # SEARCHCANCEL = (By.ACCESSIBILITY_ID,"取消")
    SEARCHHOT = (By.ACCESSIBILITY_ID,"热门搜索")

    ##搜索分类
    # SEARCHLOVE = (By.ACCESSIBILITY_ID,"search_love")
    # SEARCHBOY = (By.ACCESSIBILITY_ID,"search_boy")
    # SEARCHANCIENTCHINA = (By.ACCESSIBILITY_ID,"search_ancientchinese")
    # SEARCHFANTASY = (By.ACCESSIBILITY_ID,"search_fantasy")
    # SEARCHCOMEDY = (By.ACCESSIBILITY_ID,"search_comedy")
    # SEARCHCAMPUS = (By.ACCESSIBILITY_ID,"search_campus")
    # SEARCHMETROPOLIS = (By.ACCESSIBILITY_ID,"search_metropolis")
    # SEARCHHEALING = (By.ACCESSIBILITY_ID,"search_healing")
    # SEARCHSUSPENSE = (By.ACCESSIBILITY_ID,"search_suspense")
    # SEARCHINSPIRATIONAL = (By.ACCESSIBILITY_ID,"search_inspirational")
    # SEARCHFILMADAPTATION = (By.ACCESSIBILITY_ID,"search_filmadaptation")
    # SEARCHTERMINATION = (By.ACCESSIBILITY_ID,"search_termination")

    ##搜索结果
    SEARCHRESUTCOUNT = (By.IOS_PREDICATE,"type == 'XCUIElementTypeOther' and value ENDSWITH '结果'")
    SEARCHRESUT0 = (By.ACCESSIBILITY_ID,"没有搜索结果。")

    ##通用id find



    ##下载
    DOWNLOADCLOSE = (By.ACCESSIBILITY_ID,"关闭")
    DOWNLOADSTART = (By.ACCESSIBILITY_ID,"下载")
    DOWNLOADPICKERWHEEL= (By.CLASS_NAME,"XCUIElementTypePickerWheel")




    BACKRE = (By.IOS_PREDICATE,'type== "XCUIElementTypeButton" and name STARTSWITH "back"')

    SUBSCRIBEUNLOGIN = (By.ACCESSIBILITY_ID, "若想查看我的关注，请先登录。")
    HAVENOTSUBSCRIBE = (By.ACCESSIBILITY_ID,'没有关注的漫画。 添加到我的关注 新的章节更新时，会提醒您。')
    LOGIN = (By.ACCESSIBILITY_ID,"登录")


    ##检索
    SEARCHCANCEL = (By.ACCESSIBILITY_ID,"取消")
    SEARCHINPUT = (By.IOS_PREDICATE,'type== "XCUIElementTypeTextField" and  value == "搜索"')
    SEARCHLOVE = (By.ACCESSIBILITY_ID,"search_love")
    SEARCHBOY = (By.ACCESSIBILITY_ID,"search_boy")
    SEARCHANCIENTCHINESE = (By.ACCESSIBILITY_ID,"search_ancientchinese")
    SEARCHFANTASY = (By.ACCESSIBILITY_ID,"search_fantasy")
    SEARCHCOMEDY = (By.ACCESSIBILITY_ID,"search_comedy")
    SEARCHCAMPUS = (By.ACCESSIBILITY_ID,"search_campus")
    SEARCHMETROPOLIS = (By.ACCESSIBILITY_ID,"search_metropolis")
    SEARCHHEALING = (By.ACCESSIBILITY_ID,"search_healing")
    SEARCHSUSPENSE = (By.ACCESSIBILITY_ID,"search_suspense")
    SEARCHINSPIRATIONAL = (By.ACCESSIBILITY_ID,"search_inspirational")
    SEARCHFILMADAPTATION = (By.ACCESSIBILITY_ID,"search_filmadaptation")
    SEARCHTERMINATION = (By.ACCESSIBILITY_ID,"search_termination")
    SEARCHRESULT = (By.IOS_PREDICATE,'type == "XCUIElementTypeStaticText" and value ENDSWITH "结果"')


    ##
    CONTAINS = [By.IOS_PREDICATE,'name CONTAINS "%s"']
    ENDS = [By.IOS_PREDICATE,'name ENDSWITH "%s"']

    IDTOBE = [By.ACCESSIBILITY_ID,"%s"]