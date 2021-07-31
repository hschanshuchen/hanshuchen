import requests

from login.Login import Login




class ProductLine:

    def __init__(self):
        self.login = Login()
        self.cookies = self.login.login_zentao()

        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Authorization": "Basic emVudGFvOm4zcGEwSmpsak0x",
                   }

    def addProductLine(self,hostip,modules,shorts):
        data = {"modules": modules,
                "shorts": shorts,
                "parentModuleID": 0,
                "maxOrder": 0
                }

        respons = requests.post(url="http://127.0.0.1/zentao/tree-manageChild-5-line.html?onlybody=yes", headers=self.headers, data=data,
                        cookies=self.cookies)
        return respons


if __name__=="__main__":

    p=ProductLine()
    res= p.addProductLine("127.0.0.1","1","1")
    print(res.text)
    print(res.status_code)