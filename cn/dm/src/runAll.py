#coding=utf-8

import unittest
from cn.dm.src.testcases.HTMLTestRunner import HTMLTestRunner

# from cn.dm.src.testcases.allTestcase import MyPageTestcase,MyCartoonTestcase,DiscoveryTestcaee,UpdateTestCase

from cn.dm.src.testcases.discoveryPageTestcase import DiscoveryPageTestcase
from cn.dm.src.testcases.myPageTestcase import MyPageLoginTestcase,MyPageTestcase
from cn.dm.src.testcases.myCartoonPageTestcase import MyCartoonPageTestcase
from cn.dm.src.testcases.updatePageTestcase import UpdatePageTestcase



import os
def runAll():
    result_path = os.path.abspath(os.path.join(os.path.curdir,"results","IOS测试报告.html"))
    print(result_path)
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyPageLoginTestcase))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyPageTestcase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyCartoonPageTestcase))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(DiscoveryPageTestcase))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UpdatePageTestcase))

    with open(result_path,'wb') as f:
        runner = HTMLTestRunner(stream=f, title='IOS测试报告', description='测试报告 详细信息')
        runner.run(suite)

if __name__ == "__main__":
    runAll()