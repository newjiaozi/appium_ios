#coding = utf-8

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
By.IOS_PREDICATE = MobileBy.IOS_PREDICATE
By.IMAGE = MobileBy.IMAGE

class BasePage():

    ##IOS
    UPDATENEXT = (By.ACCESSIBILITY_ID,"下次再说")
    BTNBACK = (By.ACCESSIBILITY_ID,"btnBack")
    SYSALLOW = (By.ACCESSIBILITY_ID,"允许")
    SYSALLOWEN = (By.ACCESSIBILITY_ID,"Allow")
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
    # LISTEPISODE = [By.XPATH,'//XCUIElementTypeTable/XCUIElementTypeCell[%d]/XCUIElementTypeStaticText[@name="%s"]']
    LISTEPISODETITLE = [By.XPATH,'//XCUIElementTypeCell[@name="episodeCell%s"]/XCUIElementTypeStaticText[@name="%s"]'] ##
    LISTBOTTOM = [By.XPATH,'//XCUIElementTypeOther[@name="bottomView"]/XCUIElementTypeStaticText[@name="%s"]'] ##开始阅读，继续阅读
    LISTBOTTOMID = (By.ACCESSIBILITY_ID,"bottomView")##开始阅读，继续阅读
    LISTEPISODECELL = [By.ACCESSIBILITY_ID,"episodeCell%s"] ##

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
    # SCROLLVIEWER = (By.ACCESSIBILITY_ID,"viewerScrollView") ###阅读漫画viewer
    SCROLLVIEWER = (By.IOS_PREDICATE,"type == 'XCUIElementTypeScrollView' and name == 'viewerScrollView'")
    VIEWERLIKEBUTTON = (By.ACCESSIBILITY_ID,"viewer_like_button_icon")
    VIEWERFAVOURITEBUTTON = (By.ACCESSIBILITY_ID,"viewer_favorite_button_icon")
    VIEWERSHAREBUTTON = (By.ACCESSIBILITY_ID,"viewer_share_button_icon") ##分享
    VIEWERSHAREBUTTONTEXT = (By.ACCESSIBILITY_ID,"分享") ##分享
    SHANGYIHUA = (By.ACCESSIBILITY_ID,"上一话")
    XIAYIHUA = (By.ACCESSIBILITY_ID,"下一话")
    VIEWERPLUSFAVOURITE = (By.ACCESSIBILITY_ID,"viewer_favorDefault")
    LOOKFIRSTEPISODE = (By.ACCESSIBILITY_ID,"看第1话")
    LOADINGTEXT = (By.ACCESSIBILITY_ID,"提示! 临时保存该漫画的话，可以更加快捷的欣赏哦！") ##可见


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
    DOWNLOADPICKERWHEELFROM  = (By.XPATH,'//XCUIElementTypeApplication[@name="咚漫"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypePicker[1]/XCUIElementTypePickerWheel')
    DOWNLOADPICKERWHEELTO  = (By.XPATH,'//XCUIElementTypePicker[2]/XCUIElementTypePickerWheel')
    # DOWNLOADSTARTENDTITLENAME = [By.XPATH,'//XCUIElementTypeStaticText[@name="%s%s"]']
    DOWNLOADSTARTENDTITLENAME = [By.IOS_PREDICATE,'type== "XCUIElementTypeStaticText" and name == "%s %s"']
    DOWNLOAD100 = (By.IOS_PREDICATE,'type== "XCUIElementTypeStaticText" and name ENDSWITH "%"')

    BACKRE = (By.IOS_PREDICATE,'type== "XCUIElementTypeButton" and name STARTSWITH "back"')

    SUBSCRIBEUNLOGIN = (By.ACCESSIBILITY_ID, "若想查看我的关注，请先登录。")
    # HAVENOTSUBSCRIBE = (By.ACCESSIBILITY_ID,'没有关注的漫画。 添加到我的关注 新的章节更新时，会提醒您。')
    HAVENOTSUBSCRIBE = (By.IOS_PREDICATE,'type == "XCUIElementTypeStaticText" and name STARTSWITH "没有关注的漫画"')
    LOGIN = (By.ACCESSIBILITY_ID,"登录")


    ##检索
    SEARCHCANCEL = (By.ACCESSIBILITY_ID,"取消")
    SEARCHINPUT = [By.IOS_PREDICATE,'type== "XCUIElementTypeTextField" and  value == "%s"']
    SEARCHRESULT = [By.IOS_PREDICATE,'type== "XCUIElementTypeStaticText" and  name == "%s" and visible == 1']
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
    # SEARCHBTN =  (By.ACCESSIBILITY_ID,"home Search") ##发现页放大镜
    SEARCHBTN = (By.IOS_PREDICATE,'type == "XCUIElementTypeButton" and name == "home Search"')
    SEARCHLOOK = (By.ACCESSIBILITY_ID,"search look")

    ##
    CONTAINS = [By.IOS_PREDICATE,'name CONTAINS "%s"']
    ENDS = [By.IOS_PREDICATE,'name ENDSWITH "%s"']
    STARTS = [By.IOS_PREDICATE, 'name STARTSWITH "%s"']
    IDTOBE = [By.ACCESSIBILITY_ID,"%s"]
    PREDICATESTATICTEXTNAMEEQUAL = [By.IOS_PREDICATE,'type == "XCUIElementTypeStaticText" and name == "%s"']
    BYIMAGE = [By.IMAGE,"%s"]


    # ADDALARM = (By.ACCESSIBILITY_ID,"添加小咚提醒")
    ADDALARM = (By.IOS_PREDICATE,'type == "XCUIElementTypeStaticText" and value ENDSWITH "凌晨更新,记得来追"')


    ##最新话底部弹窗
    ALERTPOPUPCLOSE = (By.ACCESSIBILITY_ID,"viewer_recmd_close.png")
    ALERTPOPUPDISPLAY = (By.ACCESSIBILITY_ID,"已经追完最新话啦")
    ALERTALLEPISODE = (By.ACCESSIBILITY_ID,"全集")
    ALERTADDFAVOURITE = (By.ACCESSIBILITY_ID,"关注")
    ALERTNEXTEPISODE = (By.ACCESSIBILITY_ID,"下一话")
    ALERTTIPS = (By.IOS_PREDICATE,'type == "XCUIElementTypeStaticText" and value ENDSWITH "的粉丝还在看这个漫画!"')


    ##预览
    PREVIEWPOPUPCLOSE = (By.ACCESSIBILITY_ID,"viewer_recmd_close.png")
    PREVIEWPOPUPDISPLAY = (By.ACCESSIBILITY_ID,"已更新至第18话")
    PREVIEWALLEPISODE = (By.ACCESSIBILITY_ID,"全集")
    PREVIEWADDFAVOURITE = (By.ACCESSIBILITY_ID,"关注")
    PREVIEWNEXTEPISODE = (By.ACCESSIBILITY_ID,"下一话")
    ##预览下滑之后出现的导航上的元素
    PREVIEWTOLIST = (By.ACCESSIBILITY_ID,"viewer recmd epList btn")
    PREVIEWCLOSE = (By.ACCESSIBILITY_ID,"viewer rcmd navClose") ##	//XCUIElementTypeButton[@name="viewer rcmd navClose"]

    #### 作品介绍下的固定文案
    ASSOCIATIONANNOUNCEMENT = (By.ACCESSIBILITY_ID,"社团公告")
    INTRODUCTION = (By.ACCESSIBILITY_ID,"故事简介")
    ACTIVITYZONE = (By.ACCESSIBILITY_ID,"活动专区")

    ##分类页面的顶部筛选文字
    GENREPAGETEXTFIRST = ("全部","恋爱","少年","古风","奇幻","搞笑","校园","都市","治愈","悬疑","励志","影视化")
    GENREPAGETEXTSECOND = ("全部","连载","完结")
    GENREPAGETEXTTHIRD = ("人气","最新")

    # GENREMAINPAGETEXT = ("恋爱","少年","古风","奇幻","搞笑","校园","都市","治愈","悬疑","励志","影视化","完结")
    GENREMAINPAGETEXT = ("恋爱","少年","古风","奇幻","搞笑","校园","完结")
    GENREPAGEGENRESELECTFIRST = [By.XPATH,'//XCUIElementTypeOther[@name="topGenreMenu"]/XCUIElementTypeScrollView/XCUIElementTypeButton[@name="%s"]']
    GENREPAGEGENRESELECTSECOND = [By.XPATH,'//XCUIElementTypeCell[@name="bottomGenreView"]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeButton[@name="%s"]']
    GENREPAGEGENRESELECTTHIRD = [By.XPATH,'//XCUIElementTypeCell[@name="bottomGenreView"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeButton[@name="%s"]']

    GENREPAGEGENRESELECTFIRST = (By.ACCESSIBILITY_ID,"topGenreMenu")
    GENREPAGEGENRESELECTSECOND = (By.ACCESSIBILITY_ID,"bottomGenreView")


    GENREPAGEGENRESELECTRENQI = (By.ACCESSIBILITY_ID,"人气")
    GENREPAGEGENRESELECTZUIXIN = (By.ACCESSIBILITY_ID,"最新")


    ###H5分享
    H5SHARE = (By.ACCESSIBILITY_ID,"webShare")

    ##无网络链接
    NONETALERT = (By.ACCESSIBILITY_ID,"无法连接网络。请确认网络连接状态。")
    NONETALERTCLOSE = (By.ACCESSIBILITY_ID,"关闭")
    NONETALERTRETRY = (By.ACCESSIBILITY_ID,"重试")


    ##用户画像
    USERPREFENRENCEGENDERTITLE = (By.ACCESSIBILITY_ID,"小咚想要更懂你")
    USERPREFENRENCEGENDERMALE = (By.ACCESSIBILITY_ID,"gender_male.png")
    USERPREFENRENCEGENDERFEMALE = (By.ACCESSIBILITY_ID,"gender_female.png")
    USERPREFENRENCEAGETITLE = (By.ACCESSIBILITY_ID,"请选择年龄区间")
    USERPREFENRENCEAGE12 = (By.ACCESSIBILITY_ID,"age_12")
    USERPREFENRENCEAGE13 = (By.ACCESSIBILITY_ID,"age_13")
    USERPREFENRENCEAGE16 = (By.ACCESSIBILITY_ID,"age_16")
    USERPREFENRENCEAGE19 = (By.ACCESSIBILITY_ID,"age_19")
    USERPREFENRENCEAGE23 = (By.ACCESSIBILITY_ID,"age_23")
    USERPREFENRENCEAGE26 = (By.ACCESSIBILITY_ID,"age_26")
    USERPREFENRENCEAGE36 = (By.ACCESSIBILITY_ID,"age_36")

    USERPREFENRENCEJUMP = (By.ACCESSIBILITY_ID,"跳过")
    USERPREFENRENCEBACK = (By.ACCESSIBILITY_ID,"recommend back btn")


    USERPREFENRENCEGENRETITLE = (By.ACCESSIBILITY_ID,"最爱的漫画类型（可多选）")
    USERPREFENRENCEGENRBOY = (By.ACCESSIBILITY_ID,"少年")
    USERPREFENRENCEGENRELOVE = (By.ACCESSIBILITY_ID,"恋爱")
    USERPREFENRENCEGENRECHINA = (By.ACCESSIBILITY_ID,"古风")
    USERPREFENRENCEGENREFANTASY = (By.ACCESSIBILITY_ID,"奇幻")
    USERPREFENRENCEGENRECOMEDY = (By.ACCESSIBILITY_ID,"搞笑")
    USERPREFENRENCEGENRESCHOOL = (By.ACCESSIBILITY_ID,"校园")
    USERPREFENRENCEGENREDUSHI = (By.ACCESSIBILITY_ID,"都市")
    USERPREFENRENCEGENREHEALING = (By.ACCESSIBILITY_ID,"治愈")
    USERPREFENRENCEGENREXUANYI = (By.ACCESSIBILITY_ID,"悬疑")
    USERPREFENRENCEGENRELIZHI = (By.ACCESSIBILITY_ID,"励志")
    USERPREFENRENCEGENREFILM = (By.ACCESSIBILITY_ID,"影视化")
    USERPREFENRENCEGENREFINISH = (By.ACCESSIBILITY_ID,"完结")

    USERPREFENRENCEGENRECONFIRM = (By.ACCESSIBILITY_ID,"确定")

    USERPREFENRENCERECOMMENDTITLE = (By.ACCESSIBILITY_ID,"小咚找到了最适合你的的作品！")
    USERPREFENRENCERECOMMENDTODISCOVERY = (By.ACCESSIBILITY_ID,"进入发现页")
    USERPREFENRENCERECOMMENDADDFAVOURITE = (By.ACCESSIBILITY_ID,"一键关注")


    ### 隐私同意
    PRIVACYTITLE = (By.ACCESSIBILITY_ID,"欢迎使用咚漫")
    PRIVACYTEXT = (By.ACCESSIBILITY_ID,"咚漫非常注重您的隐私保护，在开始使用之前，请认真阅读咚漫的《隐私政策》和《用户服务协议》 如果同意以上条款，请点击“同意”开启咚漫。")
    PRIVACYREADLONLY = (By.ACCESSIBILITY_ID,"只浏览")
    PRIVACYAGREE = (By.ACCESSIBILITY_ID,"同意")

    ##我的漫画蒙层
    MYCARTOONMENGCENGRECENTLY  = (By.ACCESSIBILITY_ID,"可观看 最近观看 的漫画")
    MYCARTOONMENGCENGSAVE  = (By.ACCESSIBILITY_ID,"可在 离线状态查看 临时保存的漫画")
    MYCARTOONMENGCENGSUBSCRIBE  = (By.ACCESSIBILITY_ID,"可管理 我的关注和 更新提醒")
    MYCARTOONMENGCENGCOMMENT  = (By.ACCESSIBILITY_ID,"可查看您的所有评论！")
    MYCARTOONMENGCENGCLOSE  = (By.ACCESSIBILITY_ID,"关闭")




    ##登录相关
    ##快捷登录 返回都是btnBack
    QUICKCLOSE = (By.ACCESSIBILITY_ID, "invalidLogin")  ## 右上角的X
    QUICKLOGIN = (By.IOS_PREDICATE, "type == 'XCUIElementTypeButton' and name == '快捷登录'")
    OTHERLOGIN = (By.IOS_PREDICATE, "type=='XCUIElementTypeStaticText' and value =='其他方式登录'")
    QUICKUSERPREFERENCE = (By.IOS_PREDICATE, "type == 'XCUIElementTypeLink' and name == '用户服务协议'")
    QUICKUSERYINSI = (By.IOS_PREDICATE, "type == 'XCUIElementTypeLink' and name == '隐私政策'")
    QUICKCOMPANY = (By.ACCESSIBILITY_ID, "© Dongman Entertainment Corp.")
    ##手机
    QUICKMOBILETITLE = (By.ACCESSIBILITY_ID, "最近使用手机号登录")
    QUICKMOBILEICON = (By.ACCESSIBILITY_ID, "fastLoginPhone")  ## 不可见,手机的小图标
    QUICKMOBILEACCOUNT = (By.ACCESSIBILITY_ID, "136****1996")
    QUICKMOBILEPASSWD = (By.IOS_PREDICATE, "type == 'XCUIElementTypeSecureTextField' and value == '请输入密码'")
    QUICKMOBILEPASSWDTITLE = (By.ACCESSIBILITY_ID, "登录手机账号1368****996")
    ##邮箱
    QUICKEMAILTITLE = (By.ACCESSIBILITY_ID, "最近使用邮箱登录")
    QUICKEMAILICON = (By.ACCESSIBILITY_ID, "fastLoginMail")  ## 不可见,小图标
    QUICKEMAILACCOUNT = (By.ACCESSIBILITY_ID, "84978****@qq.com")
    QUICKEMAILPASSWD = (By.IOS_PREDICATE, "type == 'XCUIElementTypeSecureTextField' and value == '请输入密码'")
    QUICKEMAILPASSWDTITLE = (By.ACCESSIBILITY_ID, "登录邮箱账号84978****@qq.com")
    ##微博
    QUICKWEIBOTITLE = (By.ACCESSIBILITY_ID, "最近使用微博登录")
    QUICKWEIBOICON = (By.ACCESSIBILITY_ID, "fastLoginWeibo")  ## 不可见,小图标
    QUICKWEIBOACCOUNT = (By.ACCESSIBILITY_ID, "微博账号")
    ##微信
    QUICKWECHATTITLE = (By.ACCESSIBILITY_ID, "最近使用微信登录")
    QUICKWECHATICON = (By.ACCESSIBILITY_ID, "fastLoginWechat")  ## 不可见,小图标
    QUICKWECHATACCOUNT = (By.ACCESSIBILITY_ID, "微信账号")
    ##QQ
    QUICKQQTITLE = (By.ACCESSIBILITY_ID, "最近使用QQ登录")
    QUICKQQICON = (By.ACCESSIBILITY_ID, "fastLoginQq")  ## 不可见,小图标
    QUICKQQACCOUNT = (By.ACCESSIBILITY_ID, "球球账号")



    ACCOUNTTITLE = (By.ACCESSIBILITY_ID,"账号管理")
    ACCOUNTNICKNAMEMOBILE = (By.ACCESSIBILITY_ID,"手机账号")
    ACCOUNTNICKNAMEEMAIL = (By.ACCESSIBILITY_ID,"邮箱账号")
    ACCOUNTNICKNAMEWEIXIN = (By.ACCESSIBILITY_ID,"微信账号")
    ACCOUNTNICKNAMEWEIBO = (By.ACCESSIBILITY_ID,"微博账号")
    ACCOUNTNICKNAMEQQ = (By.ACCESSIBILITY_ID,"球球账号")

    LOGINCONFIRM = (By.ACCESSIBILITY_ID,"登录")


    ## 验证码登录页面
    TOPASSLOGIN = (By.ACCESSIBILITY_ID,"密码登录") ##点击切换到密码登录
    CLOSELOGIN = (By.ACCESSIBILITY_ID,"invalidLogin") ##关闭登录页面
    WECHATLOGIN = (By.ACCESSIBILITY_ID,"wechatLogin")
    QQLOGIN = (By.ACCESSIBILITY_ID,"qqLogin")
    WEIBOLOGIN = (By.ACCESSIBILITY_ID,"weiboLogin")


    ## 密码登录页面
    TOCODELOGIN = (By.ACCESSIBILITY_ID,"验证码登录")
    INPUTUSER = (By.IOS_PREDICATE,"type =='XCUIElementTypeStaticText' and name =='请输入手机号/邮箱'")
    INPUTUSERACCOUNT = (By.ACCESSIBILITY_ID,"loginAccount")
    INPUTPASS = (By.CLASS_NAME,"XCUIElementTypeSecureTextField")
    LOGINCONFIRM = (By.ACCESSIBILITY_ID,"登录")
    RESETPASS = (By.ACCESSIBILITY_ID,"密码重置")



    COMMENTDATA = "哇塞，这个太太太～～"



    MOREDATA = (By.ACCESSIBILITY_ID,"更多")
    GENRESELECTPRICATE = [By.IOS_PREDICATE,"type =='XCUIElementTypeButton' and name =='%s'"]