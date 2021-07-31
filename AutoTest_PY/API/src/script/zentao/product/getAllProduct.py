import re
import unittest
from bs4 import BeautifulSoup
from Config import Config
from Log import Logger
from product.Product import Product
from util import util


class GatAllProduct(unittest.TestCase):
    def setUp(self):
        self.logger = Logger().get_log().logger
        self.logger.info("开始执行用例 %s " % self.id())
        self.conf = Config()
        self.hostIp = self.conf.get_http("localhost")
        self.username = self.conf.get_user("username")
        self.product = Product()
        self.productIdList = []

    def test_getAllProduct_001(self):
        self.logger.info("用例步骤执行 %s" % self.id())
        self.data = {"name": "productName_" + util().getRandomStr(5),
                     "code": "productCode_" + util().getRandomStr(5),
                     "line": 0,
                     "PO": self.username,
                     "QD": "",
                     "RD": "",
                     "type": "normal",
                     "desc": "",
                     "acl": "open",
                     "uid": "6104402102131"
                     }
        response = self.product.addProduct(self.hostIp, self.data)
        self.assertEqual(200, response.status_code, "验证码是200")
        msg = re.findall(r"alert\('(.+?)'\)", response.text)[0]
        self.assertEqual("保存成功", msg, "返回提示信息保存成功")

        response = self.product.getAllProduct(self.hostIp)
        soup = BeautifulSoup(response.content, "html.parser")
        productTagList = soup.find_all("input", type='checkbox')
        for tag in productTagList:
            self.productIdList.append(tag.get("value"))

    def tearDown(self):
        self.logger.info("环境清理 %s " % self.id())
        for n in self.productIdList:
            response = self.product.deleteProduct(self.hostIp, n)
            self.assertEqual(200, response.status_code, "验证码是200")
        self.logger.info("\n\n" + "=" * 180 + "\n")
