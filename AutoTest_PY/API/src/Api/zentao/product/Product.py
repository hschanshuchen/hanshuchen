from bs4 import BeautifulSoup

from Http import Http
from login.Login import Login
from util import util


class Product:

    def __init__(self):
        self.http = Http()
        self.login = Login()
        self.params = {}
        self.files = {}
        self.json = {}
        self.cookies = self.login.login_zentao()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic emVudGFvOm4zcGEwSmpsak0x",
                        }

    def addProduct(self, hostIp, data):
        respons = self.http.post("http://%s/zentao/product-create.html" % hostIp, self.headers, self.cookies, data)
        return respons

    def getAllProduct(self, hostIp):
        respons = self.http.post("http://%s/zentao/product-all.html" % hostIp, self.headers, self.cookies)
        return respons

    def deleteProduct(self, hostIp, id):
        respons = self.http.post("http://%s/zentao/product-delete-%s-yes.html" % (hostIp, id), self.headers,
                                 self.cookies)
        return respons


# if __name__ == "__main__":
#     p = Product()
#     u = util()
#     productIdList = []
#     res = p.getAllProduct("127.0.0.1")
#     soup = BeautifulSoup(res.content, "html.parser")
#     productTagList = soup.find_all("input", type='checkbox')
#
#     for tag in productTagList:
#         productIdList.append(tag.get("value"))
#     print(productIdList)
    # data = {"name": "productName_" + util().getRandomStr(5),
    #         "code": "productCode_" + util().getRandomStr(5),
    #         "line": 0,
    #         "PO": "admin",
    #         "QD": "",
    #         "RD": "",
    #         "type": "normal",
    #         "desc": "",
    #         "acl": "open",
    #         "uid": "6104402102131"
    #         }
    # res = p.addProduct("127.0.0.1", data)
    # print(res.text)

    # for i in range(2000):
    #     re = p.addProduct("127.0.0.1", u.getRandomStr(45), u.getRandomStr(45))
    #     print(re.text)

    # for i in range(20000):
    #     re = p.deleteProduct("127.0.0.1", i)
    #     print("第  %s  次执行删除" % i)
