#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.myCartoonPage import MyCartoonPage as  MCP

class MyCartoonPageAction(BasePageAction):


    def getInRecently(self):
        self.waitEleClick(MCP.RECENTLY)

    ## hasdata=True意思是  有最近观看
    def checkRecentLook(self,hasdata=True):
        if hasdata:
            eles = self.waitElePresents(MCP.RECENTLOOKEPISODENO)
            self.savePNG("有%s个最近观看的漫画" % len(eles))
            if len(eles) > 3:
                # self.waitStaleness(MCP.EVERYONEWATCH)
                self.savePNG("没有大家都在看")
            else:
                self.waitElePresents(MCP.EVERYONEWATCH)
                eles = self.waitElesPresents(MCP.EVERYONEWATCHCOUNT)
                self.savePNG("有最近观看，有%s个大家都在看" % len(eles))
        else:
            if self.waitElePresents(MCP.NORECENTLY):
                self.savePNG("没有最近观看的漫画")
                eles = self.waitElesPresents(MCP.EVERYONEWATCHCOUNT)
                self.savePNG("没有最近观看的漫画,有%s个大家都在看" % len(eles))

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
        self.waitEleClick(MCP.EDITBTN)
        self.waitEleClick(MCP.DELETEALL)
        self.savePNG("全部删除最近观看")
        self.waitEleClick(MCP.SYSCONFIRM)
        self.waitElePresents(MCP.NORECENTLY)
        self.savePNG("全部删除最近观看完成")

    def getInSubscribe(self):
        self.waitEleClick(MCP.MYSUBSCRIBE)

    def checkMySubscribe(self,hasdata=True):
        if hasdata:
            eles = self.waitElesPresents(MCP.MYSUBSCRIBEUPDATETIME)
            if eles:
                self.savePNG("有%s个关注作品" % len(eles))
        else:
            if self.waitElePresents(MCP.NOMYSUBSCRIBE):
                self.savePNG("我的漫画-我的关注-没有数据")


    def deleteMySubscribe(self):
        self.waitEleClick(MCP.EDITBTN)
        self.waitEleClick(MCP.DELETEALL)
        self.savePNG("全部删除我的关注")
        self.waitEleClick(MCP.SYSCONFIRM)
        self.waitElePresents(MCP.NOMYSUBSCRIBE)
        self.savePNG("全部删除我的关注完成")


    def getInSave(self):
        self.waitEleClick(MCP.SAVE30)

    def checkSave(self,hasdata=True):
        if hasdata:
            eles = self.waitElesPresents(MCP.SAVEDATA,seconds=3)
            self.savePNG("有%s个临时保存文件" % len(eles))
        else:
            if self.waitElePresents(MCP.NOSAVE30):
                self.savePNG("没有临时保存文件")




    def getInMyComment(self):
        self.waitEleClick(MCP.MYCOMMENT)

    def checkMyComment(self,hasdata=True):
        if hasdata:
            eles = self.waitElesPresents(MCP.COMMENTEPISODENO)
            self.savePNG("有%条评论" % len(eles))
        else:
            if self.waitElePresents(MCP.NOCOMMENT):
                self.savePNG("您还没有评论")

