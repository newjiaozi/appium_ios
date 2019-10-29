#coding=utf-8


from .baseTestcase import BaseTestcase


class CommentTestcase(BaseTestcase):

    def test001_commentScroll(self):
        self.DPA.getInFoundPage()
        self.DPA.getInDiscoveryXXPage()
        self.DPA.searchTitle(searchKey="看脸时代")
        self.BPA.checkTitleList()


    def test002_commentCut(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test003_commentMotion(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test004_commentReplyScroll(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test005_commentReplyCut(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test006_commentReplyMotion(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())


    def test011_commentScrollJump(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ())
        self.assertTrue(self.MPA.logout())

    def test012_commentCutJump(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test013_commentMotionJump(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test014_commentReplyScrollJump(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test015_commentReplyCutJump(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())

    def test016_commentReplyMotionJump(self):
        self.MPA.toDefaultPage()
        self.assertTrue(self.MPA.loginByQQ(quick=True))
        self.assertTrue(self.MPA.logout())