import unittest

from src.Common import Log
from src.Common.configHttp import configHttp


class Case01(unittest.TestCase):
    http = configHttp()
    logger = Log.MyLog.get_log()
    url = 'https://api.apiopen.top/getJoke?page=1&count=2&type=video'


    def setUp(self):
        self.logger.info("开始执行用例")
    def tearDown(self):
        self.logger.info("用例执行结束")
    def test_getSupportCity(self):
        self.logger.info("用例步骤执行")
        # self.http.params={"byProvinceName":54339}
        # res=self.http.get()
        # print(res)