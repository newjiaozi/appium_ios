#coding=utf-8


from .baseTestcase import BaseTestcase

class MyCartoonPageTestcase(BaseTestcase):

    def test001_checkDefaultPage(self):
        self.MCPA.getInMyToon()
        self.MCPA.savePNG('我的漫画默认页面')

    def test002_NoRecently(self):
        self.MCPA.getInMyToon()
        self.MCPA.getInRecently()
        self.MCPA.checkRecentLook(hasdata=False)

    def test003_NoSubscribe(self):
        self.MCPA.getInMyToon()
        self.MCPA.getInSubscribe()
        self.MCPA.checkMySubscribe(hasdata=False)

    def test004_NoSave(self):
        self.MCPA.getInMyToon()
        self.MCPA.getInSave()
        self.MCPA.checkSave(hasdata=False)

    def test005_NoComment(self):
        self.MCPA.getInMyToon()
        self.MCPA.getInMyComment()
        self.MCPA.checkMyComment(hasdata=False)


    # def test011_hasRecently(self):
    #     self.MCPA.getInMyToon()
    #     self.MCPA.getInRecently()
    #     self.MCPA.clickEveryoneWatching(3)
    #     self.MCPA.checkRecentLook()
    #     self.MCPA.clickEveryoneWatching(1)
    #     self.MCPA.checkRecentLook()
    #
    #
    # def test013_deleteRecently(self):
    #     self.MCPA.getInMyToon()
    #     self.MCPA.getInRecently()
    #     self.MCPA.deleteRecently()
    #
    #
    # def test014_hasSubscribe(self):
    #     self.MCPA.getInMyToon()
    #     self.MCPA.getInSubscribe()
    #     self.MCPA.checkMySubscribe(hasdata=True)
    #
    # def test015_deleteSubscribe(self):
    #     self.MCPA.getInMyToon()
    #     self.MCPA.getInSubscribe()
    #     self.MCPA.deleteMySubscribe()
    #
    #
    # def test016_hasSave(self):
    #     self.MCPA.getInMyToon()
    #     self.MCPA.getInSave(hasdata=False)
    #
    # def test018_hasComment(self):
    #     self.MCPA.getInMyToon()
    #     self.MCPA.getInMyComment(hasdata=False)