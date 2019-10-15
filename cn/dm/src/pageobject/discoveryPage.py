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

    # SEARCH = (By.ACCESSIBILITY_ID,"search") ##搜索图标
    BIGBANNER = (By.IOS_PREDICATE,"type == 'XCUIElementTypeImage' and name BEGINSWITH 'TopBanner'") ## banner scroll
    BIGBANNERFORMAT = [By.IOS_PREDICATE,"type == 'XCUIElementTypeImage' and name == '%s'"] ## banner scroll
    # BIGBANNERPARENT = (By.XPATH,'//XCUIElementTypeImage[@name="TopBanner5"]')
    # NEWTITLE = (By.ACCESSIBILITY_ID,"新作") ## 新作
    RANK = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '排行'") ## 排行
    RECOMMEND = (By.ACCESSIBILITY_ID,"个性推荐") ## 推荐
    GENRE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '分类'") ## 分类

    DONMANRECOMMEND = (By.ACCESSIBILITY_ID,"咚漫推荐")  ##咚漫推荐
    NEWTITLEDEBUT = (By.ACCESSIBILITY_ID,"咚漫推荐, 更多") ##咚漫推荐, 更多


    JIAZUOQXK = (By.ACCESSIBILITY_ID,"佳作抢先看") ##佳作抢先看
    NEWCOME = (By.ACCESSIBILITY_ID,"新作登场")  ##新作登场

    # GENRE = (By.ACCESSIBILITY_ID,"分类")  ##分类
    GENRETOP = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '分类'")
    RANKTOP = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '排行'")
    MAINTOP = (By.ACCESSIBILITY_ID,"推荐")


    ZHUTIZHUANQU =(By.ACCESSIBILITY_ID,"主题专区")
    CAINIXIHUAN = (By.ACCESSIBILITY_ID,"猜你喜欢")


    ## 榜


    ##新作
    NEWBACK = (By.ACCESSIBILITY_ID,"back bt s")
    NEWRECOMMEND = (By.ACCESSIBILITY_ID,"新作推荐")

    ##排行
    RANKMORE = (By.XPATH,'//XCUIElementTypeCell[@name="HomeRankMoreCell"]/XCUIElementTypeStaticText[@name="更多"]')
    RANKMORETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="HomeRankMoreCell"]/XCUIElementTypeStaticText[@name="%s"]']

    WEEKRANK = (By.ACCESSIBILITY_ID,"上升榜") ## 上升榜
    NEWRANK = (By.ACCESSIBILITY_ID,"新作榜") ## 新榜
    TOTALRANK = (By.ACCESSIBILITY_ID,"总榜") ## 总榜
    COLLECTIONVIEW = (By.CLASS_NAME,"XCUIElementTypeCollectionView")
    ##排行榜内部
    WEEKRANKPAGE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '上升榜'")
    NEWRANKPAGE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '新作榜'")
    TOTALRANKPAGE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeButton' and name == '总榜'")
    TOTALRANKTITLECELL = [By.ACCESSIBILITY_ID,"rankTotalListCell%s"]
    TOTALRANKTITLE = [By.XPATH,'//XCUIElementTypeCell[@name="rankTotalListCell%s"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[@name="%s"]']
    NEWRANKTITLECELL = [By.ACCESSIBILITY_ID,"rankNewListCell%s"]
    NEWRANKTITLE = [By.XPATH,'//XCUIElementTypeCell[@name="rankNewListCell%s"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[@name="%s"]']
    WEEKRANKTITLECELL = [By.ACCESSIBILITY_ID,"rankWeekListCell%s"]
    WEEKRANKTITLE = [By.XPATH,'//XCUIElementTypeCell[@name="rankWeekListCell%s"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[@name="%s"]']
    ANYRANKTITLE = [By.XPATH,'//XCUIElementTypeCell[@name="%s"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[@name="%s"]']

    ## 咚漫推荐
    DMRECOMMEND = (By.ACCESSIBILITY_ID,"咚漫推荐")
    DMMORE = (By.XPATH,'//XCUIElementTypeCell[@name="HomeRecommendMoreCell"]/XCUIElementTypeStaticText[@name="更多"]')
    DMMORETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="HomeRecommendMoreCell"]/XCUIElementTypeStaticText[@name="%s"]']
    DMMORECELL = (By.ACCESSIBILITY_ID,"HomeRecommendMoreCell")

    ##佳作抢先看
    PRIORITY = (By.ACCESSIBILITY_ID,"佳作抢先看")
    PRIORITYMORE =  (By.XPATH,'//XCUIElementTypeCell[@name="HomePriorityMoreCell"]/XCUIElementTypeStaticText[@name="更多"]')
    PRIORITYMORETITLE =  [By.XPATH,'//XCUIElementTypeCell[@name="HomePriorityMoreCell"]/XCUIElementTypeStaticText[@name="%s"]']
    PRIORITYMORECELL = (By.ACCESSIBILITY_ID,"HomePriorityMoreCell")



    ##新作登
    NEWTITLE = (By.ACCESSIBILITY_ID,"新作登场")
    NEWTITLELOGIN = (By.ACCESSIBILITY_ID,"新作推荐")
    NEWTITLEMORE = (By.XPATH,'//XCUIElementTypeCell[@name="HomeNewTitleMoreCell"]/XCUIElementTypeStaticText[@name="更多"]')
    NEWTITLEMORETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="HomeNewTitleMoreCell"]/XCUIElementTypeStaticText[@name="%s"]']
    NEWTITLEMORECELL = (By.ACCESSIBILITY_ID,"HomeNewTitleMoreCell")


    ##barbanner
    BARBANNER0 = (By.ACCESSIBILITY_ID,"BarBanner1")
    BARBANNER1 = (By.ACCESSIBILITY_ID,"BarBanner2")
    # PARENTBARBANNER0 = (By.XPATH,'//XCUIElementTypeImage[@name="BarBanner0"]/..')
    # PARENTBARBANNER1 = (By.XPATH,'//XCUIElementTypeImage[@name="BarBanner1"]/..')

    ##分类
    GENREMORE = (By.XPATH,'//XCUIElementTypeCell[@name="HomeGenreMoreCell"]/XCUIElementTypeStaticText[@name="更多"]')
    GENREMORETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="HomeGenreMoreCell"]/XCUIElementTypeStaticText[@name="%s"]']
    GENREMORECELL = (By.ACCESSIBILITY_ID,"HomeGenreMoreCell")



    ##主题专区
    THEME = (By.ACCESSIBILITY_ID,"主题专区")
    THEMEMORE = (By.XPATH,'//XCUIElementTypeCell[@name="HomeThemeMoreCell"]/XCUIElementTypeStaticText[@name="更多"]')
    THEMEMORETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="HomeThemeMoreCell"]/XCUIElementTypeStaticText[@name="%s"]']
    THEMEMORECELL = (By.ACCESSIBILITY_ID,"HomeThemeMoreCell")
    MOREDATAPREDICATE = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and name == '更多'")


    ##猜你喜欢
    FAVOURITE = (By.ACCESSIBILITY_ID,"猜你喜欢")
    FAVOURITEMORE = (By.ACCESSIBILITY_ID,"HomeFavoriteMoreCell")


    ##top

    DISCOVERYTOP = (By.ACCESSIBILITY_ID,"home btn Top")

    ##个性推荐
    RECOMMENDICON = (By.ACCESSIBILITY_ID,"recommend setting icon")
    RECOMMENDBACK = (By.ACCESSIBILITY_ID,"recommend back btn")
    RECOMMENDTITLE = (By.ACCESSIBILITY_ID,"推荐")

    ##最近在追
    RECENTLY = (By.ACCESSIBILITY_ID,"最近在追")
    RECENTLYMORE = (By.ACCESSIBILITY_ID,"HomeRecentReadCell")


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
    GENRESEARCH = (By.ACCESSIBILITY_ID,"genre search btn")

    ## 排序
    SORTBYTIME = (By.ACCESSIBILITY_ID,"按更新时间")
    SORTBYLIKE = (By.ACCESSIBILITY_ID,"按点赞数")
    SORTBYRANK = (By.ACCESSIBILITY_ID,"按人气")
    SORTCANCEL = (By.ACCESSIBILITY_ID,"取消")

    ##自定义菜单

    FINISHTITLE = (By.ACCESSIBILITY_ID,"完结佳作")
    GENRERANK = (By.IOS_PREDICATE,"type == 'XCUIElementTypeStaticText' and name ENDSWITH '类排行'")


    ###登录
    DISCOVERYLOGINBANNER = (By.ACCESSIBILITY_ID,"立即登录，玩转属于你自己的咚漫！")
    DISCOVERYLOGINBANNERPARENT = (By.ACCESSIBILITY_ID,'//XCUIElementTypeStaticText[@name="立即登录，玩转属于你自己的咚漫！"]/..')


    ##自定义菜单
    ###分类排行
    CUSTOMIZEMENUBANNER = (By.ACCESSIBILITY_ID,"")

    CUSTOMIZEMENUGENRERANK = (By.ACCESSIBILITY_ID,"genreListCell")
    CUSTOMIZEMENUGENRERANKTEXT = [By.ACCESSIBILITY_ID,"%s类排行"]

    CUSTOMIZEMENUGENRERANKMORE = (By.XPATH,'//XCUIElementTypeCell[@name="genreListCell"]/XCUIElementTypeStaticText[@name="更多"]')
    CUSTOMIZEMENUGENRERANKTITLE = [By.XPATH,'//XCUIElementTypeCell[@name="genreListCell"]/XCUIElementTypeStaticText[@name="%s"]']

    ## 完结佳作
    CUSTOMIZEMENUFINISH = (By.ACCESSIBILITY_ID,"finishGenreListCell")
    CUSTOMIZEMENUFINISHTEXT = (By.ACCESSIBILITY_ID,"完结佳作")
    CUSTOMIZEMENUFINISHMORE = (By.XPATH,'//XCUIElementTypeCell[@name="finishGenreListCell"]/XCUIElementTypeStaticText[@name="更多"]')
    CUSTOMIZEMENUFINISHTITLE = [By.XPATH,'//XCUIElementTypeCell[@name="finishGenreListCell"]/XCUIElementTypeStaticText[@name="%s"]']

    ## 自定义菜单
    CUSTOMIZEMENUMODULE = [By.ACCESSIBILITY_ID,"%sModuleListCell"]
    CUSTOMIZEMENUMODULEMORE = [By.XPATH,'//XCUIElementTypeCell[@name="%sModuleListCell"]/XCUIElementTypeStaticText[@name="更多"]']
    CUSTOMIZEMENUMODULETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="%sModuleListCell"]/XCUIElementTypeStaticText[@name="%s"]']