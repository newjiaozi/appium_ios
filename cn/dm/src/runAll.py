#coding=utf-8
import sys

pathPycharm = ['/Users/dongman/PycharmProjects/appium_ios']
for i in pathPycharm:
    sys.path.insert(0,i)
# print(sys.path)
import unittest
from cn.dm.src.testcases.HTMLTestRunner import HTMLTestRunner
from cn.dm.src.testcases.discoveryPageTestcase import DiscoveryPageTestcase
from cn.dm.src.testcases.myPageTestcase import MyPageTestcase
from cn.dm.src.testcases.myCartoonPageTestcase import MyCartoonPageTestcase
from cn.dm.src.testcases.updatePageTestcase import UpdatePageTestcase
from cn.dm.src.testcases.scenarioTestcase import ScenarioTestcase
from cn.dm.src.handleEmail import sendMail,deleteResultsFiles
import datetime,time
from cn.dm.src.logger import logger
import os


def runAll():
    # logger.info(sys.path)
    result_path = os.path.join(os.path.dirname(__file__),"results","IOS测试报告.html")
    # result_path = os.path.abspath(result_path)
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyPageTestcase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyCartoonPageTestcase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(DiscoveryPageTestcase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UpdatePageTestcase))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ScenarioTestcase))

    with open(result_path,'wb') as f:
        runner = HTMLTestRunner(stream=f, title='IOS测试报告', description='测试报告 详细信息')
        runner.run(suite)

if __name__ == "__main__":
    logger.info("\n"*5)
    logger.info("%s开始执行%s" % ("*" * 30, "*" * 30))
    deleteResultsFiles()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        runAll()
        logger.info("%s结束执行%s" % ("*"*30,"*"*30))
    except Exception:
        logger.exception("执行过程中出现异常")
        logger.info("%s结束执行%s" % ("*"*30,"*"*30))
    finally:
        time.sleep(5)
        sendMail(now_time)


