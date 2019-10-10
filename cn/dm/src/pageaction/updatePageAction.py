#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.updatePage import UpdatePage as UP
from ..interface import appHomeCard2,appMyFavorite2,v1TitleLikeAndCount,appFavoriteAdd,appFavoriteTotalRemoveAll
from ..logger import logger
from ..login import Config

class UpdagePageAction(BasePageAction):

    ## 检查，星期的text都在page中
    def getInDefault(self):
        self.waitEleClick(UP.UPDATE)
        self.waitEleClick(UP.RQBTN)
        # weekdays = self.getWeekday(True)
        # for day in weekdays:
        #     self.waitEleClick((UP.IDTOBE[0],UP.IDTOBE[1] % day[0]))
        #     titles = self.getRQDataByWeekday(day)
        #     # title = self.getFirstTitle(titles)
        #     title = titles[0]
        #     self.waitElePresents((UP.IDTOBE[0],UP.IDTOBE[1] % title["cellName"]))
        #     self.savePNG(day[0]+title["title"])

        self.clickToday()
        weekday = self.getWeekday(False)
        titles = self.getRQDataByWeekday(weekday)
        for title in titles:
            # title_name = self.waitElePresents((UP.IDTOBE[0],UP.IDTOBE[1] % "["+title["representGenre"]+"]"+title["title"]))
            title_name = self.waitElePresents((UP.IDTOBE[0],UP.IDTOBE[1] % title["cellName"]))
            if title_name:
                self.scroll2Visible(title_name)
                # self.savePNG('更新页'+title["title"])
                self.savePNG('更新页',title["title"])

        self.savePNG("更新页今天数据底部")

    def getInEveryday(self):
        self.waitEleClick(UP.UPDATE)
        self.waitEleClick(UP.RQBTN)
        weekdays = self.getWeekday(True)
        for day in weekdays:
            self.waitEleClick((UP.IDTOBE[0],UP.IDTOBE[1] % day[0]))
            titles = self.getRQDataByWeekday(day)
            # title = self.getFirstTitle(titles)
            title = titles[0]
            cell = self.waitElePresents((UP.IDTOBE[0],UP.IDTOBE[1] % title["cellName"]))
            self.savePNG(day[0],title["title"])
            ele = self.getChildEleClick(cell,(UP.ENDS[0],UP.ENDS[1] % title['title']))
            self.checkViewer(title['title'],title['episodeTitle'],False)
            self.getBackFromViewer()

    def clickSearch(self):
        logger.info("点击【搜索】")
        return self.waitEleClick(UP.SEARCH)

    def clickSubscribe(self):
        return self.waitEleClick(UP.SUBSCRIBE)

    def clickRQ(self):
        logger.info("点击【人气】")
        return self.waitEleClick(UP.RQBTN)

    def clickToday(self):
        self.waitEleClick(UP.TODAY)

    def checkEveryDay(self):
        days = self.getWeekday()
        for day in days:
            pass

    def getLikeAndCount(self,titleEpisodeNos):
        return v1TitleLikeAndCount(titleEpisodeNos)

    def getMyFavorite2(self):
        return appMyFavorite2()

    def getRQDataByWeekday(self,weekday):
        result = appHomeCard2(weekday[1])
        if result:
            titles = result["title"]
            # titleEpisodeNos = result["titleEpisodeNos"]
            # for i in range(0,len(titles)):
            #     titles[i]["titleEpisodeNos"]=titleEpisodeNos[i]
            if weekday[0] == "今天":
                banner = result["banner"]
                for i in banner:
                    titles.insert(int(i["exposurePosition"]),i)
            for i in range(0,len(titles)):
                if "titleNo" in titles[i]:
                    titles[i]["cellName"] = UP.BANNERCELLTEXT+str(i)
                else:
                    titles[i]["cellName"] = UP.NOTICEBANNERCELLTEXT+str(i)
            # logger.info(titles)
            return titles
        else:
            return False


    def getUpdateSuscribeData(self):
        result = appMyFavorite2()
        if result:
            for i in range(0,len(result)):
                result[i]["cellName"] = UP.FAVOURITEBANNERTEXT+str(i)
            return result
        else:
            return False



    def getFavoriteData(self):
        titleEpisodeNos,titleEpisodeList =  self.getMyFavorite2()
        likeCount = self.getLikeAndCount(titleEpisodeNos)
        for i in range(0,len(titleEpisodeNos)):
            titleEpisodeNos[i].update(likeCount[i])
        return titleEpisodeNos

    def getFirstTitle(self,titles):
        for title in titles:
            if title.get("titleNo",None):
                return title

    def getEveryDayByInterface(self,day):
        if self.waitEleClick(UP.RQBTN):
            dayCode = day[1]
            logger.info("getEveryDayByInterface检查%s的数据" % day[0])
            if  dayCode == "MONDAY":
                self.waitEleClick((UP.IDTOBE[0],UP.IDTOBE[1] % day[0]))
            else:
                self.swipeLeft()
            titles = self.getRQDataByWeekday(day)
            if titles:
                if self.checkUpdatePageData(titles,randomCount=1,maxTimes=500):
                    if dayCode == "COMPLETE":
                        self.swipeDown()
                    logger.info("getEveryDayByInterface检查%s的数据成功" % day[0])
                    return True
            else:
                if dayCode == "COMPLETE":
                    self.swipeDown()
                logger.info("getEveryDayByInterface检查%s的数据失败" % day[0])
                return False
        return False

    def subscribeNoData(self):
        if self.clickSubscribe():
            # eles = self.waitElesPresents(UP.ALREADYSUBSCRIBE)
            # if eles:
            #     for i in range(0,len(eles)):
            #         self.cancelSuscribe()
            if self.waitEleClick(UP.ALREADYSUBSCRIBE):
                return self.waitTextInPage(UP.HAVENOTSUBSCRIBE[1])
        logger.info("subscribeNoData失败")
        return False

    def cancelSuscribe(self):
        eles = self.waitElesPresents(UP.ALREADYSUBSCRIBE)
        if eles:
            for ele in eles:
                self.tapXY(ele)
                break


    def subscribehasData(self):
        if appFavoriteTotalRemoveAll():
            if self.clickSubscribe():
                # if appFavoriteAdd(self.getRandomTitleNo()):
                if appFavoriteAdd(1419):
                    if self.clickSubscribe():
                        if self.getInLogin():
                            self.loginByPassNotLoginPage(user=Config("mobile"),passwd=Config("passwd"),successText="")
                        titles = self.getUpdateSuscribeData()
                        if titles:
                            return self.checkUpdateSubscribePageData(titles,randomCount=1)
        self.savePNG("subscribehasData失败")
        return False

    def getInLogin(self):
        if self.waitEleVisiable(UP.NOLOGINTEXT,seconds=1):
            return self.waitEleClick(UP.NOLOGINLOGIN)
        return False

    def getInUpdatePageSearch(self):
        return self.clickSearch()

    def checkUpdatePageData(self,data,randomCount=3,maxTimes=10):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length,data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        for i in range(0,data_length):
            if i in randomData:
                dataTitle = data[i]
                if dataTitle.get("titleNo",None):
                    titleFromList2 = self.getTitleFromList2(dataTitle["titleNo"])
                    genreTitleText = "[%s]%s" % (dataTitle["representGenreCN"],dataTitle["title"])
                    lastEpisodeNameText = dataTitle["episodeTitle"]
                    # likeCountText = self.handleTitleLikeCount(titleFromList2["likeitCount"])
                    authorText = self.getAuthorText(titleFromList2)
                    favouriteText = "关注"
                    toAllText = "全集"
                    if self.swipeUpUntilSubElesDisplay((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"]),[(UP.IDTOBE[0],UP.IDTOBE[1] % genreTitleText),
                                                                      (UP.IDTOBE[0], UP.IDTOBE[1] % lastEpisodeNameText),
                                                                      (UP.IDTOBE[0], UP.IDTOBE[1] % toAllText),
                                                                      (UP.IDTOBE[0], UP.IDTOBE[1] % authorText),
                                                                      # (UP.IDTOBE[0], UP.IDTOBE[1] % likeCountText),
                                                                      (UP.IDTOBE[0], UP.IDTOBE[1] % favouriteText)],maxTimes=maxTimes):
                        if 1 == self.getRandomInt(1):
                            logger.info("checkViewer")
                            if self.clickChildEle((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"]), (UP.IDTOBE[0], UP.IDTOBE[1] % genreTitleText)):
                                if self.checkViewer(dataTitle["titleNo"], dataTitle["episodeNo"], False):
                                    count +=1
                        else:
                            logger.info("checkTitleList")
                            if self.clickChildEle((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"]), (UP.IDTOBE[0], UP.IDTOBE[1] % toAllText)):
                                if self.checkTitleList(dataTitle["titleNo"],randomCount=1):
                                    count +=1

                else:
                    if self.swipeUpUntilDisplay((UP.IDTOBE[0],UP.IDTOBE[1] % dataTitle["cellName"])):
                        if self.waitEleClick((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"])):
                            if self.handleNoticeBanner(dataTitle):
                                count +=1

        if count == len(randomData):
            return True
        else:
            return False



    def handleNoticeBanner(self,banner):
        linkUrl = banner.get("linkUrl", None)
        linkTitleNo = banner.get("linkTitleNo",None)
        logger.info(banner)
        if linkUrl:
            logger.info("linkUrl:%s" % linkUrl )
            return self.parseScheme(linkUrl,banner)
        elif linkTitleNo:
            logger.info("linkTitleNo:%s" % linkTitleNo )
            return self.checkViewer(linkTitleNo,1)
        else:
            return self.getBackFromViewerByTapXY()


    def checkUpdateSubscribePageData(self,data,randomCount=1,maxTimes=10):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length,data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        for i in range(0,data_length):
            if i in randomData:
                dataTitle = data[i]
                titleFromList2 = self.getTitleFromList2(dataTitle["titleNo"])
                genreTitleText = "[%s]%s" % (dataTitle["representGenreCN"],dataTitle["title"])
                lastEpisodeNameText = dataTitle["episodeTitle"]
                # likeCountText = self.handleTitleLikeCount(titleFromList2["likeitCount"])
                authorText = self.getAuthorText(titleFromList2)
                favouriteText = "已关注"
                toAllText = "全集"
                if self.swipeUpUntilSubElesDisplay((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"]),[(UP.IDTOBE[0],UP.IDTOBE[1] % genreTitleText),
                                                                  (UP.IDTOBE[0], UP.IDTOBE[1] % lastEpisodeNameText),
                                                                  (UP.IDTOBE[0], UP.IDTOBE[1] % toAllText),
                                                                  (UP.IDTOBE[0], UP.IDTOBE[1] % authorText),
                                                                  # (UP.IDTOBE[0], UP.IDTOBE[1] % likeCountText),
                                                                  (UP.IDTOBE[0], UP.IDTOBE[1] % favouriteText)],maxTimes=maxTimes):
                    if 1 == self.getRandomInt(1):
                        logger.info("checkViewer")
                        if self.clickChildEle((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"]), (UP.IDTOBE[0], UP.IDTOBE[1] % genreTitleText)):
                            if self.checkViewer(dataTitle["titleNo"], dataTitle["episodeNo"], False):
                                count +=1
                    else:
                        logger.info("checkTitleList")
                        if self.clickChildEle((UP.IDTOBE[0], UP.IDTOBE[1] % dataTitle["cellName"]), (UP.IDTOBE[0], UP.IDTOBE[1] % toAllText)):
                            if self.checkTitleList(dataTitle["titleNo"],randomCount=1):
                                count +=1


        if count == len(randomData):
            return True
        else:
            return False
