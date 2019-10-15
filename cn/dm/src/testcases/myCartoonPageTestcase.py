#coding=utf-8


from .baseTestcase import BaseTestcase
from ..login import Config

class MyCartoonPageTestcase(BaseTestcase):

    def test002_NoRecently(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInRecently())
        self.assertTrue(self.MCPA.checkRecentLook(hasdata=False))

    def test003_NoSubscribeToLogin(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInSubscribe())
        self.MCPA.checkSubscribeNoLogin()
        self.assertTrue(self.MPA.loginByPassNotLoginPage(user=Config("mobile"),passwd=Config("passwd"),successText="没有关注的漫画。 添加到我的关注 新的章节更新时，会提醒您。"))
        # self.assertTrue(self.MCPA.getInRecently())
        # self.assertTrue(self.MCPA.getInSubscribe())
        # self.assertTrue(self.MCPA.checkMySubscribe(hasdata=False,newlogin=True))

    def test005_NoSave(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInSave())
        self.assertTrue(self.MCPA.checkSave(hasdata=False))

    def test006_NoComment(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInMyComment())
        self.assertTrue(self.MCPA.checkMyComment(hasdata=False))


    def test011_hasRecently(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInRecently())
        self.assertTrue(self.MCPA.checkRecentLook(hasdata=False,readOne=True))
        self.assertTrue(self.MCPA.checkRecentLook())

    def test013_deleteRecently(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInRecently())
        self.assertTrue(self.MCPA.deleteRecently())

    def test014_hasSubscribe(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInSubscribe())
        self.assertTrue(self.MCPA.checkMySubscribe())

    def test015_deleteSubscribe(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInSubscribe())
        self.assertTrue(self.MCPA.deleteMySubscribe())

    def test016_hasSave(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInSave())
        self.assertTrue(self.MCPA.checkSaveData())

    def test017_deleteSave(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInSave())
        self.assertTrue(self.MCPA.deleteSaveData())

    def test018_hasComment(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInMyComment())
        self.assertTrue(self.MCPA.checkMyComment())

        #"点击编辑，点击删除开始的，btn，点击删除，点击确定。"
    def test020_deleteComment(self):
        self.MCPA.toDefaultPage("MYTOON")
        self.assertTrue(self.MCPA.getInMyComment())
        self.assertTrue(self.MCPA.deleteCommentData())
