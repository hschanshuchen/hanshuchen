import re
import requests
from src.Common.MD5 import MD5
from src.Common.util import util


class Login:

    def __init__(self):
        self.session = requests.Session()
        self.username = util().get_user("username")
        self.password = util().get_user("password")
        self.md5 = MD5()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic emVudGFvOm4zcGEwSmpsak0x"}

    def step1(self):
        """
        登陆首页，获取verifyRand
        :return:
        """
        verifyRand = ""
        while (True):
            # 使用session发起请求
            response1 = self.session.get("http://127.0.0.1/zentao/user-login.html", headers=self.headers)
            response1.encoding = 'utf-8'
            # 响应中获取verifyRand元素对应的属性值
            rand = re.findall("id='verifyRand' value='(\d+)'", response1.text)
            if len(rand[0]) == 10:
                verifyRand = rand[0]
                break
        return verifyRand

    def step2(self):
        """
        发送登录接口，获取重定向url
        :return:
        """
        verifyRand = self.step1()
        # 组装加密后的密码
        password_md5 = self.md5.encrypt_md5(self.password)
        password_verifyRand = password_md5 + verifyRand
        pwd = self.md5.encrypt_md5(password_verifyRand)
        # 发送登录请求
        data = {"account": "admin", "password": pwd, "referer": "http://127.0.0.1/zentao/my.html",
                "verifyRand": verifyRand}
        response2 = self.session.post("http://127.0.0.1/zentao/user-login.html", headers=self.headers, data=data)
        response2.encoding = 'utf-8'
        return response2

    def step3(self):
        """
        发送接口，进入登录后首页
        :return:
        """
        response2 = self.step2()
        rand0 = response2.text[response2.text.rfind('http'):]
        url3 = rand0[:rand0.rfind('\';')]
        response3 = self.session.get(url3, headers=self.headers)
        response3.encoding = 'utf-8'

        result0 = response3.text[response3.text.rfind("zentao/user-logout.html"):]
        result1 = result0[:result0.rfind("</li></ul></li>")]
        result2 = result1[:result1.rfind("</a>")]
        result = result2[result2.rfind(" >"):][2:]

        print(result)
        return response3


if __name__ == "__main__":
    L = Login()
    s = L.step3()
