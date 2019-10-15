#coding=utf-8


from .baseTestcase import BaseTestcase



class UpdatePageTestcase(BaseTestcase):

    def test001_checkMonday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=1)))

    def test002_checkTuesday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=2)))

    def test003_checkWednesday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=3)))

    def test004_checkThursday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=4)))

    def test005_checkFriday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=5)))

    def test006_checkSaturday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=6)))

    def test007_checkSunday(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=7)))

    def test008_checkFinish(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getEveryDayByInterface(self.UPA.getWeekday(whichDay=8)))

    def test021_checkSubscribeHasData(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.subscribehasData())

    def test022_checkSubscribeNoData(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.subscribeNoData())

    def test031_checkDefaultSearch(self):
        self.UPA.toDefaultPage("UPDATE")
        self.assertTrue(self.UPA.getInUpdatePageSearch())
        self.assertTrue(self.UPA.checkGenreUI())
        self.assertTrue(self.UPA.checkDefaultSearchUI())

