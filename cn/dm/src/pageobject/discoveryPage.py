#coding=utf-8

from selenium.webdriver.common.by import By
from .basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
By.IOS_PREDICATE = MobileBy.IOS_PREDICATE



class DiscoveryPage(BasePage):


    ##ios
    # DISCOVERYRQ = (By.ACCESSIBILITY_ID,"人气")
    # DISCOVERYSUBSCRIBE = (By.ACCESSIBILITY_ID,"关注")

    SEARCH = (By.ACCESSIBILITY_ID,"search") ##搜索图标
    BIGBANNER = (By.IOS_PREDICATE,"type == 'XCUIElementTypeImage' and name BEGINSWITH 'TopBanner'") ## banner scroll
    # NEWTITLE = (By.ACCESSIBILITY_ID,"新作") ## 新作
    RANK = (By.ACCESSIBILITY_ID,"排行") ## 排行
    RECOMMEND = (By.ACCESSIBILITY_ID,"个性推荐") ## 推荐
    GENRE = (By.ID,"分类") ## 分类

    DONMANRECOMMEND = (By.ACCESSIBILITY_ID,"咚漫推荐")  ##咚漫推荐
    NEWTITLEDEBUT = (By.ACCESSIBILITY_ID,"咚漫推荐, 更多") ##咚漫推荐, 更多


    JIAZUOQXK = (By.ACCESSIBILITY_ID,"佳作抢先看") ##佳作抢先看
    NEWCOME = (By.ACCESSIBILITY_ID,"新作登场")  ##新作登场

    GENRE = (By.ACCESSIBILITY_ID,"分类")  ##分类

    ZHUTIZHUANQU =(By.ACCESSIBILITY_ID,"主题专区")
    CAINIXIHUAN = (By.ACCESSIBILITY_ID,"猜你喜欢")


    ## 榜
    WEEKRANK = (By.ACCESSIBILITY_ID,"上升榜") ## 上升榜
    NEWRANK = (By.ACCESSIBILITY_ID,"新作榜") ## 新榜
    TOTALRANK = (By.ACCESSIBILITY_ID,"总榜") ## 总榜


    ##新作
    NEWBACK = (By.ACCESSIBILITY_ID,"back bt s")
    NEWRECOMMEND = (By.ACCESSIBILITY_ID,"新作推荐")

    ##排行
    RANKMORE = (By.ACCESSIBILITY_ID,"HomeRankMoreCell")
    UPRANKTITLE = (By.ACCESSIBILITY_ID,"上升榜")
    NEWRANKTITLE = (By.ACCESSIBILITY_ID,"新作榜")
    SUMRANKTITLE = (By.ACCESSIBILITY_ID,"总榜")
    COLLECTIONVIEW = (By.CLASS_NAME,"XCUIElementTypeCollectionView")

    ## 咚漫推荐
    DMRECOMMEND = (By.ACCESSIBILITY_ID,"咚漫推荐")
    DMMORE = (By.ACCESSIBILITY_ID,"HomeRecommendMoreCell")

    ##佳作抢先看
    PRIORITY = (By.ACCESSIBILITY_ID,"佳作抢先看")
    PRIORITYMORE = (By.ACCESSIBILITY_ID,"HomePriorityMoreCell")

    ##新作登场
    NEWTITLE = (By.ACCESSIBILITY_ID,"新作登场")
    NEWTITLEMORE = (By.ACCESSIBILITY_ID,"HomeNewTitleMoreCell")



    ##barbanner
    BARBANNER0 = (By.ACCESSIBILITY_ID,"BarBanner0")
    BARBANNER1 = (By.ACCESSIBILITY_ID,"BarBanner1")

    ##分类
    GENREMORE = (By.ACCESSIBILITY_ID,"HomeGenreMoreCell")


    ##主题专区
    THEME = (By.ACCESSIBILITY_ID,"主题专区")
    THEMEMORE = (By.ACCESSIBILITY_ID,"HomeThemeMoreCell")


    ##猜你喜欢
    FAVOURITE = (By.ACCESSIBILITY_ID,"猜你喜欢")
    FAVOURITEMORE = (By.ACCESSIBILITY_ID,"HomeFavoriteMoreCell")

    ##个性推荐
    RECOMMENDICON = (By.ACCESSIBILITY_ID,"recommend setting icon")
    RECOMMENDBACK = (By.ACCESSIBILITY_ID,"recommend back btn")
    RECOMMENDTITLE = (By.ACCESSIBILITY_ID,"推荐")


    ##分类
    GENRETITLE = (By.ACCESSIBILITY_ID,"分类")
    GENRESORT = (By.ACCESSIBILITY_ID,"sort")
    GENRELIANAI = (By.ACCESSIBILITY_ID,"恋爱")
    GENRESHAONIAN = (By.ACCESSIBILITY_ID,"少年")
    GENREGUFENG = (By.ACCESSIBILITY_ID,"古风")
    GENREQIHUAN = (By.ACCESSIBILITY_ID,"奇幻")
    GENREGAOXIAO = (By.ACCESSIBILITY_ID,"搞笑")
    GENREXIAOHUAN = (By.ACCESSIBILITY_ID,"校园")
    GENREDUSHI = (By.ACCESSIBILITY_ID,"都市")
    GENREZHIYU = (By.ACCESSIBILITY_ID,"治愈")
    GENREXUANYI = (By.ACCESSIBILITY_ID,"悬疑")
    GENRELIZHI = (By.ACCESSIBILITY_ID,"励志")
    GENREYINGSHIHUA = (By.ACCESSIBILITY_ID,"影视化")
    GENREWANJIE = (By.ACCESSIBILITY_ID,"完结")

    ## 排序
    SORTBYTIME = (By.ACCESSIBILITY_ID,"按更新时间")
    SORTBYLIKE = (By.ACCESSIBILITY_ID,"按点赞数")
    SORTBYRANK = (By.ACCESSIBILITY_ID,"按人气")
    SORTCANCEL = (By.ACCESSIBILITY_ID,"取消")





