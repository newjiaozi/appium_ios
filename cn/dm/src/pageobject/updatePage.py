#coding=utf-8

from selenium.webdriver.common.by import By
from .basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
By.IOS_PREDICATE = MobileBy.IOS_PREDICATE



class UpdatePage(BasePage):
    SEARCH = (By.ACCESSIBILITY_ID,"card home base search")
    RQBTN = (By.ACCESSIBILITY_ID,"人气") ## 人气
    GZBTN = (By.ACCESSIBILITY_ID,"关注") ## 关注
    TODAY = (By.ACCESSIBILITY_ID,"今天")
    MONDAY = (By.ACCESSIBILITY_ID,"周一")
    TUESDAY = (By.ACCESSIBILITY_ID,"周二")
    WEDNESDAY = (By.ACCESSIBILITY_ID,"周三")
    THURSDAY = (By.ACCESSIBILITY_ID,"周四")
    FRIDAY = (By.ACCESSIBILITY_ID,"周五")
    SATURDAY = (By.ACCESSIBILITY_ID,"周六")
    SUNDAY = (By.ACCESSIBILITY_ID,"周日")
    END = (By.ACCESSIBILITY_ID,"完结")

    CELLSTABLE = (By.IOS_PREDICATE,'type == "XCUIElementTypeTable"')
    BANNERCELL = (By.IOS_PREDICATE,'name BEGINSWITH "PopularBannerCell"')
    NOTICEBANNERCELL = (By.IOS_PREDICATE,'name BEGINSWITH "PopularNoticeBannerCell"')
    FAVOURITEBANNER = (By.IOS_PREDICATE,'name BEGINSWITH "FavoriteBannerCell"')

    BANNERCELLTEXT = "PopularBannerCell"
    NOTICEBANNERCELLTEXT = "PopularNoticeBannerCell"
    FAVOURITEBANNERTEXT = "FavoriteBannerCell"

    ALLEPISODE = (By.ACCESSIBILITY_ID,"全集")
    ADDSUBSCRIBE =  (By.ACCESSIBILITY_ID,"关注")
    CANCELSUBSCRIBE = (By.ACCESSIBILITY_ID,"已关注")
    LIKEIT = (By.ACCESSIBILITY_ID,"赏我个赞吧！")

    TODAY = (By.ACCESSIBILITY_ID,"今天")