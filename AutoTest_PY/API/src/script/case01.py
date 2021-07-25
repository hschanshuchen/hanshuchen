import unittest

from src.Common.Log import  Logger


class Case01(unittest.TestCase):
    logger=Logger().get_log().logger
    url = 'https://api.apiopen.top/getJoke?page=1&count=2&type=video'


    def setUp(self):
        self.logger.info("开始执行用例")
    def tearDown(self):
        self.logger.info("用例执行结束")
    def test_getSupportCity(self):
        self.logger.info("用例步骤执行")