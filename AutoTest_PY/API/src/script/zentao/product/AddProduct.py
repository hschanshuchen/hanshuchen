import re
import unittest

from src.Api.zentao.product.Product import Product
from src.Common.Config import Config
from src.Common.Log import Logger
from src.Common.Util import Util


class AddProduct(unittest.TestCase):
    def setUp(self):
        self.logger = Logger().get_log().logger
        self.logger.info("开始执行用例 %s " % self.id())
        self.conf = Config()
        self.hostIp = self.conf.get_http("localhost")
        self.username = self.conf.get_user("username")
        self.product = Product()
        self.productIdList = []

    def test_addProduct_001(self):
        self.logger.info("用例步骤执行 %s" % self.id())
        self.data = {"name": "productName_" + Util().getRandomStr(5),
                     "code": "productCode_" + Util().getRandomStr(5),
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
        self.productIdList.append(int(re.findall(r"product-browse-(.+?)\.", response.text)[0]))

    def test_addProduct_002(self):
        self.logger.info("执行用例步骤 %s " % self.id())
        productName = "productName_" + Util().getRandomStr(5)
        self.data = {"name": productName,
                     "code": "productCode_" + Util().getRandomStr(5),
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
        self.productIdList.append(int(re.findall(r"product-browse-(.+?)\.", response.text)[0]))
        response = self.product.addProduct(self.hostIp, self.data)
        msg = re.findall(r"alert\('(.+?)『productName", response.text)[0]
        self.assertEqual("『产品名称』已经有", msg, "产品名称重复校验")

    def test_addProduct_003(self):
        self.logger.info("执行用例步骤 %s " % self.id())
        self.data = {"name": Util().getRandomStr(62) + Util().getRandomStr(29),
                     "code": "productCode_" + Util().getRandomStr(5),
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
        self.assertEqual("『产品名称』长度应当不超过『90』，且大于『0』。", msg, "名称长度校验")

    def tearDown(self):
        self.logger.info("环境清理 %s " % self.id())
        for n in self.productIdList:
            response = self.product.deleteProduct(self.hostIp, n)
            self.assertEqual(200, response.status_code, "验证码是200")
        self.logger.info("\n\n" + "=" * 180 + "\n")
