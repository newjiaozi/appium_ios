#coding=utf-8


from .baseTestcase import BaseTestcase



class UpdatePageTestcase(BaseTestcase):


    def test001_checkEveryToday(self):
        self.UPA.getInEveryday()


    # def test002_scrollToday(self):
    #     self.UPA.getInDefault()

