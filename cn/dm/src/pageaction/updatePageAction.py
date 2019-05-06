#coding=utf-8


from .basePageAction import BasePageAction
from ..pageobject.updatePage import UpdatePage as UP


class UpdagePageAction(BasePageAction):

    ## 检查，星期的text都在page中
    def getInDefault(self):
        self.waitPresents(UP.RQBTN)
        weekdays = self.getWeekday()
        for day in weekdays:
            assert self.waitTextInPage(day) is True
        self.savePNG("更新页默认页")




