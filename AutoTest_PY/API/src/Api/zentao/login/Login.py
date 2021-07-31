import hashlib
import re
import requests

from Config import Config
from Http import Http
from src.Common.MD5 import MD5
from src.Common.util import util


class Login:

    def __init__(self):
        self.sid = ""
        self.login_url = "http://127.0.0.1/zentao/user-login.html"
        self.username = Config().get_user("username")
        self.password = Config().get_user("password")
        self.md5 = MD5()
        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic emVudGFvOm4zcGEwSmpsak0x",
                        }

    def step1(self):
        """
        登陆首页，获取verifyRand
        :return:
        """
        sid = ""
        verifyRand = ""
        while (True):
            # 使用session发起请求
            response1 = requests.get(self.login_url, headers=self.headers)
            response1.encoding = 'utf-8'
            # 响应中获取verifyRand元素对应的属性值
            rand = re.findall("id='verifyRand' value='(\d+)'", response1.text)
            if len(rand[0]) == 10:
                verifyRand = rand[0]
                self.sid = response1.cookies["zentaosid"]
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
                "verifyRand": verifyRand, "keepLogin[]": "on"}
        Cookies = dict(zentaosid=self.sid, lang='zh-cn', keepLogin='on')
        response2 = requests.post(self.login_url, headers=self.headers, cookies=Cookies,
                                  data=data)
        response2.encoding = 'utf-8'
        Cookies = dict(zentaosid=self.sid, lang='zh-cn', keepLogin='on', zp=response2.cookies["zp"])
        return Cookies

    def login_zentao(self):
        return self.step2()


if __name__ == "__main__":
    L = Login()
    s2 = L.step2()
    print(s2)

