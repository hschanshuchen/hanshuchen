import unittest

import urllib3

from src.Api.ecshop.Message import Message
from src.Common.Log import Logger


class Case01(unittest.TestCase):
    logger = Logger().get_log().logger
    message = Message()
    data = {"user_email": "2427697226@qq.con", "msg_type": "0", "msg_title": "留言标题", "msg_content": "留言内容",
            "act": "act_add_message"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def setUp(self):
        urllib3.disable_warnings()
        self.logger.info(50*"="+"开始执行用例"+50*"=")

    def tearDown(self):
        self.logger.info(50*"="+"用例执行结束"+50*"=")

    def test_getSupportCity(self):
        self.logger.info(50*"="+"用例步骤执行"+50*"=")

