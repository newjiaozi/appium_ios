#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.updatePage import UpdatePage as UP
from ..interface import appHomeCard2,appMyFavorite2,v1TitleLikeAndCount


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
                self.savePNG('更新页'+title["title"])

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
            self.savePNG(day[0] + title["title"])
            ele = self.getChildEleClick(cell,(UP.ENDS[0],UP.ENDS[1] % title['title']))
            self.checkViewer(title['title'],title['episodeTitle'])
            self.getBackFromViewer()




    def clickSearch(self):
        self.waitEleClick(UP.SEARCH)

    def clickSubscribe(self):
        self.waitEleClick(UP.SUBSCRIBE)

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
        titles = result["title"]
        titleEpisodeNos = result["titleEpisodeNos"]
        for i in range(0,len(titles)):
            titles[i]["titleEpisodeNos"]=titleEpisodeNos[i]
        if weekday[0] == "今天":
            banner = result["banner"]
            for i in banner:
                # print(i)
                titles.insert(int(i["exposurePosition"]),i)
                # print(titles)
        for i in range(0,len(titles)):
            if titles[i].get("titleNo",None):
                titles[i]["cellName"] = UP.BANNERCELLTEXT+str(i)
            else:
                titles[i]["cellName"] = UP.NOTICEBANNERCELLTEXT+str(i)
        # print(titles)
        return titles

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