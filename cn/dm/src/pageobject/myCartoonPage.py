#coding=utf-8

from selenium.webdriver.common.by import By
from .basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
By.IOS_PREDICATE = MobileBy.IOS_PREDICATE

class MyCartoonPage(BasePage):

    ##
    RECENTLY = (By.ACCESSIBILITY_ID,"最近观看")
    MYSUBSCRIBE = (By.ACCESSIBILITY_ID,"我的关注")
    SAVE30 = (By.ACCESSIBILITY_ID,"临时保存") ## 作者名字
    MYCOMMENT = (By.ACCESSIBILITY_ID,"我的评论") ## 更新日期
    NORECENTLY = (By.ACCESSIBILITY_ID,"还没有看过漫画>.< 看看其他人都在看什么吧~")
    EVERYONEWATCH = (By.ACCESSIBILITY_ID,"大家都在看")
    NOSAVE30 = (By.ACCESSIBILITY_ID,"没有临时保存的漫画。")
    NOCOMMENT = (By.ACCESSIBILITY_ID,"您还没有评论。")
    EDITBTN = (By.ACCESSIBILITY_ID,"btn edit")
    NOMYSUBSCRIBE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeTable' and name =='没有关注的漫画。 添加到我的关注 新的章节更新时，会提醒您。'")
    NOMYSUBSCRIBETEXT = '没有关注的漫画。 添加到我的关注 新的章节更新时，会提醒您。'
    DELETEALL = (By.ACCESSIBILITY_ID,"全部删除")



    ##最近观看
    RECENTLOOKEPISODENO = (By.IOS_PREDICATE,"type =='XCUIElementTypeStaticText' and value STARTSWITH '#'")
    # EVERYONELOOKING = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value == ''大家都在看")
    EVERYONEWATCHCOUNT = (By.ACCESSIBILITY_ID,"myWebtoon_star.png")
    EVERYONEWATCH = (By.ACCESSIBILITY_ID,"大家都在看")

    ##我的关注
    MYSUBSCRIBEUPDATETIME = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value ENDSWITH '更新'")
    MYSBUSCRIBEUNLOGIN = (By.ACCESSIBILITY_ID,"若想查看我的关注，请先登录。")

    ##临时保存
    SAVEDATA = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and value ENDSWITH '下载完毕'")

    ##我的评论
    COMMENTEPISODENO = (By.IOS_PREDICATE,"type =='XCUIElementTypeStaticText' and value CONTAINS '#'")
    COMMENTUNLOGIN = (By.ACCESSIBILITY_ID,'若想查看评论，请先登录。')
    COMMENTDATA = "哇塞，这个太太太～～"
    COMMENTDELETEICON = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name BEGINSWITH '删除'")
    COMMENTDELETETEXT = (By.ACCESSIBILITY_ID,"删除")

