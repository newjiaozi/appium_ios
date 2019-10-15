#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.myCartoonPage import MyCartoonPage as  MCP
from ..interface import everyOneWatching,appFavouriteTotalList2,appFavoriteAdd
from ..logger import logger


class MyCartoonPageAction(BasePageAction):

    def getInRecently(self):
        return self.waitEleClick(MCP.RECENTLY)

    ## hasdata=True意思是  有最近观看
    def checkRecentLook(self,hasdata=True,readOne=False):
        if hasdata:
            recentlyCache = self.getCache()
            return self.checkRecentData(recentlyCache)
        else:
            if self.waitEleVisiable(MCP.NORECENTLY):
                if readOne:
                    titles = everyOneWatching()
                    if titles:
                        if self.checkPageWebtoonDataViewer(titles,randomCount=1,addFavourite=True,addComment=True,downloadEpisode=True):
                            logger.info("checkRecentLook成功 %s" % hasdata)
                            return True
                    else:
                        logger.error("checkRecentLook失败 %s" % hasdata)
                        self.savePNG("checkRecentLook失败 %s" % hasdata)
                        return False
                else:
                    return True
            else:
                return False


    ##data为字典，注意
    def checkRecentData(self,data,randomCount=1):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomDictKeys(data.keys(), data_length)
        else:
            randomData = self.getRandomDictKeys(data.keys(),randomCount)
        count = 0
        for i,j in data.items():
            episodeSeqText = "#%s" % j[2]
            titleName = j[0]["title"]
            if self.swipeUpUntilDisplay((MCP.IDTOBE[0],MCP.IDTOBE[1] % titleName),maxTimes=10):
                if self.swipeUpUntilDisplay((MCP.IDTOBE[0],MCP.IDTOBE[1] % episodeSeqText),maxTimes=10):
                    if i in randomData:
                        if self.waitEleClick((MCP.IDTOBE[0],MCP.IDTOBE[1] % titleName)):
                            if self.getBackFromViewerByViewerType(j[0]["viewer"]):
                                count +=1
        if count == len(randomData):
            return True
        else:
            return False



    def clickEveryoneWatching(self,count=1,subscribe=False):
        for i in range(0,count):
            eles = self.waitElesPresents(MCP.EVERYONEWATCHCOUNT)
            eles[0].click()
            if subscribe and i==1:
                self.Scroll2Subscribe()
                self.subscribeA()
                self.clickScrollviewer()
            self.getBackRe()

    def deleteRecently(self):
        if self.waitEleClick(MCP.EDITBTN):
            if self.waitEleClick(MCP.DELETEALL):
                if self.waitEleClick(MCP.SYSCONFIRM):
                    return self.waitEleVisiable(MCP.NORECENTLY)
        logger.info("deleteRecently失败")
        self.savePNG("deleteRecently失败")
        return False

    def getInSubscribe(self):
        return self.waitEleClick(MCP.MYSUBSCRIBE)

    def addFavourite(self,titleNo):
        titles = appFavouriteTotalList2
        if titles:
            return titles
        return appFavoriteAdd(titleNo)

    def checkMySubscribe(self,hasdata=True):
        if hasdata:
            titles = appFavouriteTotalList2()
            if titles:
                return self.checkMySubscribeData(titles)
            else:
                return False
        else:
            if self.waitEleVisiable(MCP.NOMYSUBSCRIBE):
                logger.info("checkMySubscribe成功 %s" % hasdata)
                return True
            else:
                logger.info("checkMySubscribe失败 %s" % hasdata)
                self.savePNG("checkMySubscribe失败 %s" % hasdata)
                return False

    def checkMySubscribeData(self,data,randomCount=1):
        data_length = len(data)
        if data_length < randomCount:
            randomData = self.getRandomInts(data_length, data_length)
        else:
            randomData = self.getRandomInts(data_length,randomCount)
        count = 0
        for i in range(0,data_length):
            if self.swipeUpUntilDisplay((MCP.IDTOBE[0],MCP.IDTOBE[1] % data[i]["title"]),maxTimes=10):
                if i in randomData:
                    if self.waitEleClick((MCP.IDTOBE[0],MCP.IDTOBE[1] % data[i]["title"])):
                        if self.checkTitleList(data[i]["titleNo"],randomCount=randomCount):
                            count +=1
        if count == len(randomData):
            logger.info("checkMySubscribeData成功")
            return True
        else:
            logger.error("checkMySubscribeData失败")
            return False

    def deleteMySubscribe(self):
        if self.waitEleClick(MCP.EDITBTN):
            if self.waitEleClick(MCP.DELETEALL):
                if self.waitEleClick(MCP.SYSCONFIRM):
                    return self.waitTextInPage(MCP.NOMYSUBSCRIBETEXT)
        logger.info("deleteMySubscribe失败")
        self.savePNG("deleteMySubscribe失败")
        return False

    def getInSave(self):
        return self.waitEleClick(MCP.SAVE30)

    def checkSave(self,hasdata=True):
        if hasdata:
            if self.saveData:
                return self.checkSaveData()
        else:
            if self.waitEleVisiable(MCP.NOSAVE30):
                logger.info("checkSave成功 %s" % hasdata)
                return True
            else:
                logger.info("checkSave失败 %s" % hasdata)
                self.savePNG("临时保存 %s " % hasdata)
                return False

    def checkSaveData(self):
        count = 0
        for i in self.saveData:
            title = self.getTitleFromList2(i)
            if self.waitEleClick((MCP.IDTOBE[0],MCP.IDTOBE[1] % title["title"])):
                ele = self.waitElePresents((MCP.IDTOBE[0],MCP.IDTOBE[1] % self.saveData[i][0]))
                if ele:
                    self.tapXY(ele)
                    if self.getBackFromViewerByViewerType(title["viewer"]):
                        if self.getBackBTV():
                            count+=1
        if count == len(self.saveData):
            logger.info("checkSaveData成功")
            return True
        else:
            logger.info("checkSaveData失败")
            return False


    def deleteSaveData(self):
        if self.waitEleClick(MCP.EDITBTN):
            if self.waitEleClick(MCP.DELETEALL):
                if self.waitEleClick(MCP.SYSCONFIRM):
                    return self.eleVisiable(MCP.NOSAVE30)
        logger.error("删除临时保存失败")
        self.savePNG("deleteSaveData失败")
        return False



    def getInMyComment(self):
        return self.waitEleClick(MCP.MYCOMMENT)

    def checkMyComment(self,hasdata=True):
        if hasdata:
            return self.eleVisiable((MCP.IDTOBE[0],MCP.IDTOBE[1] % MCP.COMMENTDATA))
        else:
            if self.waitEleVisiable(MCP.NOCOMMENT):
                logger.info("checkMyComment成功")
                return True
            else:
                logger.info("checkMyComment失败")
                self.savePNG("checkMyComment失败 %s" % hasdata)
                return False

    def deleteCommentData(self):
        if self.waitEleClick(MCP.EDITBTN):
            if self.waitEleClick(MCP.COMMENTDELETEICON):
                if self.waitEleClick(MCP.COMMENTDELETETEXT):
                    if self.waitEleClick(MCP.SYSCONFIRM):
                        return self.eleVisiable(MCP.NOCOMMENT)
        logger.error("删除评论失败")
        self.savePNG("deleteCommentData失败")
        return False


    def checkSubscribeNoLogin(self):
        ele = self.waitEleVisiable(MCP.MYSBUSCRIBEUNLOGIN)
        if ele:
            self.tapTopLogin(ele)
            logger.info("点击登录成功")
            self.deleteComments()
            self.deleteFavourites()



