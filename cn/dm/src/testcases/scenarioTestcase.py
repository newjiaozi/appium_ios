#coding=utf-8




from .baseTestcase import BaseTestcase


class ScenarioTestcase(BaseTestcase):

    # def test001_readScrollViewer(self):
    #     time.sleep(20)
    #
    # def test002_readCutViewer(self):
    #     time.sleep(20)
    #
    # def test003_readMotionViewer(self):
    #     time.sleep(20)
    #
    # def test004_readActivityViewer(self):
    #     time.sleep(20)
    #
    # def test005_Favourite(self):
    #     time.sleep(20)
    #
    # def test006_Comment(self):
    #     time.sleep(20)
    #
    # def test007_PPL(self):
    #     time.sleep(20)
    #
    # def test008_PPL(self):
    #     time.sleep(20)
    #
    # def test009_Preview(self):
    #     time.sleep(20)
    #
    # def test010_search(self):
    #     time.sleep(20)


    def test021_oneKeyLoginClose(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapOneKeyClose())

    def test022_oneKeyLoginExchangeAccount(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapExchangeAccount())

    def test023_oneKeyLoginUniformYinsi(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapUniformH5())

    def test024_oneKeyLoginDMYinsi(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapYINSI())


    def test025_oneKeyLoginDMUserRules(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapUserRules())

    def test026_oneKeyLogin(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapOneKeyLogin())

    def test027_oneKeyLoginQuickClose(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapCloseOneQuick())

    def test028_oneKeyLoginOtherLogin(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapOtherLogin())

    def test029_oneKeyQuickLogin(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.tapAccountManage(False))
        self.assertTrue(self.MPA.tapOneQuickLogin())

