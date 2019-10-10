#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.discoveryPage import DiscoveryPage as DP
from ..interface import appGenrelist2,appTitleRanking,appHome4DM,appHome4Priority,appHomeRecommend2,appHomeLeaduplook,appHomeMenuModuleMore
from ..logger import logger
import random



class DiscoveryPageAction(BasePageAction):

    ## 检查，星期的text都在page中
    def getInDiscoveryPage(self):
        logger.info("进入发现页")
        self.waitEleClick(DP.DISCOVERY)


    def checkMenuDetail(self):
        pass

    def getInBigBanner(self):
        self.waitEleClick(DP.BIGBANNER)

    def getInRank(self):
        self.waitEleClick(DP.RANK)

    def getInRecommend(self):
        self.waitEleClick(DP.RECOMMEND)

    def getInGenre(self):
        logger.info("进入分类页")
        return self.waitEleClick(DP.GENRE)

    def getInWeekRank(self):
        self.waitEleClick(DP.WEEKRANK)

    def getInNewRank(self):
        self.waitEleClick(DP.NEWRANK)

    def getInTotalRank(self):
        self.waitEleClick(DP.TOTALRANK)

    def getInDiscoveryXXPage(self,xx="推荐"):
        logger.info("进入%s页" % xx)
        return self.waitEleClick((DP.IDTOBE[0],DP.IDTOBE[1] % xx))

    def getInRecently(self):
        self.waitEleClick(DP.RECENTLY)

    def getInRecentlyMore(self):
        self.waitEleClick(DP.RECENTLYMORE)

    def getInDMRecommend(self):
        self.waitEleClick(DP.DMRECOMMEND)

    def getInDMRecommendMore(self):
        if self.swipeUpUntilDisplay(DP.DMMORE,maxTimes=10):
            if self.waitEleClick(DP.DMMORE):
                data = appHomeRecommend2()
                if data:
                    self.sleep(1)
                    self.savePNG("咚漫推荐页")
                    return self.checkPageWebtoonData(data)
                else:
                    return False
            return False
        else:
            return False

    def getInPriority(self):
        self.waitEleClick(DP.PRIORITY)

    def getInPriorityMore(self):
        if self.swipeUpUntilDisplay(DP.PRIORITYMORE,maxTimes=10):
            if self.waitEleClick(DP.PRIORITYMORE):
                data = appHomeLeaduplook()
                if data:
                    self.sleep(1)
                    self.savePNG("抢先看页")
                    return self.checkPageData(data)
                else:
                    return False
            else:
                return False
        else:
            return False

    def getInNewTitle(self):
        self.waitEleClick(DP.NEWTITLE)

    def getInNewTitleMore(self):
        if self.swipeUpUntilDisplay(DP.NEWTITLEMORE,maxTimes=10):
            if self.waitEleClick(DP.NEWTITLEMORE):
                data = self.getNewTitle()
                if data:
                    self.sleep(1)
                    self.savePNG("新作推荐")
                    return self.checkPageData(data,check1="title",check2="synopsis")
                else:
                    return False
            else:
                return False
        else:
            return False

    def getInGenreMore(self):
        if self.swipeUpUntilDisplay(DP.GENREMORE,maxTimes=10):
            self.savePNG("分类页")
            return self.waitEleClick(DP.GENREMORE)
        else:
            return False

    def getInTheme(self):
        self.waitEleClick(DP.THEME)

    def getInThemeMore(self):
        if self.swipeUpUntilDisplay(DP.THEMEMORE,maxTimes=10):
            self.savePNG("主题专区")
            return self.waitEleClick(DP.THEMEMORE)
        else:
            return False

    def getInRankMore(self):
        if self.swipeUpUntilDisplay(DP.RANKMORE,maxTimes=10):
            if self.waitEleClick(DP.RANKMORE):
                rankData = appTitleRanking()
                if rankData:
                    if self.waitEleClick(DP.NEWRANKPAGE):
                        data = rankData["newrank"]
                        res1 = self.checkRankPageData(data,1,rankType="new")
                    else:
                        return False

                    if self.waitEleClick(DP.WEEKRANKPAGE):
                        data = rankData["uprank"]
                        res2 = self.checkRankPageData(data,1,rankType="week")
                    else:
                        return False
                    if self.waitEleClick(DP.TOTALRANK):
                        data = rankData["totalrank"]
                        res3 = self.checkRankPageData(data,1,rankType="total")
                    else:
                        return False
                    return res1 and res2 and res3
                    # return res3
                else:
                    return False
            else:
                return False
        else:
            return False


    def checkRankPageData(self,data,randomCount=3,rankType="total"):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)

        count = 0
        res3 = False
        for i in range(0,data_length):
            likeText = self.handleTitleLikeCount(data[i]["webtoon"]["likeitCount"])
            if rankType == "total":
                res1 = self.swipeUpUntilSubElesDisplay((DP.TOTALRANKTITLECELL[0], DP.TOTALRANKTITLECELL[1] % i),
                                                  [(DP.IDTOBE[0], DP.IDTOBE[1] % data[i]["webtoon"]["title"]),(DP.IDTOBE[0],DP.IDTOBE[1] % likeText)],
                                                  maxTimes=10)
            elif rankType == "week":
                res1 = self.swipeUpUntilSubElesDisplay((DP.WEEKRANKTITLECELL[0], DP.WEEKRANKTITLECELL[1] % i),
                                                  [(DP.IDTOBE[0], DP.IDTOBE[1] % data[i]["webtoon"]["title"]),(DP.IDTOBE[0],DP.IDTOBE[1] % likeText)],
                                                  maxTimes=10)
            elif rankType == "new":
                res1 = self.swipeUpUntilSubElesDisplay((DP.NEWRANKTITLECELL[0], DP.NEWRANKTITLECELL[1] % i),
                                                  [(DP.IDTOBE[0], DP.IDTOBE[1] % data[i]["webtoon"]["title"]),(DP.IDTOBE[0],DP.IDTOBE[1] % likeText)],
                                                  maxTimes=10)
            else:
                return False
            if i in randomData:
                if self.waitEleClick((DP.IDTOBE[0],DP.IDTOBE[1] % data[i]["webtoon"]["title"])):
                    res3 = self.checkGetInViewerOrPreview(data[i]["webtoon"]["titleNo"])
                else:
                    res3 = False
            if res1:
                count+=1
            else:
                return False
        if count == len(randomData):
            return True and res3
        else:
            return False






    def checkPageData(self,data,check1="title",check2="shortSynopsis",randomCount=3):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        res3 = True
        for i in range(0,data_length):
            res1 = self.swipeUpUntilDisplay((DP.IDTOBE[0],DP.IDTOBE[1] % data[i][check1]),maxTimes=10)
            if check2:
                if len(data[i][check2]) > 100:
                    res2 = self.swipeUpUntilDisplay((DP.ENDS[0],DP.ENDS[1] % data[i][check2][-20:]))
                else:
                    res2 = self.swipeUpUntilDisplay((DP.IDTOBE[0],DP.IDTOBE[1] % data[i][check2]),maxTimes=10)
            else:
                res2 = True
            if i in randomData:
                if self.waitEleClick((DP.IDTOBE[0],DP.IDTOBE[1] % data[i][check1])):
                    res3 = self.checkGetInViewerOrPreview(data[i]["titleNo"])
                else:
                    res3 = False
            if res1 and res2 and res3:
                count += 1
            else:
                return False
        if count == len(randomData):
            return True
        else:
            return False



    def checkCutomizePageData(self,data,fatherId,check1="title",check2="shortSynopsis",randomCount=3):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        res3 = True
        for i in range(0,data_length):
            res1 = self.swipeUpUntilDisplay((DP.CUSTOMIZEMENUMODULETITLE[0],DP.CUSTOMIZEMENUMODULETITLE[1] % (fatherId,data[i][check1])),maxTimes=10)
            res2 = self.swipeUpUntilDisplay((DP.CUSTOMIZEMENUMODULETITLE[0],DP.CUSTOMIZEMENUMODULETITLE[1] % (fatherId,data[i][check2])),maxTimes=10)

            if i in randomData:
                if self.waitEleClick((DP.IDTOBE[0],DP.IDTOBE[1] % data[i][check1])):
                    res3 = self.checkGetInViewerOrPreview(data[i]["titleNo"])
                else:
                    res3 = False
            if res1 and res2 and res3:
                count += 1
            else:
                return False
        if count == len(randomData):
            return True
        else:
            return False



    def checkCustomizeGenreData(self,data,check1="title",check2="shortSynopsis",randomCount=3):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        res3 = True
        if self.swipeUpUntilDisplay((DP.CUSTOMIZEMENUGENRERANKTITLE[0], DP.CUSTOMIZEMENUGENRERANKTITLE[1] % data[2][check2]), maxTimes=10):
            ele = self.waitElePresents(DP.CUSTOMIZEMENUGENRERANK)
            for i in range(0,data_length):
                res1 = self.swipeLeftByEleLocation((DP.CUSTOMIZEMENUGENRERANKTITLE[0],DP.CUSTOMIZEMENUGENRERANKTITLE[1] % data[i][check1]),ele,maxTimes=10)
                res2 = self.swipeLeftByEleLocation((DP.CUSTOMIZEMENUGENRERANKTITLE[0],DP.CUSTOMIZEMENUGENRERANKTITLE[1] % data[i][check2]),ele,maxTimes=10)
                if i in randomData:
                    if self.waitEleClick((DP.CUSTOMIZEMENUGENRERANKTITLE[0],DP.CUSTOMIZEMENUGENRERANKTITLE[1] % data[i][check1])):
                        res3 = self.checkGetInViewerOrPreview(data[i]["titleNo"])
                    else:
                        res3 = False
                if res1 and res2 and res3:
                    count += 1
                else:
                    return False
            if count == len(randomData):
                return True
            else:
                return False
        else:
            return False




    def getInFavourite(self):
        self.waitEleClick(DP.FAVOURITE)

    def getInFavouriteMore(self):
        self.waitEleClick(DP.FAVOURITEMORE)

    def getInBarBanner(self,seq=0):
        barbanner = self.home["barbanner"]
        if seq == 0:
            if self.swipeUpUntilDisplay(DP.BARBANNER0):
                self.waitEleClick(DP.BARBANNER0)
                return self.handleBanner(barbanner[0])
        else:
            if self.swipeUpUntilDisplay(DP.BARBANNER1):
                self.waitEleClick(DP.BARBANNER1)
                return self.handleBanner(barbanner[1])

    def getInDiscoveryLogin(self):
        self.waitEleClick(DP.DISCOVERYLOGINBANNER)

    def clickDiscoveryTop(self):
        self.waitEleClick(DP.DISCOVERYTOP)




    def checkRankUI(self):
        weekrank = False
        newrank = False
        totalrank = False
        if self.waitEleVisiable(DP.WEEKRANK):
            weekrank = True
        if self.waitEleVisiable(DP.NEWRANK):
            newrank = True
        if self.waitEleVisiable(DP.TOTALRANK):
            totalrank = True
        self.savePNG("排行榜页")
        return weekrank and newrank and totalrank


    def checkMainUI(self,new=True,login=True):
        bigbanner = False
        rank = False
        dm = False
        priority = False
        newtitle = False
        barbanner0 = True
        barbanner1 = True
        genre = False
        theme =  False
        loginui = False
        search = False
        topbtn = False
        if new:
            if self.checkDefaultHotWord():
                search = True
                self.savePNG("SEARCHHOTWORD")
            if self.checkTopGrenreRank():
                topbtn = True
                self.savePNG("TOPGENRERANK")
            if self.checkBigBanner():
                bigbanner = True
                self.savePNG("BIGBANNER")
            if self.checkMainRankUI():
                rank = True
                self.savePNG("RANK")
            if self.checkMainDMRecommendUI():
                dm = True
                self.savePNG("DMRECOMMEND")

            if self.checkMainPriorityUI():
                priority=True
                self.savePNG("MainPriority")

            if self.checkMainNewTitleUI():
                newtitle = True
                self.savePNG("MAINNEWTITLE")

            # if self.checkBarBanner():
            #     barbanner0 = True
            #     self.savePNG("BARBANNER0")
            #
            # else:
            #     # self.scroll2VisibleById(DP.BARBANNER0[1])
            #     self.swipeOneScreen()
            #     barbanner0 = self.checkBarBanner()
            #     self.savePNG("BARBANNER0")

            if self.checkMainGenreUI():
                genre = True
                self.savePNG("MAINGENRE")

            if self.checkMainThemeUI():
                theme = True
                self.savePNG("MAINTHEME")

            # if not login:
            #     if self.checkLoginBanner():
            #         loginui = True
            #         self.savePNG("LOGINBANNER")

            # if self.checkBarBanner(seq=1):
            #     barbanner1 = True
            #     self.savePNG("BARBANNER1")
            #
            # else:
            #     # self.scroll2VisibleById(DP.BARBANNER1[1])
            #     self.swipeOneScreen()
            #     barbanner1 = self.checkBarBanner(seq=1)
            #     self.savePNG("BARBANNER1")

        else:
            if self.checkDefaultHotWord():
                search = True
                self.savePNG("SEARCHHOTWORD")
            if self.checkTopGrenreRank():
                topbtn = True
                self.savePNG("TOPGENRERANK")
            if self.checkBigBanner():
                bigbanner = True
                self.savePNG("BIGBANNER")

            if self.checkMainDMRecommendUI():
                dm = True
                self.savePNG("DMRECOMMEND")

            if self.checkMainPriorityUI():
                priority=True
                self.savePNG("MainPriority")

            if self.checkMainNewTitleUI():
                newtitle = True
                self.savePNG("MAINNEWTITLE")

            # if self.checkBarBanner():
            #     barbanner0 = True
            #     self.savePNG("BARBANNER0")
            #
            # else:
            #     self.swipeOneScreen()
            #     barbanner0 = self.checkBarBanner()
            #     self.savePNG("BARBANNER0")

            if self.checkMainRankUI():
                rank = True
                self.savePNG("RANK")


            if self.checkMainGenreUI():
                genre = True
                self.savePNG("MAINGENRE")

            if self.checkMainThemeUI():
                theme = True
                self.savePNG("MAINTHEME")

            if not login:
                if self.checkLoginBanner():
                    loginui = True
                    self.savePNG("LOGINBANNER")

            # if self.checkBarBanner(seq=1):
            #     barbanner1 = True
            #     self.savePNG("BARBANNER1")
            #
            # else:
            #     self.swipeOneScreen()
            #     barbanner1 = self.checkBarBanner(seq=1)
            #     self.savePNG("BARBANNER1")


        self.waitEleClick(DP.DISCOVERYTOP)

        if login:
            # print(bigbanner,rank,dm,priority,newtitle,barbanner0,barbanner1,genre,theme,loginui)
            return bigbanner and rank and dm and priority and newtitle and barbanner0 and barbanner1 and genre and theme and search and topbtn
        else:
            # print(bigbanner,rank,dm,priority,newtitle,barbanner0,barbanner1,genre,theme,loginui)
            return bigbanner and rank and dm and priority and newtitle and barbanner0 and barbanner1 and genre and theme and loginui and search and topbtn


    def checkBigBanner(self):
        bigbanner = self.home["bigbanner"]
        bigbannerCount = len(bigbanner)
        logger.info("共有%s个 bigbanner" % bigbannerCount)
        resultCount = 0
        alreadyCheck = []
        for i in range(0,bigbannerCount):
            bigbannerBtn = self.waitElePresents(DP.BIGBANNER)
            name = bigbannerBtn.get_attribute("name")
            logger.info("BIGBANNER:%s" % name)
            if name:
                index = int(name[-1])
                if index in alreadyCheck:
                    resultCount+=1
                    self.sleep(5)
                    continue
                alreadyCheck.append(index)
            else:
                resultCount += 1
                self.sleep(5)
                continue
            self.tapByXY(self.width/2,self.height/4)
            if self.handleBanner(bigbanner[index]):
                logger.info("handleBanner成功:%s" % name)
                resultCount+=1
            else:
                logger.info("handleBanner失败:%s" % name)
            self.sleep(5)
        if bigbannerCount == resultCount:
            return True
        else:
            logger.info("bigbannerCount:%s,resultCount:%s" % (bigbannerCount,resultCount))
            return False

    def swipeLeftBigBanner(self,loc,bannerSize,times=0):
        if times >= 50:
            return False
        if self.waitEleClick(loc,seconds=1):
            return True
        else:
            width = bannerSize["width"]
            height = bannerSize["height"]
            self.scrollSlow(width* 9/10,height/ 2, 0, height/2)
            # self.swipeLeft()
            return self.swipeLeftBigBanner(loc,bannerSize,times)


    def handleBanner(self,banner):
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


    def checkDMRecommendMoreUI(self):
        return self.swipeUpUntilDisplay(DP.DONMANRECOMMEND)

    def checkPriorityMoreUI(self):
        # return self.swipeUpUntilDisplay(DP.DONMANRECOMMEND)

        return self.eleVisiable(DP.PRIORITY)

    def checkNewTitleMoreUI(self):
        return self.swipeUpUntilDisplay(DP.NEWTITLELOGIN)


    def checkThemeMoreUI(self):
        return self.swipeUpUntilDisplay(DP.THEME)

        # return self.eleVisiable(DP.THEME)

    def checkMainRankUI(self):
        res1 = self.checkMainTotalRank()
        res2 = self.checkMainNewRank()
        res3 = self.checkMainWeekRank()
        return res1 and res2 and res3
        # return True

    def checkMainTotalRank(self):
        if self.waitEleClick(DP.TOTALRANK):
            totalRank = self.home["totalrank"]
            return self.checkPageData(totalRank,check2="")
            # totalRankCount = 0
            # for i in totalRank:
            #     self.swipeUpUntilDisplay((DP.RANKMORETITLE[0],DP.RANKMORETITLE[1] % i["title"]),maxTimes=10)
            #     self.waitEleClick((DP.RANKMORETITLE[0],DP.RANKMORETITLE[1] % i["title"]))
            #     if self.checkGetInViewerOrPreview(i["titleNo"],1):
            #         totalRankCount+=1
            # if totalRankCount == len(totalRank):
            #     return True
            # else:
            #     return False
        else:
            False

    def checkMainNewRank(self):
        if self.waitEleClick(DP.NEWRANK):
            newRank = self.home["newrank"]
            return self.checkPageData(newRank,check2="")
            # newRankCount = 0
            # for i in newRank:
            #     self.swipeUpUntilDisplay((DP.RANKMORETITLE[0], DP.RANKMORETITLE[1] % i["title"]),maxTimes=10)
            #     self.waitEleClick((DP.RANKMORETITLE[0], DP.RANKMORETITLE[1] % i["title"]))
            #     if self.checkGetInViewerOrPreview(i["titleNo"]):
            #         newRankCount += 1
            # if newRankCount == len(newRank):
            #     return True
            # else:
            #     return False
        else:
            return False

    def checkMainWeekRank(self):
        if self.swipeUpUntilDisplay(DP.RANKMORE):
            weekRank = self.waitElePresents(DP.WEEKRANK)
            if weekRank:
                self.tapXY(weekRank)
                upRank = self.home["uprank"]
                return self.checkPageData(upRank,check2="")
                # upRankCount = 0
                # for i in upRank:
                #     self.swipeUpUntilDisplay((DP.RANKMORETITLE[0], DP.RANKMORETITLE[1] % i["title"]),maxTimes=10)
                #     self.waitEleClick((DP.RANKMORETITLE[0], DP.RANKMORETITLE[1] % i["title"]))
                #     if self.checkGetInViewerOrPreview(i["titleNo"]):
                #         upRankCount += 1
                # if upRankCount == len(upRank):
                #     return True
                # else:
                #     return False
            else:
                return False
        else:
            return False
        # return self.eleVisiable(DP.RANKMORE)

    def checkMainDMRecommendUI(self):
        fixdata = self.getFixDMData()
        if fixdata:
            success_count = 0
            for i in fixdata:
                title = self.getTitleFromList2(i)
                if self.swipeUpUntilDisplay((DP.DMMORETITLE[0],DP.DMMORETITLE[1] % title["title"]),maxTimes=10):
                    pass
                    if self.swipeUpUntilDisplay((DP.DMMORETITLE[0],DP.DMMORETITLE[1] % title["shortSynopsis"]),maxTimes=10):
                        if self.waitEleClick((DP.DMMORETITLE[0],DP.DMMORETITLE[1] % title["title"])):
                            if self.checkGetInViewerOrPreview(i,1):
                                success_count += 1
                            else:
                                return False
                            if success_count == len(fixdata):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                return self.checkPageData()
        else:
            return self.swipeUpUntilDisplay(DP.DMMORE,maxTimes=10)

        # return self.eleVisiable(DP.DMMORE)
    def getFixDMData(self):
        fixdataTitle = []
        fixdataCount = {}
        for i in range(0,4):
            res = appHome4DM()
            for j in res:
                if j["titleNo"] not in fixdataTitle:
                    fixdataTitle.append(j["titleNo"])
                    fixdataCount[j["titleNo"]] = 1
                else:
                    fixdataCount[j["titleNo"]] += 1

        result = []
        for i in fixdataTitle:
            if fixdataCount[i] == 4:
                result.append(i)
        return result

    def getFixPriorityData(self):
        fixdataTitle = []
        fixdataCount = {}
        for i in range(0,4):
            res = appHome4Priority()
            for j in res:
                if j["titleNo"] not in fixdataTitle:
                    fixdataTitle.append(j["titleNo"])
                    fixdataCount[j["titleNo"]] = 1
                else:
                    fixdataCount[j["titleNo"]] += 1

        result = []
        for i in fixdataTitle:
            if fixdataCount[i] == 4:
                result.append(i)
        return result



    def checkMainPriorityUI(self):
        fixdata = self.getFixPriorityData()
        if fixdata:
            success_count = 0
            for i in fixdata:
                title = self.getTitleFromList2(i)
                if self.swipeUpUntilDisplay((DP.PRIORITYMORETITLE[0],DP.PRIORITYMORETITLE[1] % title["title"]),maxTimes=10):
                    if self.swipeUpUntilDisplay((DP.PRIORITYMORETITLE[0],DP.PRIORITYMORETITLE[1] % title["shortSynopsis"]),maxTimes=10):
                        if self.waitEleClick((DP.PRIORITYMORETITLE[0],DP.PRIORITYMORETITLE[1] % title["title"])):
                            if self.checkGetInViewerOrPreview(i,1):
                                success_count += 1
                            else:
                                return False
                            if success_count == len(fixdata):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return self.swipeUpUntilDisplay(DP.PRIORITYMORE,maxTimes=10)

        # return self.eleVisiable(DP.PRIORITYMORE)

    def checkMainNewTitleUI(self):
        # newTitle = self.home["new"]
        # count = 0
        # for i in newTitle:
        #     self.swipeUpUntilDisplay((DP.NEWTITLEMORETITLE[0], DP.NEWTITLEMORETITLE[1] % i["title"]))
        #     self.waitEleClick((DP.NEWTITLEMORETITLE[0], DP.NEWTITLEMORETITLE[1] % i["title"]))
        #     if self.checkGetInViewerOrPreview(i["titleNo"]):
        #         count += 1
        # if count == len(newTitle):
        #     return True
        # else:
        #     return False
        return self.swipeUpUntilDisplay(DP.NEWTITLEMORE,maxTimes=10)

    def checkMainGenreUI(self):
        if self.swipeUpUntilDisplay(DP.THEMEMORE,maxTimes=10): ##等待主题出现
            count=0
            for i in DP.GENREMAINPAGETEXT:
                if self.waitEleClick((DP.GENREMORETITLE[0],DP.GENREMORETITLE[1] % i)):
                    count+=1
                    self.savePNG(i)
            if count == len(DP.GENREMAINPAGETEXT):
                return True
            else:
                return False
        else:
            return False

        # return self.swipeUpUntilDisplay(DP.GENREMORE)

        # return self.eleVisiable(DP.GENREMORE)

    def checkMainThemeUI(self):
        return self.swipeUpUntilDisplay(DP.THEMEMORE,maxTimes=10)

        # return self.eleVisiable(DP.THEMEMORE)

            # return self.eleVisiable(DP.PARENTBARBANNER1)
    def checkMainRecently(self):
        return self.swipeUpUntilDisplay(DP.RECENTLYMORE)
        # return self.eleVisiable(DP.RECENTLYMORE)

    def checkLoginBanner(self):
        return self.swipeUpUntilDisplay(DP.DISCOVERYLOGINBANNERPARENT)

        # return self.eleVisiable(DP.DISCOVERYLOGINBANNER)

    def checkDefaultHotWord(self):
        res = self.menus
        firsthotword = res[0]["hotWords"]
        if self.eleVisiable((DP.IDTOBE[0],DP.IDTOBE[1] % firsthotword)):
            self.savePNG("HOTWORD",firsthotword)
            return True
        else:
            return False

    def checkTopGrenreRank(self):
        return self.eleVisiable(DP.RANK) and self.eleVisiable(DP.GENRE)

    def checkSearchBtn(self):
        hotWordsTitleNo = self.menus[0]["hotWordsTitleNo"]
        return self.checkTitleList(hotWordsTitleNo)

    def getInSearchInput(self):
        res = self.menus
        firsthotword = res[0]["hotWords"]
        return self.waitEleClick((DP.IDTOBE[0],DP.IDTOBE[1] % firsthotword))

    def getInSearchBtn(self):
        return self.waitEleClick(DP.SEARCHBTN)


    def checkGenrePage(self):
        if self.eleVisiable(DP.GENRESEARCH):
            return self.randomSelectGenre()
        else:
            return False

    def randomSelectGenre(self):
        first = random.choice(DP.GENREPAGETEXTFIRST)
        second = random.choice(DP.GENREPAGETEXTSECOND)
        third = random.choice(DP.GENREPAGETEXTTHIRD)
        logger.info("%s_%s_%s" % (first,second,third))
        self.waitEleClick((DP.GENREPAGEGENRESELECTFIRST[0],DP.GENREPAGEGENRESELECTFIRST[1] % first))
        self.waitEleClick((DP.GENREPAGEGENRESELECTSECOND[0],DP.GENREPAGEGENRESELECTSECOND[1] % second))
        self.waitEleClick((DP.GENREPAGEGENRESELECTTHIRD[0],DP.GENREPAGEGENRESELECTTHIRD[1] % third))
        self.savePNG(first, second, third)
        result = self.getGenreDataAll(first,second,third)
        return self.checkPageData(result,check2="")




    def scrollMainGenre(self,fromloc,toloc):
        self.getXY(fromloc,toloc)
        if self.waitEleVisiable(DP.GENREMORETITLE[0],DP.GENREMORETITLE[1] % "完结"):
            return True
        else:
            return self.scrollSlow()


    ###自定义菜单处理
    def checkCustomizeMenuBanner(self,banners):
        bannerCount = len(banners)
        resultCount = 0
        alreadyCheck = []
        for i in range(0,bannerCount):
            bigbannerBtn = self.waitElePresents(DP.CUSTOMIZEMENUBANNER)
            name = bigbannerBtn.get_attribute("name")
            if name:
                index = int(name[-1])
                if index in alreadyCheck:
                    continue
                alreadyCheck.append(index)
            else:
                continue
            self.tapByXY(self.width/2,self.height/4)
            if self.checkViewer(banners[i]):
                resultCount+=1
            self.sleep(5)
        if bannerCount == resultCount:
            return True
        else:
            return False

    def checkCustomizeMenuGenreRank(self,genre="恋爱"):
        res = self.getGenreDataAll(genre=genre)
        res_length = len(res)
        if res_length < 6:
            return self.waitEleNotPresents(DP.CUSTOMIZEMENUGENRERANK)
        else:
            if self.swipeUpUntilDisplay((DP.CUSTOMIZEMENUGENRERANKTEXT[0],DP.CUSTOMIZEMENUGENRERANKTEXT[1] % genre)):
                return self.checkCustomizeGenreData()
            else:
                return False

    def checkCustomizeMenuFinish(self,genre="恋爱"):
        res = self.getGenreDataAll(genre=genre,status="完结")
        res_length = len(res)
        if res_length < 4:
            return self.waitEleNotPresents(DP.CUSTOMIZEMENUFINISH)
        else:
            return self.checkCutomizePageData(res[:4],DP.CUSTOMIZEMENUFINISH[1],randomCount=2)

    def checkCustomizeMenuList(self,module): ## type1为2X2，type2为2x3
        type = module["typesetting"]
        data = module["titleList"]
        data = list(filter(lambda x:x["fixed"] == "Y",data))
        data_length =len(data)
        if data_length == 0:
            return True
        else:
            if type == 1:
                if data_length == 4:
                    return self.waitEleNotPresents(DP.CUSTOMIZEMENUFINISHMORE) and \
                           self.checkCutomizePageData(data,module["name"],check1="titleName",randomCount=data_length)
                else:
                    return self.checkCutomizePageData(data,module["name"],check1="titleName",randomCount=data_length)
            elif type == 2:
                if data_length == 6:
                    return self.waitEleNotPresents(DP.CUSTOMIZEMENUFINISHMORE) and \
                           self.checkCutomizePageData(data,module["name"],check1="titleName",randomCount=data_length)
                else:
                    return self.checkCutomizePageData(data,module["name"],check1="titleName",randomCount=data_length)


    def checkMenusPage(self):
        menus = self.menus
        result=0
        for menu in menus:
            name = menu["name"]
            if name == "推荐":
                continue
            if self.getInDiscoveryXXPage(name):
                self.defaultPage = True
                if self.checkMenusDetail(menu):
                    result+=1
                else:
                    return False
            else:
                return False
        if result == len(menus)-1:
            return True
        else:
            return False

    def checkMenusDetail(self,menu):
        result = 0
        detail = menu["menuDetail"]
        type = menu["type"]
        banners = detail["bannerList"]
        moduleList = detail["moduleList"]
        # genrePosition = detail["genrePosition"]
        finishedTitlePosition = detail["finishedTitlePosition"]
        if self.checkCustomizeMenuBanner(banners):
            if type == "GENRE":
                moduleList.insert(0,{"genrePosition":{"genreName":menu["genreName"]}})
                moduleList.insert(finishedTitlePosition,{"finishedTitlePosition":{"genreName":menu["genreName"]}})
            for module in moduleList:
                if self.checkMenusDetailByModule(module):
                    result += 1
            if result == len(moduleList):
                return True
            else:
                return False
        else:
            return False


    def checkMenusDetailByModule(self,module):
        if module.get("genrePosition",None):
            return self.checkCustomizeMenuGenreRank(module["genrePosition"]["genreName"])
        elif module.get("finishedTitlePosition",None):
            return self.checkCustomizeMenuFinish(module["genrePosition"]["genreName"])
        else:
            return self.checkCustomizeMenuList(module)

    def checkGenreRankMore(self,genre="恋爱"):
        if self.swipeUpUntilDisplay(DP.CUSTOMIZEMENUGENRERANKMORE):
            self.waitEleClick(DP.CUSTOMIZEMENUGENRERANKMORE)
            res = self.getGenreDataAll(genre)
            if self.checkPageData(res[:9],check2="",randomCount=1):
                return self.getBackBTS()
            else:
                return False
        else:
            return False

    def checkGenreFinishMore(self,genre="恋爱"):
        if self.swipeUpUntilDisplay(DP.CUSTOMIZEMENUFINISHMORE):
            self.waitEleClick(DP.CUSTOMIZEMENUFINISHMORE)
            res = self.getGenreDataAll(genre,status="完结")
            if self.checkPageData(res[:4],check2="",randomCount=1):
                return self.getBackBTS()
            else:
                return False
        else:
            return False

    def checkModuleListMore(self,module):
        menuId = module["menuId"]
        moduleId = module["moduleId"]
        name = module["name"]
        if self.swipeUpUntilDisplay((DP.CUSTOMIZEMENUMODULEMORE[0],DP.CUSTOMIZEMENUMODULEMORE[1] % name)):
            self.waitEleClick((DP.CUSTOMIZEMENUMODULEMORE[0],DP.CUSTOMIZEMENUMODULEMORE[1] % name))
            res = appHomeMenuModuleMore(menuId,moduleId)
            if res:
                if self.checkPageData(res,check1="titleName",randomCount=2):
                    return self.getBack()
                else:
                    return False
            else:
                return False
        else:
            return False

    def checkMenusPageHotword(self):
        menus = self.menus
        result=0
        for menu in menus:
            name = menu["name"]
            if name == "推荐":
                continue
            hotword = menu["hotWords"]
            titleNo = menu["hotWordsTitleNo"]
            if self.getInDiscoveryXXPage(name):
                if self.waitElePresents((DP.IDTOBE[0],DP.IDTOBE[1] % hotword)):
                    self.savePNG(name,hotword)
                    self.getInSearchBtn()
                    if self.checkTitleList(titleNo):
                        result+=1
                        self.getBackFromList()
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if result == len(menus)-1:
            return True
        else:
            return False

    def checkSearchBtnByTitleNo(self,titleNo):
        return self.checkTitleList(titleNo)