
import unittest
from HTMLTestRunner import HTMLTestRunner
from time import time, strftime, localtime
import os

class HTML:
    def __init__(self):
        # 定义需要执行哪个包下的文件，我要运行项目的文件夹是：当前目录下的父级目录下的“testcases”目录
        self.dir_test = os.path.abspath("../script")
        print(self.dir_test)
        # 获取当前时间
        self.now = strftime("%Y_%m_%d-%H-%M-%S", localtime(time()))
        # 报告位置
        self.filename = os.path.abspath("../result//report//") + self.now + "report.html"

    def htmlTest(self,title,description):
        # 使用unittest.TestLoader().discover方法，运行以case.py结尾的所有py文件
        my_discover = unittest.TestLoader().discover(self.dir_test, "*.py")

        with open(self.filename, "wb") as fp:
        # 定义报告标题，描述，以及报告的详细情况
            runner = HTMLTestRunner(stream=fp,title=title,description=description, verbosity=0)
        # 运行文件
            runner.run(my_discover)


if __name__=="__main__":

    ht=HTML()
    ht.htmlTest("XXX项目接口自动化测试报告","各接口测试用例执行情况")

