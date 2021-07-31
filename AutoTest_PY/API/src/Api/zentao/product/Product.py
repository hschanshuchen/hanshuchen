import re
import requests
from login.Login import Login
from util import util


class Product:

    def __init__(self):
        self.login = Login()
        self.cookies = self.login.login_zentao()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic emVudGFvOm4zcGEwSmpsak0x",
                        }

    def addProduct(self, hostIp, data):
        respons = requests.post(url="http://%s/zentao/product-create.html" % hostIp, headers=self.headers, data=data,
                                cookies=self.cookies)
        return respons

    def deleteProduct(self, hostIp, id):
        cookies01 = self.cookies
        respons = requests.post(url="http://%s/zentao/product-delete-%s-yes.html" % (hostIp, id),
                                headers=self.headers,
                                cookies=cookies01)
        return respons


if __name__ == "__main__":
    p = Product()
    u = util()

    # res = p.addProduct("127.0.0.1", u.getRandomStr(45), u.getRandomStr(45))
    # print(res.text)
    # id = int(res.text.split("self.location='/zentao/product-browse-")[1].split(".")[0])
    # print(id)

    # for i in range(2000):
    #     re=p.addProduct("127.0.0.1",u.getRandomStr(45),u.getRandomStr(45))
    #     print(re.text)

    for i in range(20000):
        re = p.deleteProduct("127.0.0.1", i)
        print("第  %s  次执行删除"%i)
