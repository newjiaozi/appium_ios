#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.discoveryPage import DiscoveryPage as DP

class DiscoveryPageAction(BasePageAction):

    ## 检查，星期的text都在page中
    def getInDefault(self):
        self.waitEleClick(DP.DISCOVERY)

    def checkDiscoveryPage(self):
        self.waitElePresents(DP.NEWCOME)
        self.waitElePresents(DP.RANK)
        self.waitElePresents(DP.RECOMMEND)
        self.waitElePresents(DP.GENRE)
        self.savePNG("默认发现页页面")

    def getInNewTitle(self):
        self.waitEleClick(DP.NEWTITLE)

    def getInRank(self):
        self.waitEleClick(DP.RANK)

    def getInRecommend(self):
        self.waitEleClick(DP.RECOMMEND)

    def getInGenre(self):
        self.waitEleClick(DP.GENRE)

    def getInWeekRank(self):
        self.waitEleClick(DP.WEEKRANK)

    def getInNewRank(self):
        self.waitEleClick(DP.NEWRANK)

    def getInTotalRank(self):
        self.waitEleClick(DP.TOTALRANK)