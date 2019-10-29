#coding=utf-8
import sys

pathPycharm = ['/Users/dongman/PycharmProjects/appium_ios']
for i in pathPycharm:
    sys.path.insert(0,i)
import unittest
from cn.dm.src.testcases.HTMLTestRunner import HTMLTestRunner
from cn.dm.src.testcases.discoveryPageTestcase import DiscoveryPageTestcase
from cn.dm.src.testcases.myPageTestcase import MyPageTestcase
from cn.dm.src.testcases.myCartoonPageTestcase import MyCartoonPageTestcase
from cn.dm.src.testcases.updatePageTestcase import UpdatePageTestcase
from cn.dm.src.testcases.scenarioTestcase import ScenarioTestcase
from cn.dm.src.testcases.commentTestcase import CommentTestcase
from cn.dm.src.handleEmail import sendMail,deleteResultsFiles
import datetime,time
import os
from cn.dm.src.logger import logger


def runAllOneByOne():

    testCaseList = [
                    MyPageTestcase,##MY页面用例
                    MyCartoonPageTestcase,##我的漫画用例
                    DiscoveryPageTestcase,##发现页用例
                    UpdatePageTestcase,##更新页用例
                    # ScenarioTestcase,##场景测试用例
                    # CommentTestcase,##评论测试用例
                    ]
    for testcase in testCaseList:
        try:
            report_name = "IOS测试报告-%s" % testcase().__class__.__name__
            logger.info("%s开始执行##%s%s" % ("*" * 30,report_name, "*" * 30))
            deleteResultsFiles()
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            report_path = os.path.join(os.path.dirname(__file__),"results","%s.html" % report_name)
            suite = unittest.TestSuite()
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testcase))

            with open(report_path,'wb') as f:
                runner = HTMLTestRunner(stream=f, title=report_name, description='测试报告 详细信息')
                runner.run(suite)
        except Exception:
            logger.info(report_name)
        finally:
            time.sleep(20)
            sendMail(now_time,report_name)
            logger.info("%s结束执行##%s%s" % ("*"*30,report_name,"*"*30))

if __name__ == "__main__":
    runAllOneByOne()



