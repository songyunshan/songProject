# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import os
import requests
class Test(unittest.TestCase):
    def testMinus(self):
        url = "http://carowner.boldseas.com/card/send-manufacturers-card?openId=oRGinjoFN6vZMPDcAllWdxdbYL2M&templateId=cardTemplateId201903041683276892"
        r = requests.get(url)
        print(r.status_code)
        self.assertEqual(r.status_code,200)
    def testDivide(self):
        result = 7/2
        hope = 3.5
        self.assertEqual(result,hope)
if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Test("testMinus")) #加入测试用例
    suite.addTest(Test("testDivide"))

    report_path = "C:\\Users\\sys\\PycharmProjects\\songNewProject\\venv\\test\\report\\result.html"
    htmlpath = os.path.join(report_path,"result.html")
    print(htmlpath)
    fp = open(report_path , "wb") #打开文件写入
    #运行器
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='这是宋昀珊的自动化测试报告',description='用例执行情况：')
    runner.run(suite)
    fp.close()


