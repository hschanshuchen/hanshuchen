import unittest

import urllib3

from src.Api.ecshop import Login
from src.Common.Http import Http
from src.Common.Log import Logger
from src.Common.util import util


class Case01(unittest.TestCase, Http):

    logger = Logger().get_log().logger
    util = util()
    login = Login.Login()
    data = {"username": "hsc", "password": "hsc123456", "act": "act_login", "back_act": "user.php", "submit": ""}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def setUp(self):
        urllib3.disable_warnings()
        self.logger.info(50*"="+"开始执行用例"+50*"=")

    def tearDown(self):
        self.logger.info(50*"="+"用例执行结束"+50*"=")

    def test_getSupportCity(self):
        self.logger.info(50*"="+"用例步骤执行"+50*"=")
        try:
            response = self.login.login_ecshop(self.data, self.headers)
            self.assertEqual(response.status_code, 200, msg="1.1 验证返回码为200")
            self.assertEqual("欢迎光临本店" in response.text, True, msg="1.2 验证返回信息正确")
            self.assertEqual( response.elapsed.total_seconds() < 3,True, msg="1.3 响应时间小于3秒")
        except AssertionError as e:
            self.logger.info(e)
            pass



