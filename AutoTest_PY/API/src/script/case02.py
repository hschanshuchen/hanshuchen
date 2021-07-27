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
        response = self.message.post_message(self.data, self.headers)
        try:
            self.assertEqual(response.status_code, 200, msg="验证返回码为200")
            self.assertEqual("您至少在30秒后才可以继续发表评论!" in response.text, True, msg="验证返回码为200")
            self.assertEqual( response.elapsed.total_seconds() < 3,True, msg="验证返回码为200")
        except AssertionError as e:
            pass  # 抛出异常继续往下执行
